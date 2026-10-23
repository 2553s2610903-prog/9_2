
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="학교정보 알리미",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 학교정보 알리미")
st.write("학교생활에 필요한 정보를 한곳에서 확인하세요.")

st.subheader("메뉴 선택")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🗓️ 학교 일정 달력")
    st.write("시험, 수행평가, 학교 행사 일정")
    if st.button("일정 확인", use_container_width=True):
        st.switch_page("pages/학교_일정_달력.py")

with col2:
    st.markdown("### 🩹 응급톡")
    st.write("응급상황 대처법과 건강 안전 안내")
    if st.button("응급톡 열기", use_container_width=True):
        st.switch_page("pages/응급톡.py")

with col3:
    st.markdown("### ⏳ D-Day 알람")
    st.write("시험과 중요한 일정까지 남은 날짜")
    if st.button("D-Day 확인", use_container_width=True):
        st.switch_page("pages/D-Day_알람.py")

st.divider()
st.info(f"오늘 날짜: {date.today():%Y년 %m월 %d일}")
st.caption(
    "학교 공식 일정은 학교 공지사항에서 확인하세요."
)
