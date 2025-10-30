import streamlit as st

st.title("넥쏘 수소량 계산기")

distance = st.number_input("남은 주행 가능 거리 (km)", min_value=0.0, step=1.0)
efficiency = st.number_input("복합 연비 (km/kg)", value=107.0, min_value=1.0, step=0.1)
tank_capacity = 6.0

if distance > 0 and efficiency > 0:
    hydrogen_kg = distance / efficiency
    hydrogen_percent = (hydrogen_kg / tank_capacity) * 100

    st.metric(label="남은 수소량 (kg)", value=f"{hydrogen_kg:.2f} kg")
    st.metric(label="잔여 수소 비율 (%)", value=f"{hydrogen_percent:.1f}%")
else:
    st.info("주행 거리와 연비를 입력하면 수소량을 계산합니다.")