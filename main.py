import streamlit as st
import math

st.set_page_config(page_title="고급 계산기", page_icon="🧮")

st.title("🧮 고급 계산기")
st.write("사칙연산, 모듈러 연산, 지수 연산, 로그 연산을 지원합니다.")

operation = st.selectbox(
    "연산 선택",
    [
        "덧셈",
        "뺄셈",
        "곱셈",
        "나눗셈",
        "모듈러(나머지)",
        "지수",
        "로그"
    ]
)

if operation == "로그":
    x = st.number_input("진수 (x)", value=10.0)
    base = st.number_input("밑 (base)", value=10.0)

    if st.button("계산"):
        try:
            result = math.log(x, base)
            st.success(f"결과: {result}")
        except ValueError:
            st.error("진수와 밑은 0보다 커야 합니다.")
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
