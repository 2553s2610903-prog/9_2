import streamlit as st
import importlib.util

# 모듈을 동적으로 로드하기 위한 함수 (파일명에 공백이 있어도 로드 가능)
def load_page(filename):
    spec = importlib.util.spec_from_file_location("module.name", filename)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo

# 페이지 기본 설정
st.set_page_config(
    page_title="9반 2조 학교 통합 포털",
    page_icon="🏫",
    layout="wide"
)

# 사이드바 메뉴
st.sidebar.title("📌 [9반 2조] 메뉴")
menu = st.sidebar.radio(
    "이동할 페이지를 선택하세요:",
    ["🏠 메인 페이지 (school_log)", "📅 학교 일정 달력", "🏥 응급톡", "💌 익명 칭찬 게시판"]
)

# 1. 메인 페이지
if menu == "🏠 메인 페이지 (school_log)":
    st.title("🏫 9반 2조 학교 통합 포털에 오신 것을 환영합니다!")
    st.markdown("---")
    
    st.subheader("💡 이 사이트는 어떤 사이트인가요?")
    st.write("우리 학교 학생들의 편리하고 안전한 학교 생활을 돕기 위해 9반 2조가 만든 통합 포털 사이트입니다.")
    
    st.markdown("---")
    st.subheader("📋 주요 기능 안내")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("### 📅 학교 일정 달력")
        st.write("학교 주요 행사, 시험 일정, 수행평가 제출일을 한눈에 확인할 수 있는 달력입니다.")
        
    with col2:
        st.error("### 🏥 응급톡")
        st.write("갑자기 아프거나 응급 상황이 발생했을 때 바로 확인해야 하는 대처 요령과 주의사항을 제공합니다.")
        
    with col3:
        st.success("### 💌 익명 칭찬 게시판")
        st.write("평소 친구에게 전하지 못했던 고마움과 따뜻한 칭찬의 한마디를 익명으로 나누는 공간입니다.")

    st.markdown("---")
    st.caption("제작: 9반 2조 (정영인, 국아린, 최은진, 한수민)")

# 2. 학교 일정 달력 페이지 연결
elif menu == "📅 학교 일정 달력":
    try:
        page = load_page("학교 일정 달력.py")
        page.run()
    except FileNotFoundError:
        st.warning("'학교 일정 달력.py' 파일을 찾을 수 없습니다.")

# 3. 응급톡 페이지 연결
elif menu == "🏥 응급톡":
    try:
        page = load_page("응급톡.py")
        page.run()
    except FileNotFoundError:
        st.warning("'응급톡.py' 파일을 찾을 수 없습니다.")

# 4. 칭찬 게시판 페이지 연결
elif menu == "💌 익명 칭찬 게시판":
    try:
        page = load_page("칭찬 게시판.py")
        page.run()
    except FileNotFoundError:
        st.warning("'칭찬 게시판.py' 파일을 찾을 수 없습니다.")
