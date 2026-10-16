import streamlit as st
import datetime
import calendar

# -----------------------------------------------------------------------------
# 페이지 기본 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="우리 학교 포털 & 안내 시스템",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 사이드바 메뉴 구성
# -----------------------------------------------------------------------------
st.sidebar.title("📌 메뉴")
menu = st.sidebar.radio(
    "이동할 페이지를 선택하세요:",
    ["🏠 메인 페이지", "⏳ D-Day 알림", "🚨 비상시 행동요령", "📅 학교 일정 달력"]
)

# -----------------------------------------------------------------------------
# 1. 메인 페이지
# -----------------------------------------------------------------------------
if menu == "🏠 메인 페이지":
    st.title("🏫 학교 정보 & 안전 포털에 오신 것을 환영합니다!")
    st.markdown("---")
    
    st.subheader("📢 주요 공지사항 & 대시보드")
    
    # 3개 컬럼으로 주요 기능 요약 표시
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("### ⏳ 주요 D-Day")
        # 예시 D-Day 연산
        today = datetime.date.today()
        exam_date = datetime.date(today.year, 11, 14) # 예: 수능 또는 기말고사 날짜
        if exam_date < today:
            exam_date = datetime.date(today.year + 1, 11, 14)
        d_day = (exam_date - today).days
        st.metric(label="2025학년도 주요 시험/행사", value=f"D-{d_day}")
        
    with col2:
        st.warning("### 🚨 긴급 연락처")
        st.write("• **학교 교무실:** 02-XXX-XXXX")
        st.write("• **행정실:** 02-XXX-YYYY")
        st.write("• **재난/소방 신고:** 119")
        
    with col3:
        st.success("### 📅 오늘 학사 일정")
        st.write(f"**오늘 날짜:** {today.strftime('%Y년 %m월 %d일')}")
        st.write("• 1학기 중간고사 대비 학습 기간")

    st.markdown("---")
    st.markdown("""
    #### 💡 메뉴 안내
    왼쪽 사이드바를 통해 원하는 기능을 이용하실 수 있습니다.
    - **D-Day 알림**: 다가오는 시험, 방학, 행사 날짜 계산
    - **비상시 행동요령**: 화재, 지진, 대피 등 안전수칙 확인
    - **학교 일정 달력**: 월별 학사 일정 조회
    """)

# -----------------------------------------------------------------------------
# 2. D-Day 알림 페이지
# -----------------------------------------------------------------------------
elif menu == "⏳ D-Day 알림":
    st.title("⏳ D-Day 카운트다운")
    st.write("중요한 학교 행사 및 시험 일정을 확인하고, 나만의 D-Day를 계산해 보세요.")
    st.markdown("---")
    
    # 등록된 일정 예시
    events = {
        "1학기 중간고사": datetime.date(2025, 4, 25),
        "여름방학 개학식": datetime.date(2025, 7, 18),
        "학교 축제": datetime.date(2025, 10, 20),
        "2학기 기말고사": datetime.date(2025, 12, 10)
    }
    
    today = datetime.date.today()
    
    st.subheader("📌 학교 주요 D-Day 일정")
    cols = st.columns(2)
    for idx, (event_name, event_date) in enumerate(events.items()):
        diff = (event_date - today).days
        with cols[idx % 2]:
            if diff > 0:
                st.metric(label=f"{event_name} ({event_date})", value=f"D-{diff}")
            elif diff == 0:
                st.metric(label=f"{event_name} ({event_date})", value="D-Day (오늘!)")
            else:
                st.metric(label=f"{event_name} ({event_date})", value=f"D+{abs(diff)}")

    st.markdown("---")
    st.subheader("➕ 나만의 개인 D-Day 계산기")
    
    user_event_name = st.text_input("일정 이름을 입력하세요", placeholder="예: 수행평가 제출일")
    user_date = st.date_input("날짜를 선택하세요", today)
    
    if user_event_name:
        user_diff = (user_date - today).days
        if user_diff > 0:
            st.success(f"🎉 **[{user_event_name}]**까지 **D-{user_diff}**일 남았습니다!")
        elif user_diff == 0:
            st.warning(f"🔥 **[{user_event_name}]**이 바로 **오늘(D-Day)**입니다!")
        else:
            st.info(f"⌛ **[{user_event_name}]**은(는) **D+{abs(user_diff)}**일 지난 일정입니다.")

# -----------------------------------------------------------------------------
# 3. 비상시 행동요령 페이지
# -----------------------------------------------------------------------------
elif menu == "🚨 비상시 행동요령":
    st.title("🚨 비상시 행동요령")
    st.write("위급 상황 발생 시 당황하지 않고 안전하게 대피할 수 있는 수칙입니다.")
    st.markdown("---")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔥 화재 발생 시", "🏚️ 지진 발생 시", "😷 응급처치 수칙", "📞 비상 연락망"])
    
    with tab1:
        st.error("### 🔥 화재 발생 시 행동요령")
        st.markdown("""
        1. **신속히 알리기**: "불이야!"라고 크게 외치고 비상벨을 누릅니다.
        2. **젖은 수건 이용**: 젖은 수건이나 옷으로 코와 입을 막고 자세를 낮춰 대피합니다.
        3. **승강기 이용 금지**: 엘리베이터 대신 계단을 이용해 지상으로 대피합니다.
        4. **문 손잡이 확인**: 문을 열기 전 손잡이를 짚어보고 뜨거우면 반대쪽 탈출로를 찾습니다.
        """)
        
    with tab2:
        st.warning("### 🏚️ 지진 발생 시 행동요령")
        st.markdown("""
        1. **탁자 아래로 대피**: 책상이나 탁자 아래로 들어가 몸을 보호하고 다리를 꼭 잡습니다.
        2. **방석 등으로 머리 보호**: 교실/실내에서는 가방이나 방석으로 머리를 감쌉니다.
        3. **문 열어두기**: 지진으로 문이 비틀려 갇히지 않도록 미리 문을 열어둡니다.
        4. **운동장으로 대피**: 진동이 멈추면 머리를 보호하며 운동장 등 넓은 공간으로 대피합니다.
        """)

    with tab3:
        st.info("### 😷 기본 응급처치 수칙")
        st.markdown("""
        * **찰과상/상처**: 깨끗한 물로 상처 부위를 씻어내고 소독합니다.
        * **화상**: 흐르는 차가운 물에 10~15분 이상 열을 식혀줍니다 (얼음 직접 대기 금지).
        * **출혈**: 깨끗한 천으로 상처 부위를 직접 압박합니다.
        """)
        
    with tab4:
        st.success("### 📞 긴급 및 주요 서비스 연락처")
        st.table({
            "기관/시설": ["화재/응급환자 (소방서)", "범죄신고 (경찰서)", "학교 보건실", "학교 행정실"],
            "전화번호": ["119", "112", "02-XXX-1114", "02-XXX-1115"],
            "위치": ["-", "-", "본관 1층", "본관 1층"]
        })

# -----------------------------------------------------------------------------
# 4. 학교 일정 달력 페이지
# -----------------------------------------------------------------------------
elif menu == "📅 학교 일정 달력":
    st.title("📅 학
