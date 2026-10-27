
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="나의 첫 번째 서비스",
    page_icon="🚀",
    layout="centered"
)

# 제목
st.title("🚀 나의 첫 번째 웹 서비스")
st.write("Streamlit으로 만든 간단한 웹 앱입니다.")

# 사용자 입력
name = st.text_input("이름을 입력하세요.")

# 버튼
if st.button("시작하기"):
    if name:
        st.success(f"{name}님, 환영합니다!")
    else:
        st.warning("이름을 먼저 입력해 주세요.")

# 선택 메뉴
menu = st.selectbox(
    "원하는 메뉴를 선택하세요.",
    ["홈", "서비스 소개", "문의하기"]
)

st.write(f"현재 선택한 메뉴: {menu}")

