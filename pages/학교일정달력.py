
import streamlit as st
import streamlit_calendar
from streamlit_calendar import calendar

st.set_page_config(page_title="학교 일정 달력", page_icon="📅")

st.title("📅 학교 일정 달력")
st.write("학교 행사, 시험, 수행평가 일정을 한눈에 확인하세요!")

# 일정 저장
if "events" not in st.session_state:
    st.session_state.events = []

# 일정 추가
st.subheader("➕ 일정 추가")

with st.form("schedule_form"):
    title = st.text_input("일정 이름")
    category = st.selectbox(
        "일정 종류",
        ["학교 행사", "시험", "수행평가", "휴일", "기타"]
    )
    start = st.date_input("시작 날짜")
    end = st.date_input("종료 날짜")
    memo = st.text_input("메모")

    submitted = st.form_submit_button("일정 추가")

if submitted:
    if not title.strip():
        st.warning("일정 이름을 입력하세요.")
    elif end < start:
        st.warning("종료 날짜를 확인하세요.")
    else:
        colors = {
            "학교 행사": "#3788d8",
            "시험": "#e74c3c",
            "수행평가": "#9b59b6",
            "휴일": "#27ae60",
            "기타": "#7f8c8d"
        }

        st.session_state.events.append({
            "title": f"[{category}] {title}",
            "start": start.isoformat(),
            "end": (end + __import__("datetime").timedelta(days=1)).isoformat(),
            "allDay": True,
            "backgroundColor": colors[category],
            "extendedProps": {"memo": memo}
        })

        st.success("일정을 추가했습니다!")

# 달력 표시
st.subheader("🗓️ 학교 일정")

calendar(
    events=st.session_state.events,
    options={
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,listMonth"
        },
        "initialView": "dayGridMonth",
        "locale": "ko",
        "height": 600
    },
    key="school_calendar"
)

# 등록된 일정 확인 및 삭제
st.subheader("📋 일정 관리")

for i, event in enumerate(st.session_state.events):
    col1, col2 = st.columns([4, 1])

    with col1:
        st.write(
            f"**{event['title']}** · {event['start']}"
        )

    with col2:
        if st.button("삭제", key=f"delete_{i}"):
            st.session_state.events.pop(i)
            st.rerun()
