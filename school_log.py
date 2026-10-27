```python
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path
import html

st.set_page_config(
    page_title="SCHOOL LOG",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

today = datetime.now(ZoneInfo("Asia/Seoul")).date()
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
weekday = weekdays[today.weekday()]


# ---------- 페이지 이동 ----------
def go_to_page(filename):
    page_path = Path(__file__).parent / "pages" / filename

    if page_path.is_file():
        st.switch_page(str(page_path))
    else:
        st.error(
            f"페이지 파일을 찾을 수 없습니다: pages/{filename}\n\n"
            "GitHub 저장소에서 파일명과 경로를 확인해 주세요."
        )


# ---------- SVG 아이콘 ----------
def icon_svg(name):
    icons = {
        "calendar": """
            <rect x="3" y="5" width="18" height="16" rx="1"/>
            <path d="M16 3v4M8 3v4M3 10h18"/>
            <path d="M7 14h3M7 17h3M14 14h3M14 17h3"/>
        """,
        "medical": """
            <path d="M12 22s8-4 8-11V5l-8-3-8 3v6c0 7 8 11 8 11z"/>
            <path d="M12 8v8M8 12h8"/>
        """,
        "clock": """
            <circle cx="12" cy="12" r="9"/>
            <path d="M12 7v5l3 2"/>
        """
    }

    body = icons.get(name, icons["calendar"])

    return f"""
    <svg xmlns="http://www.w3.org/2000/svg"
         width="38" height="38" viewBox="0 0 24 24"
         fill="none" stroke="currentColor" stroke-width="1.5"
         stroke-linecap="square" stroke-linejoin="miter"
         aria-hidden="true">
        {body}
    </svg>
    """


# ---------- 디자인 CSS ----------
st.markdown("""
<style>
:root {
    --blue: #2925ff;
    --black: #111111;
    --gray: #777777;
    --line: #dedede;
    --soft: #f6f6f8;
}

.stApp {
    background: #ffffff;
    color: var(--black);
}

.block-container {
    max-width: 1600px;
    padding: 1.5rem 3rem 3rem;
}

#MainMenu, footer {
    visibility: hidden;
}

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

/* 상단 브랜드 */
.brand-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    padding: 12px 0 24px;
    border-bottom: 1px solid var(--line);
    margin-bottom: 42px;
}

.brand-name {
    font-size: 30px;
    font-weight: 900;
    letter-spacing: -1.8px;
    color: var(--black);
}

.brand-dot,
.footer-brand span {
    color: var(--blue);
}

.brand-meta {
    text-align: right;
    font-size: 10px;
    line-height: 1.8;
    color: var(--gray);
    letter-spacing: 1.5px;
}

/* 메인 타이틀 */
.eyebrow {
    color: var(--blue);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 4px;
    margin-bottom: 24px;
}

.main-title {
    color: var(--black);
    font-size: clamp(52px, 8vw, 112px);
    font-weight: 900;
    letter-spacing: -0.075em;
    line-height: 0.98;
    overflow-wrap: anywhere;
}

.main-title .blue {
    color: var(--blue);
}

.main-description {
    color: #555555;
    font-size: 15px;
    line-height: 2;
    margin-top: 28px;
    margin-bottom: 32px;
}

.hero-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    padding: 20px 0;
    margin-bottom: 35px;
}

.hero-label {
    color: #888888;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero-right {
    color: var(--black);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-align: right;
}

/* 각진 날짜 패널 */
.date-panel {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    background: var(--soft);
    border: 1px solid var(--line);
    border-left: 4px solid var(--blue);
    border-radius: 0;
    padding: 20px 24px;
    margin-bottom: 48px;
}

.date-label {
    color: #777777;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 7px;
}

.date-value {
    color: var(--black);
    font-size: clamp(20px, 3vw, 27px);
    font-weight: 850;
    letter-spacing: -1px;
}

.date-weekday {
    color: var(--blue);
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
    text-align: right;
}

/* 서비스 제목 */
.section-header {
    display: flex;
    justify-content: space-between;
    align-items: end;
    gap: 20px;
    margin-bottom: 25px;
}

.section-title {
    color: var(--black);
    font-size: clamp(24px, 3vw, 32px);
    font-weight: 900;
    letter-spacing: -1.5px;
}

.section-caption {
    color: var(--gray);
    font-size: 13px;
    margin-top: 7px;
}

.section-number {
    color: var(--blue);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    white-space: nowrap;
}

/* 카드 내용 */
.service-card {
    min-height: 235px;
}

.card-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
    padding-bottom: 15px;
    margin-bottom: 24px;
    border-bottom: 1px solid #eeeeee;
}

.card-number {
    color: var(--blue);
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.2px;
}

.card-category {
    color: #999999;
    font-size: 9px;
    letter-spacing: 1px;
}

.card-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 58px;
    height: 58px;
    color: var(--blue);
    background: #f4f4ff;
    border: 1px solid #e5e4ff;
    margin-bottom: 23px;
}

.card-title {
    color: var(--black);
    font-size: 23px;
    font-weight: 900;
    letter-spacing: -1px;
    margin-bottom: 10px;
}

.card-description {
    color: #777777;
    font-size: 13px;
    line-height: 1.9;
    min-height: 50px;
}

/* 카드 테두리 */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff;
    border: 1px solid var(--line);
    border-radius: 0;
    box-shadow: none;
    padding: 14px;
    transition: border-color 0.2s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #aaa8ff;
}

/* 버튼 */
.stButton {
    margin-top: 15px;
}

.stButton > button {
    width: 100%;
    min-height: 48px;
    color: var(--black);
    background: #ffffff;
    border: 1px solid #d7d7d7;
    border-radius: 0;
    font-size: 13px;
    font-weight: 750;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    color: #ffffff;
    background: var(--blue);
    border-color: var(--blue);
    transform: translateY(-1px);
    box-shadow: none;
}

.stButton > button:focus-visible {
    outline: 2px solid var(--blue);
    outline-offset: 2px;
}

/* 학교생활 팁 */
.tip-section {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 30px;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    padding: 28px 0;
    margin-top: 55px;
}

.tip-label {
    color: var(--blue);
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
}

.tip-title {
    color: var(--black);
    font-size: 26px;
    font-weight: 900;
    letter-spacing: -1px;
    margin-top: 10px;
}

.tip-text {
    color: #555555;
    font-size: 13px;
    line-height: 2;
}

/* 하단 */
.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    padding-top: 24px;
    color: #999999;
    font-size: 10px;
}

.footer-brand {
    color: var(--black);
    font-size: 15px;
    font-weight: 900;
    letter-spacing: -0.5px;
}

@media (max-width: 768px) {
    .block-container {
        padding: 1rem 1rem 2rem;
    }

    .brand-name {
        font-size: 24px;
    }

    .brand-meta {
        font-size: 9px;
    }

    .brand-row {
        margin-bottom: 32px;
    }

    .main-title {
        font-size: clamp(46px, 12vw, 72px);
        letter-spacing: -0.06em;
        line-height: 1.02;
    }

    .main-description {
        font-size: 13px;
    }

    .hero-bottom {
        align-items: flex-start;
        flex-direction: column;
    }

    .hero-right {
        text-align: left;
    }

    .date-panel {
        padding: 17px;
    }

    .date-value {
        font-size: 20px;
    }

    .section-title {
        font-size: 24px;
    }

    .section-number {
        font-size: 9px;
    }

    .card-title {
        font-size: 21px;
    }

    .tip-section {
        grid-template-columns: 1fr;
        gap: 16px;
        margin-top: 40px;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------- 상단 브랜드 ----------
st.markdown(f"""
<div class="brand-row">
    <div class="brand-name">SCHOOL LOG<span class="brand-dot">.</span></div>
    <div class="brand-meta">
        SCHOOL INFORMATION SERVICE<br>
        EST. 2026 / {today:%Y.%m.%d}
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- 메인 타이틀 ----------
st.markdown("""
<div class="eyebrow">YOUR SCHOOL, YOUR LOG.</div>

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
    <div class="hero-label">SCHOOL INFORMATION / 2026</div>
    <div class="hero-right">YOUR DAILY SCHOOL GUIDE ↘</div>
</div>
""", unsafe_allow_html=True)


# ---------- 날짜 패널 ----------
st.markdown(f"""
<div class="date-panel">
    <div>
        <div class="date-label">TODAY / 오늘의 날짜</div>
        <div class="date-value">{today:%Y년 %m월 %d일}</div>
    </div>
    <div class="date-weekday">
        {html.escape(weekday)}<br>
        <span style="color:#999999;font-size:10px;">
            {today:%Y . %m . %d}
        </span>
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- 서비스 섹션 ----------
st.markdown("""
<div class="section-header">
    <div>
        <div class="section-title">Explore Our Services.</div>
        <div class="section-caption">학교생활에 필요한 메뉴를 선택하세요.</div>
    </div>
    <div class="section-number">INDEX / 03</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")


# ---------- 학교 일정 달력 ----------
with col1:
    with st.container(border=True):
        st.markdown(f"""
        <div class="service-card">
            <div class="card-top">
                <span class="card-number">01 / SCHEDULE</span>
                <span class="card-category">CALENDAR</span>
            </div>
            <div class="card-icon">{icon_svg("calendar")}</div>
            <div class="card-title">학교 일정 달력</div>
            <div class="card-description">
                시험, 수행평가, 학교 행사 일정을<br>
                한눈에 확인하세요.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("일정 확인하기  ↗", key="calendar", use_container_width=True):
            go_to_page("학교일정달력.py")


# ---------- 응급톡 ----------
with col2:
    with st.container(border=True):
        st.markdown(f"""
        <div class="service-card">
            <div class="card-top">
                <span class="card-number">02 / SAFETY</span>
                <span class="card-category">EMERGENCY</span>
            </div>
            <div class="card-icon">{icon_svg("medical")}</div>
            <div class="card-title">응급톡</div>
            <div class="card-description">
                응급상황 행동 요령과<br>
                아플 때 대처법을 확인하세요.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("응급 정보 확인  ↗", key="emergency", use_container_width=True):
            go_to_page("응급톡.py")


# ---------- D-Day 알람 ----------
with col3:
    with st.container(border=True):
        st.markdown(f"""
        <div class="service-card">
            <div class="card-top">
                <span class="card-number">03 / D-DAY</span>
                <span class="card-category">COUNTDOWN</span>
            </div>
            <div class="card-icon">{icon_svg("clock")}</div>
            <div class="card-title">D-Day 알람</div>
            <div class="card-description">
                시험과 과제 제출일까지<br>
                남은 날짜를 확인하세요.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("D-Day 확인하기  ↗", key="dday", use_container_width=True):
            go_to_page("D-Day 알람.py")


# ---------- 학교생활 TIP ----------
st.markdown("""
<div class="tip-section">
    <div>
        <div class="tip-label">SCHOOL LIFE / TIP</div>
        <div class="tip-title">Stay prepared.</div>
    </div>
    <div class="tip-text">
        시험과 수행평가 일정을 미리 확인하고,
        중요한 학교생활 정보를 놓치지 마세요.<br>
        응급상황에서는 혼자 해결하려 하지 말고
        주변 선생님에게 도움을 요청하세요.
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- 하단 안내 ----------
st.markdown("""
<div class="footer">
    <div class="footer-brand">SCHOOL LOG<span>.</span></div>
    <div>학교 공식 일정은 학교 공지사항을 통해 확인하세요.</div>
</div>
""", unsafe_allow_html=True)
```
