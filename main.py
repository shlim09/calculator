import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="고급 계산기", page_icon="🧮", layout="wide")

# 모던 디자인 CSS
st.markdown("""
    <style>
    /* 전체 배경 */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-attachment: fixed;
        min-height: 100vh;
    }
    
    /* 페이지 배경 */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-attachment: fixed;
    }
    
    /* 사이드바 배경 */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(102, 126, 234, 0.95) 0%, rgba(118, 75, 162, 0.95) 100%);
    }
    
    /* 컨테이너/카드 스타일 */
    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin-bottom: 20px;
    }
    
    /* 제목 스타일 */
    h1 {
        color: white;
        text-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    
    h2 {
        color: #667eea;
        font-weight: 700;
        margin-top: 20px;
    }
    
    h3 {
        color: #764ba2;
        font-weight: 600;
    }
    
    /* 텍스트 스타일 */
    p {
        color: #2d3748;
        line-height: 1.6;
    }
    
    /* 버튼 스타일 */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 28px;
        font-weight: 600;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px 0 rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #f093fb 100%);
        box-shadow: 0 6px 20px 0 rgba(102, 126, 234, 0.6);
        transform: translateY(-2px);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* 입력 필드 스타일 */
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-size: 16px !important;
        color: #2d3748 !important;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus,
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        outline: none !important;
    }
    
    /* Select 박스 스타일 */
    .stSelectbox > div > div > select {
        background-color: rgba(255, 255, 255, 0.95) !important;
        color: #2d3748 !important;
        cursor: pointer;
    }
    
    /* 성공 메시지 */
    .stSuccess {
        background: linear-gradient(135deg, rgba(52, 211, 153, 0.1) 0%, rgba(16, 185, 129, 0.1) 100%) !important;
        border-left: 4px solid #34d399 !important;
        border-radius: 8px;
        padding: 16px;
        color: #047857;
        font-weight: 500;
    }
    
    /* 에러 메시지 */
    .stError {
        background: linear-gradient(135deg, rgba(248, 113, 113, 0.1) 0%, rgba(239, 68, 68, 0.1) 100%) !important;
        border-left: 4px solid #f87171 !important;
        border-radius: 8px;
        padding: 16px;
        color: #991b1b;
        font-weight: 500;
    }
    
    /* 라벨 스타일 */
    label {
        color: #2d3748 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }
    
    /* 그래프 컨테이너 */
    .stPlotlyContainer {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Matplotlib 그래프 */
    .stPyplotContainer {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* 메트릭 스타일 */
    .stMetric {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(240, 147, 251, 0.1) 100%);
        border-radius: 12px;
        padding: 20px;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    .stMetric > div:nth-child(1) {
        color: #667eea;
        font-weight: 700;
    }
    
    .stMetric > div:nth-child(2) {
        color: #2d3748;
        font-weight: 600;
        font-size: 28px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧮 고급 계산기")
st.write("사칙연산, 모듈러 연산, 지수 연산, 로그 연산, 순열/조합, 함수 그래프를 지원합니다.")

operation = st.selectbox(
    "기능 선택",
    [
        "덧셈",
        "뺄셈",
        "곱셈",
        "나눗셈",
        "모듈러(나머지)",
        "지수",
        "로그",
        "순열(nPr)",
        "조합(nCr)",
        "중복조합(nHr)",
        "함수 그래프"
    ]
)

# ==========================
# 함수 그래프
# ==========================
if operation == "함수 그래프":

    st.subheader("📈 함수 그래프 그리기")

    expr = st.text_input(
        "함수를 입력하세요 (예: x**2, np.sin(x), np.cos(x), np.exp(x))",
        value="x**2"
    )

    col1, col2 = st.columns(2)
    with col1:
        x_min = st.number_input("x 최소값", value=-10.0)
    with col2:
        x_max = st.number_input("x 최대값", value=10.0)

    if st.button("그래프 그리기"):

        try:
            x = np.linspace(x_min, x_max, 1000)

            y = eval(
                expr,
                {
                    "__builtins__": {},
                    "np": np,
                    "x": x,
                    "math": math
                }
            )

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x, y, linewidth=2.5, color='#667eea')

            ax.set_title(f"y = {expr}", fontsize=16, fontweight='bold', color='#2d3748')
            ax.set_xlabel("x", fontsize=12, fontweight='bold', color='#2d3748')
            ax.set_ylabel("y", fontsize=12, fontweight='bold', color='#2d3748')
            ax.grid(True, alpha=0.3, linestyle='--')
            ax.set_facecolor('rgba(255, 255, 255, 0.98)')
            fig.patch.set_facecolor('transparent')

            st.pyplot(fig)

        except Exception as e:
            st.error(f"함수 입력 오류: {e}")

# ==========================
# 로그
# ==========================
elif operation == "로그":

    col1, col2 = st.columns(2)
    with col1:
        x = st.number_input("진수 (x)", value=10.0)
    with col2:
        base = st.number_input("밑 (base)", value=10.0)

    if st.button("계산"):

        try:
            result = math.log(x, base)
            st.metric("계산 결과", f"{result:.6f}")

        except ValueError:
            st.error("진수와 밑은 0보다 커야 합니다.")

# ==========================
# 순열
# ==========================
elif operation == "순열(nPr)":

    col1, col2 = st.columns(2)
    with col1:
        n = st.number_input("n", min_value=0, step=1)
    with col2:
        r = st.number_input("r", min_value=0, step=1)

    if st.button("계산"):

        try:
            if r > n:
                st.error("r은 n보다 클 수 없습니다.")
            else:
                result = math.perm(int(n), int(r))
                st.metric("순열 결과 (nPr)", result)

        except Exception as e:
            st.error(f"오류 발생: {e}")

# ==========================
# 조합
# ==========================
elif operation == "조합(nCr)":

    col1, col2 = st.columns(2)
    with col1:
        n = st.number_input("n", min_value=0, step=1)
    with col2:
        r = st.number_input("r", min_value=0, step=1)

    if st.button("계산"):

        try:
            if r > n:
                st.error("r은 n보다 클 수 없습니다.")
            else:
                result = math.comb(int(n), int(r))
                st.metric("조합 결과 (nCr)", result)

        except Exception as e:
            st.error(f"오류 발생: {e}")

# ==========================
# 중복조합
# ==========================
elif operation == "중복조합(nHr)":

    col1, col2 = st.columns(2)
    with col1:
        n = st.number_input("n", min_value=1, step=1)
    with col2:
        r = st.number_input("r", min_value=0, step=1)

    if st.button("계산"):

        try:
            result = math.comb(int(n + r - 1), int(r))
            st.metric("중복조합 결과 (nHr)", result)

        except Exception as e:
            st.error(f"오류 발생: {e}")

# ==========================
# 일반 계산기
# ==========================
else:

    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("첫 번째 수", value=0.0)
    with col2:
        num2 = st.number_input("두 번째 수", value=0.0)

    if st.button("계산"):

        try:

            if operation == "덧셈":
                result = num1 + num2

            elif operation == "뺄셈":
                result = num1 - num2

            elif operation == "곱셈":
                result = num1 * num2

            elif operation == "나눗셈":

                if num2 == 0:
                    st.error("0으로 나눌 수 없습니다.")
                    st.stop()

                result = num1 / num2

            elif operation == "모듈러(나머지)":
                result = num1 % num2

            elif operation == "지수":
                result = num1 ** num2

            st.metric("계산 결과", f"{result:.6f}" if isinstance(result, float) else result)

        except Exception as e:
            st.error(f"오류 발생: {e}")
