import streamlit as st
import datetime
import calendar

# -----------------------------------------------------------------------------
# 1. 기본 페이지 설정 및 세션 상태 초기화
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="school log",
    page_icon="🏫",
    layout="wide"
)

# 현재 선택된 페이지를 저장하는 세션 상태 설정
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 메인 페이지"

def set_page(page_name):
    """페이지 이동 함수"""
    st.session_state.current_page = page_name

# -----------------------------------------------------------------------------
# 2. 사이드바 메뉴 (클릭 이동과 연동)
# -----------------------------------------------------------------------------
st.sidebar.title("📌 school log")
page_options = ["🏠 메인 페이지", "⏳ D-Day 알림", "📅 학교 일정 달력", "🏥 응급톡"]

# 세션 상태에 맞춰 사이드바 라디오 버튼 위치 동기화
selected_menu = st.sidebar.radio(
    "이동할 페이지 선택:",
    page_options,
    index=page_options.index(st.session_state.current_page)
)

# 사이드바에서 직접 클릭했을 경우 업데이트
if selected_menu != st.session_state.current_page:
    st.session_state.current_page = selected_menu
    st.rerun()

# -----------------------------------------------------------------------------
# 3. 페이지 1: 🏠 메인 페이지 (school log)
# -----------------------------------------------------------------------------
if st.session_state.current_page == "🏠 메인 페이지":
    
    st.title("🏫 school log")
    st.markdown("##### 학교 생활에 필요한 주요 정보를 쉽고 빠르게 찾아보세요!")
    st.markdown("---")
    
    st.subheader("💡 기능 바로가기 (원하는 영역을 클릭하세요)")
    st.write("아래 카드나 이미지를 클릭하면 해당 기능 페이지로 즉시 이동합니다.")
    st.write("")

    # 3개 컬럼으로 카드 및 클릭 이동 버튼 배치
    col1, col2, col3 = st.columns(3)
    
    # [카드 1: D-Day 알림]
    with col1:
        with st.container(border=True):
            # Unsplash의 관련 무료 이미지 활용
            st.image(
                "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&w=600&q=80",
                use_container_width=True,
                caption="⏳ D-Day 알림"
            )
            st.markdown("#### ⏳ D-Day 알림")
            st.write("주요 시험, 방학, 행사까지 남은 날짜를 카운트다운하고 나만의 D-Day를 등록하세요.")
            if st.button("👉 D-Day 확인하러 가기", key="btn_dday", use_container_width=True):
                set_page("⏳ D-Day 알림")
                st.rerun()

    # [카드 2: 학교 일정 달력]
    with col2:
        with st.container(border=True):
            st.image(
                "https://images.unsplash.com/photo-1506784365847-bbad939e9335?auto=format&fit=crop&w=600&q=80",
                use_container_width=True,
                caption="📅 학교 일정 달력"
            )
            st.markdown("#### 📅 학교 일정 달력")
            st.write("학사 일정, 시험 기간, 수행평가 제출일을 한눈에 알기 쉬운 달력으로 확인하세요.")
            if st.button("👉 일정 달력 보러 가기", key="btn_cal", use_container_width=True):
                set_page("📅 학교 일정 달력")
                st.rerun()

    # [카드 3: 응급톡]
    with col3:
        with st.container(border=True):
            st.image(
                "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=600&q=80",
                use_container_width=True,
                caption="🏥 응급톡"
            )
            st.markdown("#### 🏥 응급톡")
            st.write("학교에서 갑자기 아프거나 응급 상황 시 꼭 알아야 할 행동 요령과 금지 사항을 확인하세요.")
            if st.button("👉 응급 수칙 확인하러 가기", key="btn_emergency", use_container_width=True):
                set_page("🏥 응급톡")
                st.rerun()

    st.markdown("---")
    
    # 요약 대시보드
    st.subheader("📢 Today's Summary (오늘의 주요 안내)")
    dash_col1, dash_col2 = st.columns(2)
    
    today = datetime.date.today()
    target_date = datetime.date(today.year, 11, 19) # 예시 시험일
    if target_date < today:
        target_date = datetime.date(today.year + 1, 11, 19)
    d_day_val = (target_date - today).days

    with dash_col1:
        st.info(f"📌 **오늘 날짜**: {today.strftime('%Y년 %m월 %d일')}")
        st.metric(label="2026학년도 수능/주요 시험까지", value=f"D-{d_day_val}")

    with dash_col2:
        st.warning("🚨 **보건실 안내**: 본관 1층 위치 / 비상 시 119 또는 교무실 연락")

