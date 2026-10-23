
import json
import calendar
from datetime import date
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="학교 일정 달력", page_icon="📅", layout="wide")

DATA_FILE = Path(__file__).with_name("events.json")

COLORS = {
    "학교 행사": "#2563eb",
    "시험": "#dc2626",
    "수행평가": "#9333ea",
    "준비물": "#d97706",
    "휴일": "#16a34a",
    "기타": "#64748b",
}

def load_events():
    try:
        if DATA_FILE.exists():
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return [
                    e for e in data
                    if isinstance(e, dict)
                    and e.get("title")
                    and e.get("id") is not None
                    and e.get("category") in COLORS
                    and valid_dates(e)
                ]
    except (OSError, ValueError, TypeError):
        st.warning("일정 파일을 읽지 못했습니다.")
    return []

def valid_dates(event):
    try:
        start = date.fromisoformat(event["start"])
        end = date.fromisoformat(event["end"])
        return end >= start
    except (KeyError, ValueError, TypeError):
        return False

def save_events(events):
    try:
        temp = DATA_FILE.with_suffix(".tmp")
        temp.write_text(
            json.dumps(events, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        temp.replace(DATA_FILE)
        return True
    except OSError:
        st.error("일정 저장에 실패했습니다.")
        return False

def get_events_on(events, day):
    result = []
    for event in events:
        if (
            date.fromisoformat(event["start"])
            <= day
            <= date.fromisoformat(event["end"])
        ):
            result.append(event)
    return result

if "events" not in st.session_state:
    st.session_state.events = load_events()

events = st.session_state.events
today = date.today()

st.title("📅 우리 학교 일정 달력")
st.caption("시험, 수행평가, 학교 행사와 준비물을 한눈에 관리하세요.")

a, b, c = st.columns(3)
a.metric("전체 일정", len(events))
b.metric("오늘 일정", len(get_events_on(events, today)))
c.metric(
    "다가오는 일정",
    sum(1 for e in events if date.fromisoformat(e["end"]) >= today),
)

calendar_tab, add_tab, manage_tab = st.tabs(
    ["🗓️ 달력 보기", "➕ 일정 추가", "📝 일정 관리"]
)

with calendar_tab:
    selected_date = st.date_input("달력 날짜 선택", value=today)
    year, month = selected_date.year, selected_date.month
    st.subheader(f"{year}년 {month}월")

    weekdays = ["월", "화", "수", "목", "금", "토", "일"]
    cols = st.columns(7)
    for col, weekday in zip(cols, weekdays):
        col.markdown(f"**{weekday}요일**")

    for week in calendar.monthcalendar(year, month):
        cols = st.columns(7)
        for col, number in zip(cols, week):
            with col:
                if number == 0:
                    st.write(" ")
                    continue

                day = date(year, month, number)
                day_events = get_events_on(events, day)

                label = f"**{number}일**"
                if day == today:
                    label += " 📍"
                st.markdown(label)

                for event in day_events[:3]:
                    color = COLORS[event["category"]]
                    st.markdown(
                        f'<div style="border-left:3px solid {color};'
                        f'padding-left:5px;margin:3px 0;'
                        f'overflow-wrap:anywhere;font-size:13px;">'
                        f'{event["title"]}</div>',
                        unsafe_allow_html=True,
                    )

                if len(day_events) > 3:
                    st.caption(f"+{len(day_events) - 3}개 더")

    st.markdown("### 🔔 다가오는 일정")
    upcoming = sorted(
        [e for e in events if date.fromisoformat(e["end"]) >= today],
        key=lambda e: e["start"],
    )
    if not upcoming:
        st.info("등록된 일정이 없습니다.")
    for event in upcoming[:5]:
        st.write(
            f'📌 **{event["start"]}** · '
            f'{event["title"]} ({event["category"]})'
        )
        if event.get("supplies"):
            st.caption(f'준비물: {event["supplies"]}')

with add_tab:
    st.subheader("새 일정 등록")

    with st.form("add_form", clear_on_submit=True):
        title = st.text_input("일정 이름")
        category = st.selectbox("일정 종류", list(COLORS))
        start = st.date_input("시작 날짜", value=today, key="new_start")
        end = st.date_input("종료 날짜", value=today, key="new_end")
        supplies = st.text_input("준비물")
        memo = st.text_area("메모")
        submit = st.form_submit_button("일정 추가")

    if submit:
        if not title.strip():
            st.error("일정 이름을 입력해 주세요.")
        elif end < start:
            st.error("종료 날짜를 확인해 주세요.")
        else:
            new_event = {
                "id": max(
                    (e["id"] for e in events), default=0
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
                st.success("일정을 추가했습니다.")
                st.rerun()

with manage_tab:
    st.subheader("일정 검색 및 관리")
    keyword = st.text_input("일정 이름 또는 메모 검색")
    category_filter = st.selectbox(
        "종류 필터", ["전체"] + list(COLORS)
    )

    filtered = [
        e for e in sorted(events, key=lambda e: e["start"])
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
        selected_id = st.selectbox(
            "관리할 일정",
            [e["id"] for e in filtered],
            format_func=lambda eid: next(
                f'{e["start"]} · {e["title"]}'
                for e in filtered if e["id"] == eid
            ),
        )
        selected = next(e for e in filtered if e["id"] == selected_id)

        st.write(f'**종류:** {selected["category"]}')
        st.write(f'**날짜:** {selected["start"]} ~ {selected["end"]}')
        st.write(f'**준비물:** {selected.get("supplies") or "없음"}')
        st.write(f'**메모:** {selected.get("memo") or "없음"}')

        if st.button("선택한 일정 삭제", type="secondary"):
            updated = [e for e in events if e["id"] != selected_id]
            if save_events(updated):
                st.session_state.events = updated
                st.success("일정을 삭제했습니다.")
                st.rerun()

st.caption(
    "일정은 events.json 파일에 저장됩니다. "
    "Cloud 환경에서는 재배포 후 파일 유지가 보장되지 않습니다."
)
