import streamlit as st

st.title("넥쏘 수소량 계산기")

range_km = st.number_input("남은 주행 가능 거리 (km)", min_value=0.0, step=1.0)
efficiency = st.number_input("복합 연비 (km/kg)", min_value=0.1, step=0.1, value=96.2)

if range_km > 0 and efficiency > 0:
    hydrogen_kg = range_km / efficiency
    st.success(f"남은 수소량은 약 {hydrogen_kg:.2f} kg 입니다.")
else:
    st.info("주행 거리와 연비를 입력해주세요.")