# -----------------------------------------------------------------------------
# 4. 페이지 2: ⏳ D-Day 알림
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "⏳ D-Day 알림":
    st.title("⏳ D-Day 알림")
    st.write("학교 주요 일정 카운트다운 및 나만의 D-Day 계산기입니다.")
    st.markdown("---")
    
    today = datetime.date.today()
    
    # 학사 D-Day
    events = {
        "1학기 중간고사": datetime.date(2026, 4, 27),
        "여름방학 개학식": datetime.date(2026, 7, 17),
        "2027학년도 수능": datetime.date(2026, 11, 19),
    }
    
    st.subheader("📌 주요 학사 D-Day")
    d_cols = st.columns(len(events))
    for idx, (name, date_val) in enumerate(events.items()):
        diff = (date_val - today).days
        with d_cols[idx]:
            if diff > 0:
                st.metric(label=name, value=f"D-{diff}", delta=f"{date_val.strftime('%Y-%m-%d')}")
            elif diff == 0:
                st.metric(label=name, value="D-Day", delta="오늘입니다!")
            else:
                st.metric(label=name, value=f"D+{abs(diff)}", delta="지난 일정")
                
    st.markdown("---")
    st.subheader("➕ 나만의 개인 D-Day 계산")
    
    user_event = st.text_input("일정 이름을 입력하세요", value="수행평가 제출")
    user_date = st.date_input("목표 날짜를 선택하세요", today)
    
    if user_event:
        user_diff = (user_date - today).days
        if user_diff > 0:
            st.success(f"🎉 **[{user_event}]**까지 **D-{user_diff}**일 남았습니다!")
        elif user_diff == 0:
            st.warning(f"🔥 **[{user_event}]**이 바로 **오늘(D-Day)**입니다!")
        else:
            st.info(f"⌛ **[{user_event}]**은(는) **D+{abs(user_diff)}**일 경과했습니다.")

# -----------------------------------------------------------------------------
# 5. 페이지 3: 📅 학교 일정 달력
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "📅 학교 일정 달력":
    st.title("📅 학교 일정 달력")
    st.write("월별 학사 일정과 수행평가/시험 일정을 확인하세요.")
    st.markdown("---")
    
    c_col1, c_col2 = st.columns([1, 2])
    
    # 학사 일정 샘플
    schedules = {
        "2026-03-03": "1학기 입학식 및 개학식",
        "2026-04-27": "1학기 중간고사 시작",
        "2026-05-05": "어린이날 (공휴일)",
        "2026-05-15": "체육대회",
        "2026-07-17": "여름방학식",
    }
    
    with c_col1:
        st.subheader("📆 월 선택")
        year = st.number_input("연도", min_value=2025, max_value=2030, value=2026)
        month = st.selectbox("월", list(range(1, 13)), index=datetime.datetime.now().month - 1)
        
        cal_str = calendar.month(year, month)
        st.text_area("달력 보기", cal_str, height=200)

    with c_col2:
        st.subheader(f"📌 {year}년 {month}월 등록 일정")
        prefix = f"{year}-{month:02d}"
        found = False
        for date_str, detail in schedules.items():
            if date_str.startswith(prefix):
                st.info(f"**{date_str}**: {detail}")
                found = True
        if not found:
            st.write("해당 월에 등록된 주요 일정이 없습니다.")

# -----------------------------------------------------------------------------
# 6. 페이지 4: 🏥 응급톡
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "🏥 응급톡":
    st.title("🏥 응급톡")
    st.write("학교에서 응급 상황 및 갑자기 아플 때의 대처 수칙 포스터입니다.")
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["🤒 갑작스러운 복통/발열", "🩸 코피/상처 발생 시", "🚨 긴급 연락처"])
    
    with tab1:
        e_col1, e_col2 = st.columns(2)
        with e_col1:
            st.success("### ⭕ 해야 할 행동 (DO)")
            st.markdown("- 편안한 자세로 누워 휴식\n- 옷 단추를 풀어 압박 줄이기\n- 즉시 보건실이나 선생님께 알리기")
        with e_col2:
            st.error("### ❌ 하면 안 되는 행동 (DON'T)")
            st.markdown("- 임의로 약 복용하지 않기\n- 아픈 배를 강하게 누르지 않기\n- 차가운 음료 마시지 않기")

    with tab2:
        e_col1, e_col2 = st.columns(2)
        with e_col1:
            st.success("### ⭕ 코피 발생 시 행동")
            st.markdown("- **고개를 약간 앞으로 숙이기**\n- 코뼈 아래 말랑한 부위를 5~10분 지그시 압박\n- 콧등에 아이스팩 대어주기")
        with e_col2:
            st.error("### ❌ 절대 금지 행동")
            st.markdown("- **고개를 뒤로 젖히지 말 것** (목으로 피가 넘어감)\n- 코를 세게 팽 지 말 것")

    with tab3:
        st.subheader("📞 주요 긴급 연락처")
        st.table({
            "구분": ["보건실", "교무실", "소방서 (응급신고)", "경찰서"],
            "위치 및 번호": ["본관 1층", "본관 2층", "119", "112"]
        })
    
