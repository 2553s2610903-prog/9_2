
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="학교정보 알리미",
    page_icon="🎓",
    layout="wide"
)

# ---------- CSS 디자인 ----------
st.markdown("""
<style>
.stApp {
    background: #f1f2f4;
    color: #222;
}

.block-container {
    max-width: 1500px;
    padding: 1.2rem 2rem 2rem;
}

/* 전체 메인 화면 */
.site {
    background: white;
    border-radius: 16px;
    padding: 0 28px 28px;
    box-shadow: 0 8px 35px rgba(0,0,0,0.06);
}

/* 상단 헤더 */
.brand {
    font-size: 28px;
    font-weight: 900;
    letter-spacing: -1.5px;
    color: #171717;
    padding: 15px 0;
}

.brand span {
    color: #568b75;
}

.top-date {
    color: #777;
    font-size: 14px;
    text-align: right;
    padding-top: 25px;
}

hr {
    border: none;
    border-top: 1px solid #e9e9e9;
    margin: 5px 0 20px;
}

/* 왼쪽 메뉴 */
.menu-label {
    font-size: 12px;
    color: #aaa;
    letter-spacing: 2px;
    margin: 12px 0 20px;
}

.menu-title {
    font-size: 15px;
    color: #777;
    padding: 13px 12px;
    border-radius: 7px;
    margin-bottom: 5px;
}

.menu-title.active {
    color: #222;
    background: #f1f5f2;
    font-weight: 800;
    border-left: 3px solid #568b75;
}

/* 메인 비주얼 배너 */
.main-banner {
    min-height: 370px;
    border-radius: 3px;
    overflow: hidden;
    position: relative;
    background:
        radial-gradient(ellipse at 85% 15%,
            rgba(255,255,255,.85) 0 2%,
            transparent 2.5%),
        radial-gradient(ellipse at 78% 20%,
            rgba(255,255,255,.4) 0 8%,
            transparent 8.5%),
        linear-gradient(120deg, #315c55 0%, #91b8a2 42%,
            #d6d7a0 70%, #e9dca9 100%);
    display: flex;
    align-items: center;
    padding: 38px;
    margin-bottom: 25px;
}

.banner-content {
    position: relative;
    z-index: 2;
    max-width: 520px;
}

.banner-kicker {
    font-size: 12px;
    letter-spacing: 4px;
    font-weight: 800;
    color: #f5f3df;
    margin-bottom: 22px;
}

.banner-title {
    color: white;
    font-size: clamp(30px, 4vw, 48px);
    font-weight: 800;
    line-height: 1.35;
    letter-spacing: -2px;
    text-shadow: 0 2px 12px rgba(0,0,0,.12);
}

.banner-desc {
    color: #fff;
    font-size: 15px;
    line-height: 1.9;
    margin-top: 16px;
}

.banner-symbol {
    position: absolute;
    right: 7%;
    bottom: 12%;
    font-size: clamp(80px, 13vw, 170px);
    opacity: .9;
    filter: drop-shadow(0 12px 14px rgba(0,0,0,.1));
}

/* 배너 하단 표시 */
.banner-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #888;
    font-size: 12px;
    margin-top: -12px;
    margin-bottom: 28px;
}

.banner-dots {
    letter-spacing: 7px;
    color: #568b75;
    font-size: 17px;
}

/* 기능 섹션 */
.section-heading {
    font-size: 22px;
    font-weight: 800;
    letter-spacing: -0.7px;
    color: #222;
    margin: 5px 0 5px;
}

.section-sub {
    color: #888;
    font-size: 13px;
    margin-bottom: 18px;
}

/* 기능 카드 */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border: 1px solid #e9e9e9;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,.025);
}

.card-icon {
    font-size: 30px;
    margin-bottom: 15px;
}

.card-name {
    font-size: 17px;
    font-weight: 800;
    color: #252525;
    margin-bottom: 8px;
}

.card-desc {
    font-size: 13px;
    line-height: 1.8;
    color: #858585;
    min-height: 48px;
}

/* 버튼 */
.stButton > button {
    border-radius: 4px;
    min-height: 42px;
    font-weight: 650;
    font-size: 13px;
    transition: all .2s ease;
}

.stButton > button:hover {
    border-color: #568b75;
    color: #568b75;
    transform: translateY(-1px);
}

/* 하단 공지 */
.notice {
    background: #f5f7f4;
    border-left: 3px solid #568b75;
    padding: 17px 20px;
    margin-top: 28px;
    color: #5e6b61;
    font-size: 13px;
    line-height: 1.9;
}

.footer {
    text-align: center;
    color: #aaa;
    font-size: 11px;
    padding: 25px 0 5px;
}

/* 모바일 대응 */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem;
    }

    .site {
        padding: 0 12px 20px;
    }

    .main-banner {
        min-height: 320px;
        padding: 24px;
    }

    .banner-symbol {
        right: 5%;
        bottom: 5%;
        opacity: .45;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- 상단 헤더 ----------
header_left, header_right = st.columns([3, 1])

with header_left:
    st.markdown(
        '<div class="brand">SCHOOL INFO <span>✳</span></div>',
        unsafe_allow_html=True
    )

with header_right:
    st.markdown(
        f'<div class="top-date">TODAY &nbsp; {date.today():%Y.%m.%d}</div>',
        unsafe_allow_html=True
    )

st.markdown("<hr>", unsafe_allow_html=True)

# ---------- 좌측 메뉴 + 메인 콘텐츠 ----------
sidebar, main = st.columns([1, 4], gap="large")

with sidebar:
    st.markdown(
        '<div class="menu-label">SCHOOL MENU</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="menu-title active">MAIN</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="menu-title">학교 일정</div>',
        unsafe_allow_html=True
    )
    if st.button("일정 페이지 →", key="side_calendar",
                 use_container_width=True):
        st.switch_page("pages/학교일정달력.py")

    st.markdown(
        '<div class="menu-title">응급톡</div>',
        unsafe_allow_html=True
    )
    if st.button("응급 정보 →", key="side_emergency",
                 use_container_width=True):
        st.switch_page("pages/응급톡.py")

    st.markdown(
        '<div class="menu-title">D-Day 알람</div>',
        unsafe_allow_html=True
    )
    if st.button("D-Day 페이지 →", key="side_dday",
                 use_container_width=True):
        st.switch_page("pages/D-Day 알람.py")

    st.markdown("---")
    st.caption("YOUR SCHOOL, YOUR LIFE")
    st.caption("학교생활을 더 편리하게")

with main:
    # ---------- 메인 배너 ----------
    st.markdown("""
    <div class="main-banner">
        <div class="banner-content">
            <div class="banner-kicker">WELCOME TO SCHOOL</div>
            <div class="banner-title">
                학교생활의 모든 것,<br>
                한곳에서 확인하세요.
            </div>
            <div class="banner-desc">
                학교 일정부터 응급상황 대처법까지<br>
                학교생활에 필요한 정보를 쉽고 빠르게.
            </div>
        </div>
        <div class="banner-symbol">🎓</div>
    </div>
    <div class="banner-bottom">
        <span>SCHOOL INFORMATION SERVICE</span>
        <span class="banner-dots">● ○ ○</span>
    </div>
    """, unsafe_allow_html=True)

    # ---------- 서비스 카드 ----------
    st.markdown(
        '<div class="section-heading">EXPLORE OUR SERVICES</div>'
        '<div class="section-sub">학교생활에 필요한 메뉴를 선택하세요.</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        with st.container(border=True):
            st.markdown("""
            <div class="card-icon">🗓️</div>
            <div class="card-name">학교 일정 달력</div>
            <div class="card-desc">
                시험, 수행평가, 학교 행사 등<br>
                주요 일정을 확인하세요.
            </div>
            """, unsafe_allow_html=True)

            if st.button("VIEW SCHEDULE  →", key="calendar",
                         use_container_width=True):
                st.switch_page("pages/학교일정달력.py")

    with col2:
        with st.container(border=True):
            st.markdown("""
            <div class="card-icon">🩹</div>
            <div class="card-name">응급톡</div>
            <div class="card-desc">
                응급상황 행동 요령과<br>
                아플 때 대처법을 확인하세요.
            </div>
            """, unsafe_allow_html=True)

            if st.button("VIEW GUIDE  →", key="emergency",
                         use_container_width=True):
                st.switch_page("pages/응급톡.py")

    with col3:
        with st.container(border=True):
            st.markdown("""
            <div class="card-icon">⏳</div>
            <div class="card-name">D-Day 알람</div>
            <div class="card-desc">
                시험과 과제 제출일까지<br>
                남은 날짜를 확인하세요.
            </div>
            """, unsafe_allow_html=True)

            if st.button("VIEW D-DAY  →", key="dday",
                         use_container_width=True):
                st.switch_page("pages/D-Day 알람.py")

# ---------- 하단 공지 ----------
st.markdown("""
<div class="notice">
    <b>💡 SCHOOL LIFE TIP</b><br>
    시험과 수행평가 일정을 미리 확인하세요.
    응급상황에서는 주변 선생님에게 도움을 요청하세요.
</div>
<div class="footer">
    SCHOOL INFO © &nbsp; | &nbsp; 학교 공식 일정은 학교 공지사항을 확인하세요.
</div>
""", unsafe_allow_html=True)
