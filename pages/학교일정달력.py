
import json
import calendar
import html
from datetime import date
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="우리 학교 플래너",
    page_icon="🌷",
    layout="wide",
)

DATA_FILE = Path(__file__).with_name("events.json")

CATEGORIES = {
    "학교 행사": "#6488EA",
    "시험": "#F07178",
    "수행평가": "#A58AE8",
    "준비물": "#E7A64B",
    "휴일": "#5CB99A",
    "기타": "#8793A5",
}
WEEKDAYS = ["월", "화", "수", "목", "금", "토", "일"]


def load_events():
    """저장된 일정을 읽고 잘못된 데이터는 건너뜁니다."""
    if not DATA_FILE.exists():
        return []

    try:
        raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        if not isinstance(raw, list):
            return []

        result = []
        for item in raw:
            if not isinstance(item, dict):
                continue

            try:
                start = date.fromisoformat(item["start"])
                end = date.fromisoformat(item["end"])
                title = str(item.get("title", "")).strip()
                category = item.get("category", "기타")

                if not title or end < start or category not in CATEGORIES:
                    continue

                result.append({
                    "id": int(item["id"]),
                    "title": title,
                    "category": category,
                    "start": start.isoformat(),
                    "end": end.isoformat(),
                    "supplies": str(item.get("supplies", "")),
                    "memo": str(item.get("memo", "")),
                })
            except (KeyError, TypeError, ValueError):
                continue

        return result

    except (OSError, json.JSONDecodeError):
        st.warning("일정 파일을 읽지 못했어요. 빈 달력으로 시작합니다.")
        return []


