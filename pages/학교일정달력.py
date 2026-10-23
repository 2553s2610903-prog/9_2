
import streamlit as st
import calendar
import json
import html
from pathlib import Path
from datetime import date

st.set_page_config(
    page_title="우리 학교 플래너",
    page_icon="🌷",
    layout="wide"
)

FILE = Path(__file__).with_name("events.json")

COLORS = {
    "학교 행사": "#6488EA",
    "시험": "#F07178",
    "수행평가": "#A58AE8",
    "준비물": "#E7A64B",
    "휴일": "#5CB99A",
    "기타": "#8793A5"
}

def load_events():
    try:
        if FILE.exists():
            data = json.loads(FILE.read_text(encoding="utf-8"))
            if isinstance(data, list):
                result = []
                for e in data:
                    try:
                        start = date.fromisoformat(e["start"])
                        end = date.fromisoformat(e["end"])
                        if (
                            end >= start
                            and str(e.get("title", "")).strip()
                            and e.get("category") in COLORS
                        ):
                            e["id"] = int(e["id"])
                            result.append(e)
                    except (KeyError, ValueError, TypeError):
                        continue
                return result
    except (OSError, json.JSONDecodeError):
        st.warning("일정 파일을 읽을 수 없습니다.")
    return []

def save_events(events):
    try:
        temp = FILE.with_suffix(".tmp")
        temp.write_text(
            json.dumps(events, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        temp.replace(FILE)
        return True
    except OSError:
        st.error("저장에 실패했습니다.")
        return False

def events_on(events, day):
    return [
        e for e in events
        if date.fromisoformat(e["start"])
        <= day
        <= date.fromisoformat(e["end"])
    ]

if "events" not in st.session_state:
    st.session_state.events = load_events()

events = st.session_state.events
today = date.today()

# 디자인
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f5f6ff, #fff8fb);
}
.block-container {
    max-width: 1250px;
    padding-top: 2rem;
}
.hero {
    background: linear-gradient(120deg, #e4eaff, #f1e6ff, #fff0e8);
    padding: 28px;
    border-radius: 24px;
    margin-bottom: 22px;
}
.hero h1 {
    color: #303957;
    font-size: 2.2rem;
}
.hero p {
    color: #707895;
}
div[data-testid="stMetric"] {
    background: white;
    padding: 16px;
    border-radius: 18px;
    border: 1px solid #ececf7;
}
.event {
    color: white;
    padding: 4px;
    margin-top: 4px;
    border-radius: 6px;
    font-size: 12px;
    overflow-wrap: anywhere;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🌷 우리 학교 일정 달력</h1>
    <p>시험부터 학교 행사까지, 중요한 날을 예쁘게 정리해 보세요!</p>
</div>
""", unsafe_allow_html=True)

# 일정 요약
upcoming = [
    e for e in events
    if date.fromisoformat(e["end"]) >= today
]

c1, c2, c3 = st.columns(3)
c1.metric("🗂️ 전체 일정", f"{len(events)}개")
c2.metric("☀️ 오늘 일정", f"{len(events_on(events, today))}개")
c3.metric("🔔 다가오는 일정", f"{len(upcoming)}개")

tab1, tab2, tab3 = st.tabs([
    "🗓️ 달력 보기",
    "✏️ 일정 추가",
    "📚 일정 관리"
])

# 달력
with tab1:
    chosen = st.date_input("보고 싶은 날짜", value=today)
    year, month = chosen.year, chosen.month

    st.markdown(
        f"<h2 style='text-align:center;color:#404967'>"
        f"{year}년 {month}월</h2>",
        unsafe_allow_html=True
    )

    weekdays = ["월", "화", "수", "목", "금", "토", "일"]
    cols = st.columns(7)

    for col, day_name in zip(cols, weekdays):
        col.markdown(f"**{day_name}**")

    for week in calendar.monthcalendar(year, month):
        cols = st.columns(7)

        for col, number in zip(cols, week):
            with col:
                if number == 0:
                    st.write("")
                    continue

                current = date(year, month, number)
                day_list = events_on(events, current)

                if current == today:
                    st.markdown(
                        f"**<span style='color:#687fe5'>"
                        f"● {number}일</span>**",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(f"**{number}일**")

                with st.container(border=True):
                    if not day_list:
                        st.caption("일정 없음")

                    for e in day_list[:3]:
                        color = COLORS[e["category"]]
                        title = html.escape(e["title"])
                        st.markdown(
                            f'<div class="event" style="background:{color}">'
                            f'{title}</div>',
                            unsafe_allow_html=True
                        )

                    if len(day_list) > 3:
                        st.caption(f"+{len(day_list)-3}개 더")

    st.divider()
    st.subheader("✨ 다가오는 일정")

    upcoming.sort(key=lambda e: e["start"])

    if not upcoming:
        st.info("등록된 일정이 없습니다.")
    else:
        for e in upcoming[:5]:
            st.markdown(
                f"**{e['start']} · {e['title']}** "
                f"({e['category']})"
            )
            if e.get("supplies"):
                st.caption(f"준비물: {e['supplies']}")

# 일정 추가
with tab2:
    st.subheader("✏️ 새로운 일정 등록")

    with st.form("add_form", clear_on_submit=True):
        title = st.text_input("일정 이름")
        category = st.selectbox("일정 종류", list(COLORS))
        start = st.date_input("시작 날짜", value=today, key="add_start")
        end = st.date_input("종료 날짜", value=today, key="add_end")
        supplies = st.text_input("준비물")
        memo = st.text_area("메모")
        submit = st.form_submit_button("💜 일정 저장")

    if submit:
        if not title.strip():
            st.error("일정 이름을 입력해 주세요.")
        elif end < start:
            st.error("종료 날짜를 확인해 주세요.")
        else:
            new_event = {
                "id": max((e["id"] for e in events), default=0) + 1,
                "title": title.strip(),
                "category": category,
                "start": start.isoformat(),
                "end": end.isoformat(),
                "supplies": supplies.strip(),
                "memo": memo.strip()
            }

            updated = events + [new_event]

            if save_events(updated):
                st.session_state.events = updated
                st.success("일정을 추가했어요!")
                st.rerun()

# 일정 검색, 수정, 삭제
with tab3:
    st.subheader("📚 일정 관리")

    keyword = st.text_input("🔎 일정 검색")
    category_filter = st.selectbox(
        "종류 필터", ["전체"] + list(COLORS)
    )

    filtered = [
        e for e in sorted(events, key=lambda x: x["start"])
        if keyword.casefold() in (
            e["title"] + e.get("memo", "") + e.get("supplies", "")
        ).casefold()
        and (
            category_filter == "전체"
            or e["category"] == category_filter
        )
    ]

    if not filtered:
        st.info("검색 결과가 없습니다.")
    else:
        ids = [e["id"] for e in filtered]

        selected_id = st.selectbox(
            "관리할 일정 선택",
            ids,
            format_func=lambda i: next(
                f'{e["start"]} · {e["title"]}'
                for e in filtered if e["id"] == i
            )
        )

        selected = next(e for e in filtered if e["id"] == selected_id)

        st.write(f"**종류:** {selected['category']}")
        st.write(f"**기간:** {selected['start']} ~ {selected['end']}")
        st.write(f"**준비물:** {selected.get('supplies') or '없음'}")
        st.write(f"**메모:** {selected.get('memo') or '없음'}")

        with st.expander("일정 수정"):
            with st.form("edit_form"):
                new_title = st.text_input(
                    "일정 이름", value=selected["title"]
                )
                new_category = st.selectbox(
                    "종류",
                    list(COLORS),
                    index=list(COLORS).index(selected["category"])
                )
                new_start = st.date_input(
                    "시작 날짜",
                    value=date.fromisoformat(selected["start"])
                )
                new_end = st.date_input(
                    "종료 날짜",
                    value=date.fromisoformat(selected["end"])
                )
                new_supplies = st.text_input(
                    "준비물", value=selected.get("supplies", "")
                )
                new_memo = st.text_area(
                    "메모", value=selected.get("memo", "")
                )
                update = st.form_submit_button("변경 사항 저장")

            if update:
                if not new_title.strip():
                    st.error("일정 이름을 입력해 주세요.")
                elif new_end < new_start:
                    st.error("종료 날짜를 확인해 주세요.")
                else:
                    updated = []
                    for e in events:
                        if e["id"] == selected_id:
                            e = {
                                **e,
                                "title": new_title.strip(),
                                "category": new_category,
                                "start": new_start.isoformat(),
                                "end": new_end.isoformat(),
                                "supplies": new_supplies.strip(),
                                "memo": new_memo.strip()
                            }
                        updated.append(e)

                    if save_events(updated):
                        st.session_state.events = updated
                        st.success("수정했습니다.")
                        st.rerun()

        if st.button("🗑️ 일정 삭제"):
            updated = [e for e in events if e["id"] != selected_id]

            if save_events(updated):
                st.session_state.events = updated
                st.success("삭제했습니다.")
                st.rerun()

st.markdown(
    "<center style='color:#9298ae'>"
    "Made for school days 🌷</center>",
    unsafe_allow_html=True
)
