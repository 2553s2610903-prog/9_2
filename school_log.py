
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="학교정보 알리미",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f5f7fb;
}
.hero {
    background: linear-gradient(120deg, #173b67, #368b9b);
    padding: 35px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
}
.hero h1 {
    color: white;
    font-size: 36px;
}
.hero p {
    font-size: 17px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🎓 학교정보 알리미</h1>
    <p>학교생활에 필요한 정보를 한곳에서 확인하세요!</p>
</div>
""", unsafe_allow_html=True)

st.info(f"📅 오늘 날짜: {date.today():%Y년 %m월 %d일}")

st.subheader("📌 서비스 바로가기")
st.write("원하는 메뉴를 선택하세요.")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    with st.container(border=True):
        st.markdown("## 🗓️")
        st.markdown("### 학교 일정 달력")
        st.write("시험, 수행평가, 학교 행사 일정을 확인하세요.")
        if st.button("일정 확인하기 →", key="calendar",
                     use_container_width=True):
            st.switch_page("pages/학교일정달력.py")

with col2:
    with st.container(border=True):
        st.markdown("## 🩹")
        st.markdown("### 응급톡")
        st.write("응급상황 행동 요령과 아플 때 대처법을 확인하세요.")
        if st.button("응급 정보 확인 →", key="emergency",
                     use_container_width=True):
            st.switch_page("pages/응급톡.py")

with col3:
    with st.container(border=True):
        st.markdown("## ⏳")
        st.markdown("### D-Day 알람")
        st.write("시험과 과제 제출일까지 남은 날짜를 확인하세요.")
        if st.button("D-Day 확인하기 →", key="dday",
                     use_container_width=True):
            st.switch_page("pages/D-Day 알람.py")

st.divider()

st.subheader("💡 학교생활 TIP")
st.success(
    "시험과 수행평가 일정을 미리 확인하고, "
    "응급상황에서는 주변 선생님에게 도움을 요청하세요."
)

st.caption("학교 공식 일정은 학교 공지사항을 통해 확인하세요.")
