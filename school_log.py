
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="학교정보 알리미",
    page_icon="🎓",
    layout="wide"
)

# ---------- 디자인 CSS ----------
st.markdown("""
<style>
/* 전체 배경 및 기본 글꼴 */
.stApp {
    background: #f7f9fd;
    color: #172b4d;
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* 상단 배너 */
.hero {
    background: linear-gradient(115deg, #e2f0ff 0%, #d3eaff 55%, #bde5ff 100%);
    border: 1px solid #d3e8ff;
    border-radius: 24px;
    padding: 36px 40px;
    margin-bottom: 32px;
    box-shadow: 0 8px 24px rgba(49, 104, 170, 0.08);
}

.hero h1 {
    color: #16345c;
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin: 0 0 12px 0;
}

.hero p {
    color: #496587;
    font-size: 17px;
    margin: 0;
    line-height: 1.7;
}

/* 날짜 안내 */
div[data-testid="stAlert"] {
    border-radius: 14px;
    border: 1px solid #d8e8ff;
    background: #edf5ff;
    color: #244a78;
}

/* 섹션 제목 */
h2, h3 {
    color: #172b4d !important;
    letter-spacing: -0.5px;
}

.section-caption {
    color: #71819a;
    font-size: 16px;
    margin-top: -8px;
    margin-bottom: 20px;
}

/* 카드 */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff;
    border: 1px solid #e5ebf4;
    border-radius: 22px;
    box-shadow: 0 7px 22px rgba(31, 55, 90, 0.05);
    padding: 12px 10px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

/* 카드 안쪽 제목과 설명 */
.card-icon {
    font-size: 42px;
    margin-bottom: 8px;
}

.card-title {
    color: #1b3152;
    font-size: 23px;
    font-weight: 750;
    margin-bottom: 10px;
}

.card-description {
    color: #71819a;
    font-size: 15px;
    line-height: 1.8;
    min-height: 58px;
}

/* 버튼 기본 디자인 */
.stButton > button {
    border: none;
    border-radius: 14px;
    min-height: 48px;
    font-size: 15px;
    font-weight: 700;
    transition: all 0.2s ease;
}

/* 각 카드별 버튼 색상 */
div[data-testid="stHorizontalBlock"] > div:nth-child(1)
.stButton > button {
    background: #3478f6;
    color: white;
}

div[data-testid="stHorizontalBlock"] > div:nth-child(2)
.stButton > button {
    background: #fa6475;
    color: white;
}

div[data-testid="stHorizontalBlock"] > div:nth-child(3)
.stButton > button {
    background: #8064ed;
    color: white;
}

.stButton > button:hover {
    filter: brightness(0.95);
    box-shadow: 0 5px 14px rgba(50, 75, 120, 0.15);
    transform: translateY(-2px);
}

/* 학교생활 TIP */
.tip-box {
    background: linear-gradient(110deg, #effaf2, #f7fcf7);
    border: 1px solid #d4efdb;
    border-radius: 20px;
    padding: 22px 26px;
    margin-top: 8px;
    margin-bottom: 20px;
}

.tip-title {
    color: #21834b;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 8px;
}

.tip-text {
    color: #496b58;
    font-size: 15px;
    line-height: 1.9;
}

/* 하단 안내 */
.footer {
    text-align: center;
    color: #96a3b7;
    font-size: 13px;
    padding-top: 10px;
}

/* 모바일 화면 */
@media (max-width: 768px) {
    .hero {
        padding: 26px 22px;
    }

    .hero h1 {
        font-size: 29px;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- 상단 배너 ----------
st.markdown("""
<div class="hero">
    <h1>🎓 학교정보 알리미</h1>
    <p>학교생활에 필요한 정보를 한곳에서 확인하세요!</p>
</div>
""", unsafe_allow_html=True)

# ---------- 날짜 ----------
st.info(f"📅 오늘 날짜: {date.today():%Y년 %m월 %d일}")

# ---------- 서비스 바로가기 ----------
st.subheader("📌 서비스 바로가기")

st.markdown(
    '<p class="section-caption">원하는 메뉴를 선택하세요.</p>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    with st.container(border=True):
        st.markdown(
            '<div class="card-icon">🗓️</div>'
            '<div class="card-title">학교 일정 달력</div>'
            '<div class="card-description">'
            '시험, 수행평가, 학교 행사 일정을<br>한눈에 확인하세요.'
            '</div>',
            unsafe_allow_html=True
        )

        if st.button(
            "일정 확인하기  →",
            key="calendar",
            use_container_width=True
        ):
            st.switch_page("pages/학교일정달력.py")

with col2:
    with st.container(border=True):
        st.markdown(
            '<div class="card-icon">🩹</div>'
            '<div class="card-title">응급톡</div>'
            '<div class="card-description">'
            '응급상황 행동 요령과<br>아플 때 대처법을 확인하세요.'
            '</div>',
            unsafe_allow_html=True
        )

        if st.button(
            "응급 정보 확인  →",
            key="emergency",
            use_container_width=True
        ):
            st.switch_page("pages/응급톡.py")

with col3:
    with st.container(border=True):
        st.markdown(
            '<div class="card-icon">⏳</div>'
            '<div class="card-title">D-Day 알람</div>'
            '<div class="card-description">'
            '시험과 과제 제출일까지<br>남은 날짜를 확인하세요.'
            '</div>',
            unsafe_allow_html=True
        )

        if st.button(
            "D-Day 확인하기  →",
            key="dday",
            use_container_width=True
        ):
            st.switch_page("pages/D-Day 알람.py")

# ---------- 학교생활 TIP ----------
st.markdown("---")

st.markdown("""
<div class="tip-box">
    <div class="tip-title">💡 학교생활 TIP</div>
    <div class="tip-text">
        시험과 수행평가 일정을 미리 확인하고,<br>
        응급상황에서는 주변 선생님에게 도움을 요청하세요.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- 하단 안내 ----------
st.markdown("""
<div class="footer">
    ⓘ 학교 공식 일정은 학교 공지사항을 통해 확인하세요.
</div>
""", unsafe_allow_html=True)
