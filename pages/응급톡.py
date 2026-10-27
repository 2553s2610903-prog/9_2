
import streamlit as st

st.set_page_config(
    page_title="응급 상황별 안내 포스터",
    page_icon="🚑",
    layout="centered"
)

# 포스터 디자인
st.markdown("""
<style>
.stApp {
    background-color: #f3f6fa;
}
.poster {
    background: white;
    border-radius: 18px;
    padding: 28px;
    border-top: 10px solid #d62828;
    box-shadow: 0 4px 18px #00000012;
}
.poster h1 {
    color: #c62828;
    font-size: 30px;
}
.poster h3 {
    color: #174a7e;
}
.notice {
    background: #fff0f0;
    padding: 14px;
    border-radius: 10px;
    color: #a31515;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 응급 상황별 안내 데이터
emergencies = {
    "🔥 화상": {
        "title": "화상 발생 시 대처 방법",
        "subtitle": "빠른 응급처치가 중요합니다.",
        "steps": [
            "1. 열원에서 안전하게 벗어납니다.",
            "2. 흐르는 시원한 물로 약 20분간 식힙니다.",
            "3. 피부에 붙은 옷이나 물질은 억지로 떼지 않습니다.",
            "4. 심한 화상은 119에 신고하고 의료진의 도움을 받습니다."
        ],
        "avoid": "얼음, 치약, 기름을 바르거나 물집을 터뜨리지 마세요."
    },
    "🩸 출혈": {
        "title": "출혈 발생 시 대처 방법",
        "subtitle": "주변의 안전을 먼저 확인하세요.",
        "steps": [
            "1. 가능하면 장갑 등으로 혈액 접촉을 피합니다.",
            "2. 깨끗한 천이나 거즈로 상처를 직접 눌러 지혈합니다.",
            "3. 피가 배어 나와도 처음 댄 천을 떼지 말고 덧댑니다.",
            "4. 출혈이 심하거나 멈추지 않으면 119에 신고합니다."
        ],
        "avoid": "상처에 박힌 물체를 직접 빼내지 마세요."
    },
    "😮 기도폐쇄": {
        "title": "음식물이 목에 걸렸을 때",
        "subtitle": "말하거나 기침할 수 있는지 확인하세요.",
        "steps": [
            "1. 강하게 기침할 수 있다면 기침하도록 돕습니다.",
            "2. 말하거나 숨 쉬지 못하면 즉시 119에 신고합니다.",
            "3. 성인 및 1세 이상 아동은 상황에 맞는 기도폐쇄 응급처치를 시행합니다.",
            "4. 의식을 잃으면 바닥에 안전하게 눕히고 119의 지시에 따릅니다."
        ],
        "avoid": "보이지 않는 음식물을 손가락으로 무작정 꺼내려 하지 마세요."
    },
    "❤️ 심정지 의심": {
        "title": "반응이 없고 정상 호흡이 없을 때",
        "subtitle": "즉시 도움을 요청하세요.",
        "steps": [
            "1. 현장 안전을 확인하고 반응과 정상 호흡을 확인합니다.",
            "2. 119에 신고하고 스피커폰으로 안내를 받습니다.",
            "3. 가슴압박을 시작하고 구급상황요원의 지시에 따릅니다.",
            "4. AED(자동심장충격기)가 있으면 가져와 음성 안내에 따릅니다."
        ],
        "avoid": "정상 호흡 여부가 불확실하면 지체하지 말고 119에 상담하세요."
    },
    "⚡ 경련": {
        "title": "경련이 발생했을 때",
        "subtitle": "다치지 않도록 주변을 안전하게 만드세요.",
        "steps": [
            "1. 주변의 단단하거나 위험한 물건을 치웁니다.",
            "2. 머리 아래에 부드러운 것을 놓고 경련 시간을 확인합니다.",
            "3. 경련을 억지로 멈추게 하거나 몸을 누르지 않습니다.",
            "4. 경련이 5분 이상 지속되거나 반복되거나 호흡에 문제가 있으면 119에 신고합니다."
        ],
        "avoid": "입안에 손가락이나 물건을 넣거나 물을 먹이지 마세요."
    }
}

st.title("🚑 응급 상황별 안내 포스터")
st.write("응급 상황을 선택하고 핵심 대처 방법을 확인하세요.")

# 상황 선택
selected = st.selectbox(
    "어떤 응급 상황인가요?",
    list(emergencies.keys())
)

data = emergencies[selected]

# 포스터 내용 만들기
poster_text = f"""
{data['title']}

{data['subtitle']}

응급 대처 방법
""" + "\n".join(data["steps"]) + f"""

주의 사항
{data['avoid']}

생명이 위급하거나 판단이 어려우면 119에 신고하세요.
교육용 안내이며 전문적인 응급의료를 대신하지 않습니다.
"""

# 포스터 표시
st.markdown(f"""
<div class="poster">
    <h1>🚨 {data['title']}</h1>
    <p><b>{data['subtitle']}</b></p>
    <hr>
    <h3>📌 응급 대처 방법</h3>
    <ol>
        {''.join(f'<li style="margin-bottom:12px">{step[3:]}</li>' for step in data['steps'])}
    </ol>
    <div class="notice">
        ⚠️ 주의 사항<br><br>
        {data['avoid']}
    </div>
    <br>
    <p style="text-align:center; font-size:22px; font-weight:bold;">
        📞 생명이 위급하면 119
    </p>
    <p style="color:#666; font-size:12px;">
        교육용 자료입니다. 실제 상황에서는 119의 안내를 따르세요.
    </p>
</div>
""", unsafe_allow_html=True)

# 다운로드
st.download_button(
    label="📥 포스터 내용 다운로드",
    data=poster_text,
    file_name="응급상황_안내포스터.txt",
    mime="text/plain"
)

st.divider()

st.caption(
    "참고: 소방청 응급처치 안전교육 자료"
)

st.markdown(
    "[소방청 공식 응급처치 교육자료 바로가기]"
    "(https://www.nfa.go.kr/nfa/safetyinfo/lifesafety/)"
)
