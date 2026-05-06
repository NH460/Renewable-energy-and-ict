import streamlit as st

# Title
st.title("🌱 Renewable Energy & ICT Dashboard")

st.write("This app estimates solar energy generation and monitors energy usage.")

# Sidebar inputs
st.sidebar.header("User Input Parameters")

area = st.sidebar.number_input("Solar Panel Area (m²)", min_value=1.0, value=10.0)
efficiency = st.sidebar.slider("Panel Efficiency (%)", 10, 30, 20)
sunlight_hours = st.sidebar.number_input("Sunlight Hours per Day", min_value=1.0, value=5.0)

# Constants
solar_irradiance = 1000  # W/m² (standard)

# Calculation
power_output = area * (efficiency / 100) * solar_irradiance  # Watts
daily_energy = power_output * sunlight_hours / 1000  # kWh

# Output
st.subheader("🔋 Energy Output")
st.write(f"Estimated Power Output: **{power_output:.2f} W**")
st.write(f"Estimated Daily Energy Generation: **{daily_energy:.2f} kWh**")

# Energy usage monitoring
st.subheader("🏠 Energy Consumption Tracker")

appliance = st.text_input("Appliance Name")
usage_hours = st.number_input("Usage Hours per Day", min_value=0.0, value=1.0)
appliance_power = st.number_input("Appliance Power (W)", min_value=1.0, value=100.0)

if st.button("Calculate Consumption"):
    consumption = (appliance_power * usage_hours) / 1000
    st.success(f"Daily Energy Consumption for {appliance}: {consumption:.2f} kWh")

# ICT Feature: Data Logging (simple simulation)
st.subheader("📡 ICT Data Log (Simulation)")

if st.button("Log Data"):
    st.info("Data logged successfully! (Simulated IoT integration)")

# Footer
st.write("---")
st.write("Developed for Renewable Energy & ICT Project")