def save_events(events):
    """임시 파일에 먼저 기록한 뒤 저장 파일로 교체합니다."""
    try:
        temp = DATA_FILE.with_suffix(".tmp")
        temp.write_text(
            json.dumps(events, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        temp.replace(DATA_FILE)
        return True
    except OSError:
        st.error("저장에 실패했어요. 파일 권한을 확인해 주세요.")
        return False


def day_events(events, current_day):
    """해당 날짜에 진행 중인 일정을 반환합니다."""
    found = []
    for event in events:
        try:
            if (
                date.fromisoformat(event["start"])
                <= current_day
                <= date.fromisoformat(event["end"])
            ):
                found.append(event)
        except (KeyError, TypeError, ValueError):
            continue
    return found


def safe_text(value):
    """HTML에 들어가는 사용자 입력을 안전하게 표시합니다."""
    return html.escape(str(value))


if "events" not in st.session_state:
    st.session_state.events = load_events()

events = st.session_state.events
today = date.today()

# ---------- 디자인 ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        180deg, #f7f8ff 0%, #fbf9ff 48%, #fffaf7 100%
    );
}
.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
h1, h2, h3 {
    color: #303957;
    letter-spacing: -0.03em;
}
.hero {
    background: linear-gradient(
        120deg, #e7ecff, #f4eaff 58%, #fff0e9
    );
    border: 1px solid #e5e7fb;
    border-radius: 25px;
    padding: 26px 30px;
    margin-bottom: 20px;
}
.hero-kicker {
    color: #747da4;
    font-size: .85rem;
    font-weight: 700;
    letter-spacing: .08em;
}
.hero-title {
    color: #303957;
    font-size: 2rem;
    font-weight: 800;
    margin: 5px 0;
}
.hero-desc {
    color: #68708e;
    font-size: 1rem;
}
div[data-testid="stMetric"] {
    background: rgba(255,255,255,.82);
    border: 1px solid #ececf7;
    border-radius: 18px;
    padding: 15px 18px;
    box-shadow: 0 4px 18px rgba(68,74,120,.04);
}
div[data-testid="stTabs"] button {
    border-radius: 12px;
    font-weight: 650;
}
.day-number {
    font-size: 1rem;
    font-weight: 800;
    color: #3e4664;
    margin-bottom: 5px;
}
.today-number {
    display: inline-block;
    background: #687fe5;
    color: white;
    border-radius: 999px;
    padding: 3px 8px;
}
.event-pill {
    border-radius: 7px;
    padding: 4px 6px;
    margin: 4px 0;
    color: white;
    font-size: .76rem;
    line-height: 1.25;
    overflow-wrap: anywhere;
}
.event-card {
    background: white;
    border: 1px solid #ececf7;
    border-radius: 15px;
    padding: 13px 15px;
    margin: 8px 0;
}
.small-muted {
    color: #858ba4;
    font-size: .82rem;
}
div.stButton > button {
    border-radius: 11px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="hero-kicker">MY SCHOOL PLANNER · DAILY ORGANIZER</div>
  <div class="hero-title">🌷 우리 학교 일정 달력</div>
  <div class="hero-desc">
    시험부터 학교 행사까지, 중요한 날을 예쁘게 모아 보세요.
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- 일정 요약 ----------
today_list = day_events(events, today)
upcoming = []

for event in events:
    try:
        if date.fromisoformat(event["end"]) >= today:
            upcoming.append(event)
    except (KeyError, ValueError, TypeError):
        continue

upcoming.sort(key=lambda e: (e["start"], e["title"]))

m1, m2, m3 = st.columns(3)
m1.metric("🗂️ 등록한 일정", f"{len(events)}개")
m2.metric("☀️ 오늘의 일정", f"{len(today_list)}개")
m3.metric("🔔 다가오는 일정", f"{len(upcoming)}개")

calendar_tab, add_tab, manage_tab = st.tabs([
    "🗓️ 예쁜 달력",
    "✏️ 일정 추가",
    "📚 일정 정리",
])

# ---------- 달력 보기 ----------
with calendar_tab:
    left, right = st.columns([1, 1])

    with left:
        chosen = st.date_input(
            "달력에서 보고 싶은 달",
            value=today,
            key="month_choice",
        )

    with right:
        st.markdown(
            "<div style='height:27px'></div>",
            unsafe_allow_html=True,
        )
        legend = "　".join(
            f'<span style="color:{color};font-weight:800">●</span> '
            f'{category}'
            for category, color in CATEGORIES.items()
        )
        st.markdown(legend, unsafe_allow_html=True)

    year, month = chosen.year, chosen.month

    st.markdown(
        f"<h2 style='text-align:center;margin:10px 0 18px'>"
        f"{year}년 {month}월</h2>",
        unsafe_allow_html=True,
    )

    # 요일 머리글
    head_cols = st.columns(7, gap="small")

    for i, weekday in enumerate(WEEKDAYS):
        color = (
            "#e27682" if i == 6
            else "#6f8de8" if i == 5
            else "#737b99"
        )
        head_cols[i].markdown(
            f'<div style="text-align:center;color:{color};'
            f'font-weight:800;padding:7px">{weekday}</div>',
            unsafe_allow_html=True,
        )

    # 월간 달력
    for week in calendar.monthcalendar(year, month):
        cols = st.columns(7, gap="small")

        for col, number in zip(cols, week):
            with col:
                # 해당 달에 속하지 않는 칸
                if number == 0:
                    st.markdown(
                        '<div style="height:105px;border-radius:14px;'
                        'background:rgba(255,255,255,.28)"></div>',
                        unsafe_allow_html=True,
                    )
                    continue

                current = date(year, month, number)
                items = day_events(events, current)

                if current == today:
                    day_label = (
                        f'<span class="today-number">{number}</span>'
                    )
                else:
                    day_label = f"<span>{number}</span>"

                pieces = [
                    f'<div class="day-number">{day_label}</div>'
                ]

                # 날짜별 일정이 있을 때만 표시
                for event in items[:3]:
                    color = CATEGORIES.get(
                        event["category"], CATEGORIES["기타"]
                    )
                    pieces.append(
                        f'<div class="event-pill" style="background:{color}">'
                        f'{safe_text(event["title"])}</div>'
                    )

                if len(items) > 3:
                    pieces.append(
                        f'<div class="small-muted">'
                        f'+{len(items) - 3}개 더</div>'
                    )

                # 일정이 없으면 날짜 숫자 외에는 아무것도 표시하지 않음
                st.markdown(
                    '<div style="min-height:105px;'
                    'background:rgba(255,255,255,.9);'
                    'border:1px solid #e9eaf5;border-radius:14px;'
                    'padding:8px 7px;'
                    'box-shadow:0 3px 12px rgba(60,65,110,.035);">'
                    + "".join(pieces)
                    + "</div>",
                    unsafe_allow_html=True,
                )

    st.markdown("### ✨ 다가오는 일정")

    if not upcoming:
        st.info(
            "아직 등록한 일정이 없어요. "
            "‘일정 추가’에서 첫 일정을 만들어 보세요!"
        )
    else:
        for event in upcoming[:5]:
            color = CATEGORIES.get(
                event["category"], CATEGORIES["기타"]
            )
            supplies_text = (
                "준비물: " + safe_text(event["supplies"])
                if event.get("supplies")
                else ""
            )

            st.markdown(
                f'<div class="event-card" '
                f'style="border-left:5px solid {color}">'
                f'<div class="small-muted">'
                f'{safe_text(event["start"])} · '
                f'{safe_text(event["category"])}</div>'
                f'<div style="font-weight:750;color:#3d4564;'
                f'font-size:1.03rem">'
                f'{safe_text(event["title"])}</div>'
                f'<div class="small-muted">{supplies_text}</div>'
                f"</div>",
                unsafe_allow_html=True,
            )

# ---------- 일정 추가 ----------
with add_tab:
    st.subheader("✏️ 새로운 일정 만들기")
    st.write("중요한 날짜와 준비할 내용을 함께 기록해 보세요.")

    with st.form("add_form", clear_on_submit=True):
        title = st.text_input(
            "일정 이름 *",
            placeholder="예: 영어 단어 시험",
        )
        category = st.selectbox(
            "일정 종류",
            list(CATEGORIES.keys()),
        )
        start = st.date_input(
            "시작 날짜",
            value=today,
            key="start_new",
        )
        end = st.date_input(
            "종료 날짜",
            value=today,
            key="end_new",
        )
        supplies = st.text_input(
            "준비물",
            placeholder="예: 영어 교과서, 필기구",
        )
        memo = st.text_area(
            "메모",
            placeholder="시험 범위, 장소, 할 일 등",
        )
        submitted = st.form_submit_button(
            "💜 달력에 저장",
            use_container_width=True,
        )

    if submitted:
        if not title.strip():
            st.error("일정 이름을 입력해 주세요.")
        elif end < start:
            st.error("종료 날짜는 시작 날짜보다 빠를 수 없어요.")
        else:
            new_event = {
                "id": max(
                    (e["id"] for e in events),
                    default=0,
                ) + 1,
                "title": title.strip(),
                "category": category,
                "start": start.isoformat(),
                "end": end.isoformat(),
                "supplies": supplies.strip(),
                "memo": memo.strip(),
            }

            updated = events + [new_event]

            if save_events(updated):
                st.session_state.events = updated
                st.success("일정을 달력에 추가했어요!")
                st.rerun()

# ---------- 일정 검색·수정·삭제 ----------
with manage_tab:
    st.subheader("📚 내 일정 모아보기")

    keyword = st.text_input("🔎 일정명, 메모, 준비물 검색")
    chosen_category = st.selectbox(
        "종류별로 보기",
        ["전체"] + list(CATEGORIES.keys()),
    )

    filtered = []

    for event in sorted(
        events,
        key=lambda e: (e["start"], e["title"]),
    ):
        searchable = " ".join([
            event["title"],
            event.get("memo", ""),
            event.get("supplies", ""),
        ]).casefold()

        if keyword.casefold() not in searchable:
            continue

        if (
            chosen_category != "전체"
            and event["category"] != chosen_category
        ):
            continue

        filtered.append(event)

    if not filtered:
        st.info("조건에 맞는 일정이 없어요.")
    else:
        labels = {
            str(e["id"]): f'{e["start"]} · {e["title"]}'
            for e in filtered
        }

        selected_id = st.selectbox(
            "상세 내용을 볼 일정",
            list(labels.keys()),
            format_func=lambda key: labels[key],
        )

        selected = next(
            e for e in filtered if str(e["id"]) == selected_id
        )

        with st.container(border=True):
            st.markdown(f"### {selected['title']}")
            st.write(f"**종류:** {selected['category']}")
            st.write(
                f"**기간:** {selected['start']} ~ {selected['end']}"
            )
            st.write(
                f"**준비물:** {selected.get('supplies') or '없음'}"
            )
            st.write(
                f"**메모:** {selected.get('memo') or '없음'}"
            )

        with st.expander("일정 수정"):
            with st.form("edit_form"):
                edit_title = st.text_input(
                    "일정 이름",
                    value=selected["title"],
                )
                edit_category = st.selectbox(
                    "종류",
                    list(CATEGORIES.keys()),
                    index=list(CATEGORIES.keys()).index(
                        selected["category"]
                    ),
                )
                edit_start = st.date_input(
                    "시작 날짜",
                    value=date.fromisoformat(selected["start"]),
                )
                edit_end = st.date_input(
                    "종료 날짜",
                    value=date.fromisoformat(selected["end"]),
                )
                edit_supplies = st.text_input(
                    "준비물",
                    value=selected.get("supplies", ""),
                )
                edit_memo = st.text_area(
                    "메모",
                    value=selected.get("memo", ""),
                )

                update = st.form_submit_button("변경 내용 저장")

            if update:
                if not edit_title.strip():
                    st.error("일정 이름을 입력해 주세요.")
                elif edit_end < edit_start:
                    st.error("종료 날짜를 확인해 주세요.")
                else:
                    updated = []

                    for event in events:
                        if event["id"] == selected["id"]:
                            event = {
                                **event,
                                "title": edit_title.strip(),
                                "category": edit_category,
                                "start": edit_start.isoformat(),
                                "end": edit_end.isoformat(),
                                "supplies": edit_supplies.strip(),
                                "memo": edit_memo.strip(),
                            }
                        updated.append(event)

                    if save_events(updated):
                        st.session_state.events = updated
                        st.success("일정을 수정했어요.")
                        st.rerun()

        if st.button("🗑️ 선택한 일정 삭제", type="secondary"):
            updated = [
                e for e in events
                if e["id"] != selected["id"]
            ]

            if save_events(updated):
                st.session_state.events = updated
                st.success("일정을 삭제했어요.")
                st.rerun()

st.markdown(
    '<div style="text-align:center;color:#9a9fb4;'
    'padding:22px 0 0">'
    'Made for school days · 나의 학교 플래너 🌷</div>',
    unsafe_allow_html=True,
)
