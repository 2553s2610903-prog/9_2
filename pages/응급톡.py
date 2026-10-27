
import streamlit as st

st.set_page_config(
    page_title="응급 상황별 안내 포스터",
    page_icon="🚑",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #ffffff;
}
.main-title {
    text-align: center;
    color: #1c3557;
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 20px;
}
.poster {
    background-color: #cfe2f3;
    border: 1px solid #333333;
    border-radius: 75px;
    padding: 30px;
}
.section-title {
    border: 1px solid #333333;
    text-align: center;
    font-size: 18px;
    padding: 2px;
    margin-bottom: 12px;
    color: #222222;
}
.guide {
    background-color: #d7e7f5;
    border: 1px solid #333333;
    border-radius: 2px;
    padding: 18px;
    min-height: 150px;
    color: #222222;
}
.guide h3 {
    margin-top: 0;
    color: #174a7e;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🚑 응급 상황별 안내 포스터</div>',
    unsafe_allow_html=True
)

author = st.text_input("제작자 이름", "최은진")

st.markdown(f"**제작자: {author}**")

# 세 가지 응급 상황
situations = [
    {
        "name": "응급상황 1",
        "situation": "🔥 화상",
        "steps": [
            "1. 열원에서 안전하게 벗어납니다.",
            "2. 흐르는 시원한 물로 약 20분간 식힙니다.",
            "3. 얼음이나 치약을 바르지 않습니다.",
            "4. 심한 화상은 119에 신고합니다."
        ]
    },
    {
        "name": "응급상황 2",
        "situation": "🩸 출혈",
        "steps": [
            "1. 가능하면 장갑 등으로 혈액 접촉을 피합니다.",
            "2. 깨끗한 거즈나 천으로 상처를 직접 누릅니다.",
            "3. 피가 배어 나와도 처음 댄 천을 떼지 말고 덧댑니다.",
            "4. 출혈이 심하면 119에 신고합니다."
        ]
    },
    {
        "name": "응급상황 3",
        "situation": "⚡ 경련",
        "steps": [
            "1. 주변의 위험한 물건을 치웁니다.",
            "2. 머리 아래에 부드러운 것을 놓습니다.",
            "3. 몸을 억지로 누르거나 입에 물건을 넣지 않습니다.",
            "4. 5분 이상 지속되거나 호흡에 문제가 있으면 119에 신고합니다."
        ]
    }
]

# 큰 포스터 영역
with st.container(border=True):
    for i, item in enumerate(situations):
        left, right = st.columns([1, 2.5], gap="large")

        with left:
            st.markdown(
                f'<div class="section-title">{item["name"]}</div>',
                unsafe_allow_html=True
            )

            uploaded_image = st.file_uploader(
                "상황별 사진",
                type=["png", "jpg", "jpeg"],
                key=f"image_{i}",
                label_visibility="collapsed"
            )

            if uploaded_image:
                st.image(uploaded_image, use_container_width=True)
            else:
                st.info(
                    f'📷 {item["situation"]}\n\n'
                    '사진을 업로드해 주세요.'
                )

        with right:
            st.markdown(
                f"""
                <div class="guide">
                    <h3>{item["situation"]}</h3>
                    <b>상황별 안내</b><br><br>
                    {"<br>".join(item["steps"])}
                </div>
                """,
                unsafe_allow_html=True
            )

        if i < len(situations) - 1:
            st.write("")

st.warning(
    "실제 응급 상황에서는 119에 신고하고 "
    "구급상황요원의 지시에 따르세요."
)

st.caption(
    "교육용 자료입니다. 게시 전 응급처치 지침을 확인하세요."
)
