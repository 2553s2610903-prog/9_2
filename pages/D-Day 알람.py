
import json
import uuid
from datetime import date, timedelta
from pathlib import Path

import streamlit as st

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(
    page_title="D-DAY | 오늘의 카운트다운",
    page_icon="🗓️",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_FILE = Path(__file__).parent / "dday_data.json"

CATEGORIES = ["시험", "생일", "기념일", "목표", "여행", "기타"]

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #faf8ff 0%, #fffdf9 100%);
    }
    h1, h2, h3 {
        color: #55456f;
    }
    .hero {
        padding: 28px;
        border-radius: 22px;
        background: linear-gradient(135deg, #e9ddff, #fff0e8);
        margin-bottom: 20px;
    }
    .hero-label {
        color: #68567f;
        font-size: 15px;
    }
    .hero-number {
        color: #493660;
        font-size: 54px;
        font-weight: 800;
        line-height: 1.3;
    }
    .hero-sub {
        color: #68567f;
        font-size: 16px;
    }
    .event-card {
        padding: 18px;
        border: 1px solid #eee6f5;
        border-radius: 16px;
        background: rgba(255,255,255,0.9);
        margin-bottom: 8px;
    }
    div.stButton > button {
        border-radius: 12px;
    }
    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #eee6f5;
        padding: 15px;
        border-radius: 14px;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# 데이터 저장 및 불러오기
# -----------------------------
def load_events():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            return []

        valid_events = []
        for item in data:
            if not isinstance(item, dict):
                continue

            try:
                event_date = date.fromisoformat(item["date"])
                title = str(item["title"]).strip()
                if not title:
                    continue

                valid_events.append({
                    "id": str(item.get("id") or uuid.uuid4()),
                    "title": title[:100],
                    "date": event_date.isoformat(),
                    "category": (
                        item.get("category")
                        if item.get("category") in CATEGORIES
                        else "기타"
                    ),
                    "memo": str(item.get("memo", ""))[:500],
                })
            except (KeyError, TypeError, ValueError):
                continue

        return valid_events

    except (OSError, json.JSONDecodeError):
        return []


def save_events(events):
    temp_file = DATA_FILE.with_suffix(".tmp")
    try:
        with temp_file.open("w", encoding="utf-8") as file:
            json.dump(events, file, ensure_ascii=False, indent=2)
        temp_file.replace(DATA_FILE)
        return True
    except OSError:
        try:
            if temp_file.exists():
                temp_file.unlink()
        except OSError:
            pass
        return False


if "events" not in st.session_state:
    st.session_state.events = load_events()

if "notice" not in st.session_state:
    st.session_state.notice = None


def notify(message, kind="success"):
    st.session_state.notice = (kind, message)


def get_days(event):
    event_date = date.fromisoformat(event["date"])
    return (event_date - date.today()).days


def format_dday(days):
    if days > 0:
        return f"D-{days}"
    if days == 0:
        return "D-DAY"
    return f"D+{abs(days)}"


def event_order(event):
    days = get_days(event)
    # 다가오는 일정 우선, 지난 일정은 그 뒤에 표시
    return (days < 0, abs(days) if days < 0 else days, event["title"])


def event_details(event):
    days = get_days(event)
    event_date = date.fromisoformat(event["date"])
    if days > 0:
        status = f"{days}일 남았어요"
    elif days == 0:
        status = "바로 오늘이에요!"
    else:
        status = f"{abs(days)}일 지났어요"

    return event_date.strftime("%Y년 %m월 %d일"), status


# -----------------------------
# 사이드바
# -----------------------------
with st.sidebar:
    st.markdown("# 🗓️ D-DAY")
    st.caption("기다리는 날을 기록해 보세요.")
    page = st.radio(
        "메뉴",
        ["홈", "일정 등록", "전체 일정"],
        label_visibility="collapsed",
    )
    st.divider()
    st.caption("✦ 오늘의 날짜")
    st.markdown(f"**{date.today().strftime('%Y년 %m월 %d일')}**")
    st.caption("날짜는 앱을 실행할 때마다 자동으로 계산돼요.")

if st.session_state.notice:
    kind, message = st.session_state.notice
    if kind == "error":
        st.error(message)
    elif kind == "warning":
        st.warning(message)
    else:
        st.success(message)
    st.session_state.notice = None


# -----------------------------
# 홈 화면
# -----------------------------
if page == "홈":
    st.title("오늘의 카운트다운 ✨")
    st.write("기다리는 날도, 이루고 싶은 목표도 한곳에.")

    events = sorted(st.session_state.events, key=event_order)
    today = date.today()

    upcoming = [
        e for e in events
        if date.fromisoformat(e["date"]) >= today
    ]

    if upcoming:
        closest = upcoming[0]
        days = get_days(closest)
        date_text, status = event_details(closest)

        st.markdown(
            f"""
            <div class="hero">
                <div class="hero-label">✦ 가장 가까운 D-DAY</div>
                <div class="hero-number">{format_dday(days)}</div>
                <h2>{closest["title"]}</h2>
                <div class="hero-sub">{date_text} · {status}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="hero">
                <div class="hero-label">✦ 새로운 시작</div>
                <div class="hero-number">D-?</div>
                <h3>기다리는 날을 추가해 보세요!</h3>
                <div class="hero-sub">
                    첫 번째 일정을 등록하면 카운트다운이 시작돼요.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    total = len(events)
    future_count = len(upcoming)
    passed_count = total - future_count

    col1, col2, col3 = st.columns(3)
    col1.metric("전체 일정", f"{total}개")
    col2.metric("다가오는 일정", f"{future_count}개")
    col3.metric("지난 일정", f"{passed_count}개")

    st.subheader("다가오는 일정")

    if not upcoming:
        st.info("아직 등록된 일정이 없어요. 왼쪽 메뉴에서 일정을 추가해 보세요.")
    else:
        for event in upcoming[:5]:
            days = get_days(event)
            date_text, status = event_details(event)
            with st.container(border=True):
                left, right = st.columns([3, 1])
                with left:
                    st.markdown(f"**{event['title']}**")
                    st.caption(
                        f"{event['category']} · {date_text}"
                    )
                    if event["memo"]:
                        st.write(event["memo"])
                with right:
                    st.markdown(f"### {format_dday(days)}")
                    st.caption(status)

    st.divider()
    st.subheader("🔔 일정 알림 미리보기")
    today_events = [e for e in events if get_days(e) == 0]
    tomorrow_events = [e for e in events if get_days(e) == 1]
    week_events = [e for e in events if get_days(e) == 7]

    if today_events:
        for e in today_events:
            st.success(f"🎉 오늘은 '{e['title']}' 일정이 있는 날이에요!")
    if tomorrow_events:
        for e in tomorrow_events:
            st.info(f"🌷 내일은 '{e['title']}' 일정이 있어요.")
    if week_events:
        for e in week_events:
            st.warning(f"📌 일주일 뒤에 '{e['title']}' 일정이 있어요.")

    if not today_events and not tomorrow_events and not week_events:
        st.caption("오늘, 내일, 7일 뒤에 해당하는 일정이 없어요.")

    st.caption(
        "알림은 앱 화면에 표시됩니다. 앱을 닫은 상태에서 "
        "휴대전화 푸시 알림이나 이메일을 보내지는 않아요."
    )


# -----------------------------
# 일정 등록 화면
# -----------------------------
elif page == "일정 등록":
    st.title("새로운 일정 등록 ✍️")
    st.write("기억하고 싶은 날을 추가해 보세요.")

    with st.form("add_event_form", clear_on_submit=True):
        title = st.text_input(
            "일정 이름",
            placeholder="예: 중간고사, 생일, 여행 출발",
            max_chars=100,
        )
        event_date = st.date_input(
            "날짜",
            value=date.today() + timedelta(days=7),
            min_value=date(1900, 1, 1),
            max_value=date(2100, 12, 31),
        )
        category = st.selectbox("분류", CATEGORIES)
        memo = st.text_area(
            "메모 (선택)",
            placeholder="준비물이나 기억할 내용을 적어 보세요.",
            max_chars=500,
        )

        submitted = st.form_submit_button(
            "✨ 일정 저장",
            use_container_width=True,
        )

    if submitted:
        if not title.strip():
            st.error("일정 이름을 입력해 주세요.")
        else:
            new_event = {
                "id": str(uuid.uuid4()),
                "title": title.strip(),
                "date": event_date.isoformat(),
                "category": category,
                "memo": memo.strip(),
            }
            updated = st.session_state.events + [new_event]

            if save_events(updated):
                st.session_state.events = updated
                notify(f"'{title.strip()}' 일정을 저장했어요!")
                st.rerun()
            else:
                st.error(
                    "파일에 저장하지 못했어요. 배포 환경의 쓰기 권한을 "
                    "확인해 주세요. 현재 화면의 일정은 유지됩니다."
                )

    st.divider()
    st.caption("💡 지난 날짜를 선택하면 지난 일정도 기록할 수 있어요.")


# -----------------------------
# 전체 일정 화면
# -----------------------------
elif page == "전체 일정":
    st.title("나의 모든 일정 📚")
    st.write("등록한 일정을 검색하고 분류별로 확인해 보세요.")

    events = sorted(st.session_state.events, key=event_order)

    search_text = st.text_input(
        "🔎 일정 검색",
        placeholder="일정 이름 또는 메모 검색",
    )
    selected_category = st.selectbox(
        "분류 필터",
        ["전체"] + CATEGORIES,
    )
    date_filter = st.selectbox(
        "기간 필터",
        ["전체", "다가오는 일정", "지난 일정", "오늘"],
    )

    filtered = []
    for event in events:
        days = get_days(event)

        if selected_category != "전체" and event["category"] != selected_category:
            continue

        if date_filter == "다가오는 일정" and days < 0:
            continue
        if date_filter == "지난 일정" and days >= 0:
            continue
        if date_filter == "오늘" and days != 0:
            continue

        query = search_text.strip().casefold()
        searchable = (event["title"] + " " + event["memo"]).casefold()
        if query and query not in searchable:
            continue

        filtered.append(event)

    st.caption(f"검색 결과: {len(filtered)}개")

    if not filtered:
        st.info("조건에 맞는 일정이 없어요.")
    else:
        for event in filtered:
            days = get_days(event)
            date_text, status = event_details(event)

            with st.container(border=True):
                left, center, right = st.columns([3, 1, 1])

                with left:
                    st.markdown(f"**{event['title']}**")
                    st.caption(f"{event['category']} · {date_text}")
                    if event["memo"]:
                        st.write(event["memo"])
                    st.caption(status)

                with center:
                    st.markdown(f"### {format_dday(days)}")

                with right:
                    if st.button(
                        "🗑️ 삭제",
                        key=f"delete_{event['id']}",
                        use_container_width=True,
                    ):
                        st.session_state.pending_delete = event["id"]

                if st.session_state.get("pending_delete") == event["id"]:
                    st.warning(f"'{event['title']}' 일정을 삭제할까요?")
                    confirm_col, cancel_col = st.columns(2)

                    with confirm_col:
                        if st.button(
                            "삭제 확인",
                            key=f"confirm_{event['id']}",
                            type="primary",
                            use_container_width=True,
                        ):
                            updated = [
                                e for e in st.session_state.events
                                if e["id"] != event["id"]
                            ]
                            if save_events(updated):
                                st.session_state.events = updated
                                del st.session_state.pending_delete
                                notify("일정을 삭제했어요.")
                                st.rerun()
                            else:
                                st.error("삭제 내용을 파일에 저장하지 못했어요.")

                    with cancel_col:
                        if st.button(
                            "취소",
                            key=f"cancel_{event['id']}",
                            use_container_width=True,
                        ):
                            del st.session_state.pending_delete
                            st.rerun()

    st.divider()
    st.caption(
        "참고: JSON 파일 저장 방식은 개인용 또는 소규모 테스트용입니다. "
        "여러 사용자가 함께 이용하는 서비스라면 데이터베이스 사용을 권장해요."
    )

