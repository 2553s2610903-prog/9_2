

import streamlit as st

st.set_page_config(
    page_title="응급 상황별 안내 포스터",
    page_icon="🚑",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f4f8fc;
}
.block-container {
    max-width: 1100px;
    padding: 2rem 1rem;
}
.poster {
    background: #cfe5f8;
    border: 2px solid #3986c5;
    border-radius: 45px;
    padding: 20px;
}
.poster-title {
    text-align: center;
    font-size: 34px;
    font-weight: 900;
    color: #123e70;
}
.subtitle {
    text-align: center;
    color: #34577a;
    margin-bottom: 25px;
}
.section {
    background: #edf6ff;
    border: 2px solid #75b9f3;
    border-radius: 20px;
    padding: 15px;
    margin: 10px 0;
}
.section-label {
    border: 2px solid #174d82;
    border-radius: 8px;
    text-align: center;
    color: #174d82;
    font-weight: bold;
    padding: 5px;
    margin-bottom: 10px;
}
.picture {
    background: linear-gradient(145deg, #e4f2ff, #b9d9f3);
    border: 2px solid #8abce6;
    border-radius: 12px;
    min-height: 150px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: #174d82;
    font-size: 22px;
    font-weight: bold;
    padding: 10px;
}
.guide {
    background: #f8fbff;
    border: 2px solid #8ac7ff;
    border-radius: 14px;
    padding: 15px;
    min-height: 200px;
    color: #20364d;
}
.guide h3 {
    color: #174d82;
    margin-top: 0;
}
.warning {
    color: #b51f2b;
    background: #fff0f1;
    border: 1px solid #f3a4aa;
    border-radius: 8px;
    padding: 10px;
    margin-top: 12px;
    font-weight: bold;
}
.footer {
    background: #fff0f1;
    border: 1px solid #f3a4aa;
    border-radius: 10px;
    text-align: center;
    padding: 15px;
    color: #b51f2b;
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="poster-title">🚨 응급 상황별 안내 포스터</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">'
    '위급한 순간, 침착하게! 올바른 응급처치가 소중한 생명을 지킵니다.'
    '</div>',
    unsafe_allow_html=True
)

name = st.text_input("제작자 이름", "최은진")

situations = [
    {
        "label": "응급상황 1",
        "icon": "🔥",
        "name": "화상",
        "picture": "🔥",
        "steps": [
            "열원에서 안전하게 벗어납니다.",
            "흐르는 시원한 물로 약 20분간 식힙니다.",
            "피부에 붙은 옷은 억지로 떼지 않습니다.",
            "심한 화상은 119에 신고합니다."
        ],
        "warning": "얼음, 치약, 기름을 바르거나 물집을 터뜨리지 마세요."
    },
    {
        "label": "응급상황 2",
        "icon": "🩸",
        "name": "코피",
        "picture": "🩸",
        "steps": [
            "앉아서 머리를 약간 앞으로 숙입니다.",
            "콧방울의 부드러운 부분을 10~15분간 눌러 줍니다.",
            "입으로 숨을 쉬고 피는 삼키지 않습니다.",
            "20분 정도 압박해도 멈추지 않으면 진료를 받습니다."
        ],
        "warning": "고개를 뒤로 젖히거나 코를 세게 풀지 마세요."
    },
    {
        "label": "응급상황 3",
        "icon": "🩹",
        "name": "출혈",
        "picture": "🩹",
        "steps": [
            "가능하면 장갑 등으로 혈액 접촉을 피합니다.",
            "깨끗한 거즈나 천으로 상처를 직접 누릅니다.",
            "피가 배어 나와도 처음 댄 천을 떼지 말고 덧댑니다.",
            "출혈이 심하거나 멈추지 않으면 119에 신고합니다."
        ],
        "warning": "상처에 박힌 물체를 직접 빼내지 마세요."
    }
]

st.markdown(
    '<div class="poster">',
    unsafe_allow_html=True
)

st.markdown(
    f'<div style="text-align:right;color:#174d82;">'
    f'제작자: {name}</div>',
    unsafe_allow_html=True
)

for item in situations:
    st.markdown('<div class="section">', unsafe_allow_html=True)

    left, right = st.columns([1, 2.3], gap="medium")

    with left:
        st.markdown(
            f'<div class="section-label">{item["label"]}</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="picture">'
            f'<div style="font-size:55px">{item["picture"]}</div>'
            f'<div>상황별 그림</div>'
            f'<div>{item["name"]}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    with right:
        steps_html = "".join(
            f'<p style="margin:8px 0;">'
            f'<b style="color:#2167a5;">● {i+1}</b>　{step}</p>'
            for i, step in enumerate(item["steps"])
        )

        st.markdown(
            f'<div class="guide">'
            f'<h3>{item["icon"]} {item["name"]} 발생 시 대처 방법</h3>'
            f'{steps_html}'
            f'<div class="warning">⚠️ 주의사항<br>'
            f'{item["warning"]}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="footer">📞 생명이 위급하면 119</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

st.caption(
    "교육용 자료입니다. 실제 응급 상황에서는 119에 신고하고 "
    "구급상황요원의 안내를 따르세요."
)
