import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="고급 계산기", page_icon="🧮")

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

    x_min = st.number_input("x 최소값", value=-10.0)
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

            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(x, y)

            ax.set_title(f"y = {expr}")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.grid(True)

            st.pyplot(fig)

        except Exception as e:
            st.error(f"함수 입력 오류: {e}")

# ==========================
# 로그
# ==========================
elif operation == "로그":

    x = st.number_input("진수 (x)", value=10.0)
    base = st.number_input("밑 (base)", value=10.0)

    if st.button("계산"):

        try:
            result = math.log(x, base)
            st.success(f"결과: {result}")

        except ValueError:
            st.error("진수와 밑은 0보다 커야 합니다.")

# ==========================
# 순열
# ==========================
elif operation == "순열(nPr)":

    n = st.number_input("n", min_value=0, step=1)
    r = st.number_input("r", min_value=0, step=1)

    if st.button("계산"):

        try:
            if r > n:
                st.error("r은 n보다 클 수 없습니다.")
            else:
                result = math.perm(int(n), int(r))
                st.success(f"순열 nPr = {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")

# ==========================
# 조합
# ==========================
elif operation == "조합(nCr)":

    n = st.number_input("n", min_value=0, step=1)
    r = st.number_input("r", min_value=0, step=1)

    if st.button("계산"):

        try:
            if r > n:
                st.error("r은 n보다 클 수 없습니다.")
            else:
                result = math.comb(int(n), int(r))
                st.success(f"조합 nCr = {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")

# ==========================
# 중복조합
# ==========================
elif operation == "중복조합(nHr)":

    n = st.number_input("n", min_value=1, step=1)
    r = st.number_input("r", min_value=0, step=1)

    if st.button("계산"):

        try:
            result = math.comb(int(n + r - 1), int(r))
            st.success(f"중복조합 nHr = {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")

# ==========================
# 일반 계산기
# ==========================
else:

    num1 = st.number_input("첫 번째 수", value=0.0)
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

            st.success(f"결과: {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")
