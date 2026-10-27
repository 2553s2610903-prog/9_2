import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

st.set_page_config(
    page_title="SCHOOL LOG",
    page_icon="🎓",
    layout="wide"
)

# ---------- 한국 시간 기준 날짜 ----------
today = datetime.now(ZoneInfo("Asia/Seoul")).date()

# ---------- 디자인 CSS ----------
st.markdown("""
<style>

/* =========================================
   1. 전체 디자인
========================================= */

.stApp {
    background: #ffffff;
    color: #111111;
}

.block-container {
    max-width: 1600px;
    padding: 1.5rem 3rem 3rem;
}

/* Streamlit 기본 장식 최소화 */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* =========================================
   2. 상단 브랜드 헤더
========================================= */

.brand-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 0 25px;
    border-bottom: 1px solid #d9d9d9;
    margin-bottom: 35px;
}

.brand-name {
    font-size: 32px;
    font-weight: 900;
    letter-spacing: -2px;
    color: #111111;
    line-height: 1;
}

.brand-dot {
    color: #201bff;
}

.brand-right {
    font-size: 12px;
    font-weight: 600;
    color: #777777;
    letter-spacing: 1.5px;
    text-align: right;
}

/* =========================================
   3. 메인 타이틀
========================================= */

.eyebrow {
    font-size: 11px;
    color: #201bff;
    font-weight: 800;
    letter-spacing: 4px;
    margin-bottom: 25px;
}

.main-title {
    font-size: clamp(48px, 7.5vw, 108px);
    font-weight: 900;
    letter-spacing: -7px;
    line-height: 0.98;
    color: #111111;
    margin: 0;
    word-break: keep-all;
}

.main-title .blue {
    color: #201bff;
}

.main-description {
    font-size: 16px;
    line-height: 1.9;
    color: #555555;
    margin-top: 30px;
    max-width: 540px;
}

.hero-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #d9d9d9;
    padding: 35px 0 25px;
    margin-bottom: 60px;
}

.hero-label {
    font-size: 11px;
    color: #888888;
    letter-spacing: 2px;
    font-weight: 700;
}

.hero-date {
    font-size: 13px;
    color: #111111;
    font-weight: 700;
}

/* =========================================
   4. 서비스 섹션
========================================= */

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: end;
    margin-bottom: 28px;
}

.section-title {
    font-size: 31px;
    font-weight: 900;
    letter-spacing: -1.5px;
    color: #111111;
}

.section-caption {
    color: #777777;
    font-size: 13px;
    margin-top: 8px;
}

.section-number {
    color: #201bff;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
}

/* =========================================
   5. 서비스 카드
========================================= */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff;
    border: 1px solid #dedede;
    border-radius: 2px;
    box-shadow: none;
    padding: 18px 18px 20px;
    transition:
        border-color 0.2s ease,
        box-shadow 0.2s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #201bff;
    box-shadow: 0 8px 24px rgba(32, 27, 255, 0.06);
}

/* 카드 위쪽 번호 */
.card-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #eeeeee;
    padding-bottom: 17px;
    margin-bottom: 25px;
}

.card-number {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #201bff;
}

.card-category {
    font-size: 10px;
    color: #999999;
    letter-spacing: 1px;
}

/* 카드 아이콘 */
.card-icon {
    font-size: 43px;
    margin-bottom: 25px;
    line-height: 1.2;
}

/* 카드 제목 */
.card-title {
    font-size: 25px;
    font-weight: 900;
    letter-spacing: -1px;
    color: #111111;
    margin-bottom: 12px;
}

/* 카드 설명 */
.card-description {
    font-size: 14px;
    line-height: 1.9;
    color: #777777;
    min-height: 58px;
    margin-bottom: 20px;
}

/* =========================================
   6. 버튼 디자인
========================================= */

.stButton {
    margin-top: 18px;
}

.stButton > button {
    background: #ffffff;
    color: #111111;
    border: 1px solid #d7d7d7;
    border-radius: 2px;
    min-height: 49px;
    font-size: 13px;
    font-weight: 750;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #201bff;
    color: #ffffff;
    border-color: #201bff;
    box-shadow: none;
    transform: translateY(-2px);
}

.stButton > button:focus {
    box-shadow: none;
    outline: 1px solid #201bff;
}

/* =========================================
   7. 날짜 안내
========================================= */

div[data-testid="stAlert"] {
    background: #f7f7f7;
    border: 1px solid #e7e7e7;
    border-radius: 2px;
    color: #333333;
    margin-bottom: 35px;
}

/* =========================================
   8. 학교생활 TIP
========================================= */

.tip-section {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 35px;
    border-top: 1px solid #d9d9d9;
    border-bottom: 1px solid #d9d9d9;
    padding: 30px 0;
    margin-top: 60px;
}

.tip-label {
    color: #201bff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 3px;
}

.tip-title {
    color: #111111;
    font-size: 27px;
    font-weight: 900;
    letter-spacing: -1px;
    margin-top: 12px;
}

.tip-text {
    color: #555555;
    font-size: 14px;
    line-height: 2;
    padding-top: 5px;
}

/* =========================================
   9. 하단 푸터
========================================= */

.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 25px;
    color: #999999;
    font-size: 11px;
    letter-spacing: 1px;
}

.footer-brand {
    font-size: 15px;
    color: #111111;
    font-weight: 900;
    letter-spacing: -0.5px;
}

.footer-brand span {
    color: #201bff;
}

/* =========================================
   10. 반응형 모바일 디자인
========================================= */

@media (max-width: 768px) {

    .block-container {
        padding: 1rem 1rem 2rem;
    }

    .brand-name {
        font-size: 25px;
    }

    .brand-row {
        margin-bottom: 30px;
    }

    .main-title {
        font-size: clamp(43px, 10vw, 70px);
        letter-spacing: -3px;
        line-height: 1.05;
    }

    .main-description {
        font-size: 14px;
    }

    .hero-bottom {
        margin-bottom: 40px;
        padding: 25px 0 20px;
    }

    .section-title {
        font-size: 25px;
    }

    .card-title {
        font-size: 22px;
    }

    .tip-section {
        grid-template-columns: 1fr;
        gap: 15px;
        margin-top: 40px;
    }

    .tip-title {
        font-size: 23px;
    }

    .footer {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================
# 상단 브랜드 헤더
# =========================================

st.markdown(f"""
<div class="brand-row">
    <div class="brand-name">
        SCHOOL LOG<span class="brand-dot">.</span>
    </div>
    <div class="brand-right">
        SCHOOL INFORMATION SERVICE<br>
        TODAY &nbsp; {today:%Y.%m.%d}
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================
# 메인 타이틀
# =========================================

st.markdown("""
<div class="eyebrow">
    YOUR SCHOOL, YOUR LOG.
</div>

<div class="main-title">
    SCHOOL<br>
    LIFE<span class="blue">.</span><br>
    <span class="blue">LOG</span>
</div>

<div class="main-description">
    학교생활의 모든 것, 한곳에서 확인하세요.<br>
    학교 일정부터 응급상황 대처법까지<br>
    필요한 정보를 쉽고 빠르게 확인할 수 있습니다.
</div>

<div class="hero-bottom">
    <div class="hero-label">
        SCHOOL INFORMATION / 2026
    </div>
    <div class="hero-date">
        YOUR DAILY SCHOOL GUIDE ↘
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================
# 날짜 안내
# =========================================

st.info(f"📅 오늘 날짜: {today:%Y년 %m월 %d일}")


# =========================================
# 서비스 바로가기
# =========================================

st.markdown("""
<div class="section-header">
    <div>
        <div class="section-title">Explore Our Services.</div>
        <div class="section-caption">
            학교생활에 필요한 메뉴를 선택하세요.
        </div>
    </div>
    <div class="section-number">
        INDEX  /  03
    </div>
</div>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3, gap="medium")


# =========================================
# 01. 학교 일정 달력
# =========================================

with col1:
    with st.container(border=True):

        st.markdown("""
        <div class="card-top">
            <span class="card-number">01 / SCHEDULE</span>
            <span class="card-category">CALENDAR</span>
        </div>

        <div class="card-icon">🗓️</div>

        <div class="card-title">
            학교 일정 달력
        </div>

        <div class="card-description">
            시험, 수행평가, 학교 행사 일정을<br>
            한눈에 확인하세요.
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "일정 확인하기  ↗",
            key="calendar",
            use_container_width=True
        ):
            st.switch_page("pages/학교일정달력.py")


# =========================================
# 02. 응급톡
# =========================================

with col2:
    with st.container(border=True):

        st.markdown("""
        <div class="card-top">
            <span class="card-number">02 / SAFETY</span>
            <span class="card-category">EMERGENCY</span>
        </div>

        <div class="card-icon">🩹</div>

        <div class="card-title">
            응급톡
        </div>

        <div class="card-description">
            응급상황 행동 요령과<br>
            아플 때 대처법을 확인하세요.
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "응급 정보 확인  ↗",
            key="emergency",
            use_container_width=True
        ):
            st.switch_page("pages/응급톡.py")


# =========================================
# 03. D-Day 알람
# =========================================

with col3:
    with st.container(border=True):

        st.markdown("""
        <div class="card-top">
            <span class="card-number">03 / D-DAY</span>
            <span class="card-category">COUNTDOWN</span>
        </div>

        <div class="card-icon">⏳</div>

        <div class="card-title">
            D-Day 알람
        </div>

        <div class="card-description">
            시험과 과제 제출일까지<br>
            남은 날짜를 확인하세요.
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "D-Day 확인하기  ↗",
            key="dday",
            use_container_width=True
        ):
            st.switch_page("pages/D-Day 알람.py")


# =========================================
# 학교생활 TIP
# =========================================

st.markdown("""
<div class="tip-section">

    <div>
        <div class="tip-label">
            SCHOOL LIFE / TIP
        </div>

        <div class="tip-title">
            Stay prepared.
        </div>
    </div>

    <div class="tip-text">
        시험과 수행평가 일정을 미리 확인하고,
        중요한 학교생활 정보를 놓치지 마세요.<br>
        응급상황에서는 혼자 해결하려 하지 말고
        주변 선생님에게 도움을 요청하세요.
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================
# 하단 안내
# =========================================

st.markdown("""
<div class="footer">
    <div class="footer-brand">
        SCHOOL LOG<span>.</span>
    </div>

    <div>
        학교 공식 일정은 학교 공지사항을 통해 확인하세요.
    </div>
</div>
""", unsafe_allow_html=True)
