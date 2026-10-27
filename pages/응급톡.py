
import streamlit as st
from pathlib import Path

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
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚑 응급 상황별 안내 포스터")
st.caption("화상 · 코피 · 출혈 응급처치 안내")

# app.py와 같은 폴더에 있는 이미지 불러오기
image_path = Path(__file__).parent / "poster.png"

if image_path.exists():
    st.image(
        str(image_path),
        use_container_width=True
    )
else:
    st.error(
        "poster.png 파일을 찾을 수 없습니다. "
        "app.py와 같은 폴더에 이미지를 넣어 주세요."
    )

st.info("생명이 위급한 경우 119에 신고하세요.")
st.caption("교육용 자료입니다. 실제 상황에서는 119의 안내를 따르세요.")
