import streamlit as st

st.title("Unit Converter")
st.markdown("Converts units: Length, Mass, Time, Temperature, and Angle")

category = st.selectbox("Choose a category", ["Length", "Mass", "Time", "Temperature", "Angle"])

def convert_units(category, value, units): 
    if category == "Length":
        if units == "KM to Miles":
            return value * 0.621371
        elif units == "Miles to KM":
            return value / 0.621371
        elif units == "M to Inches":
            return value * 39.37008
        elif units == "Inches to M":
            return value / 39.37008
        elif units == "M to Feet":
            return value * 3.28084
        elif units == "Feet to M":
            return value / 3.28084
    elif category == "Mass":
        if units == "Kilograms to Pounds":
            return value * 2.20462
        elif units == "Pounds to Kilograms":
            return value / 2.20462
        elif units == "Grams to Ounces":
            return value * 0.035274
        elif units == "Ounces to Grams":
            return value / 0.035274
    elif category == "Time":
        if units == "Seconds to Minutes":
            return value / 60
        elif units == "Minutes to Seconds":
            return value * 60
        elif units == "Hours to Minutes":
            return value * 60
        elif units == "Minutes to Hours":
            return value / 60
        elif units == "Hours to Days":
            return value / 24
        elif units == "Days to Hours":
            return value * 24
    elif category == "Temperature":
        if units == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif units == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif units == "Celsius to Kelvin":
            return value + 273.15
        elif units == "Kelvin to Celsius":
            return value - 273.15
    elif category == "Angle":
        if units == "Degrees to Radians":
            return value * 3.141592653589793 / 180
        elif units == "Radians to Degrees":
            return value * 180 / 3.141592653589793

if category == "Length":
    units = st.selectbox("Choose a conversion", ["KM to Miles", "Miles to KM", "M to Inches", "Inches to M", "M to Feet", "Feet to M"])
elif category == "Mass":
    units = st.selectbox("Choose a conversion", ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Ounces", "Ounces to Grams"])
elif category == "Time":
    units = st.selectbox("Choose a conversion", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Minutes to Hours", "Hours to Days", "Days to Hours"])
elif category == "Temperature":
    units = st.selectbox("Choose a conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"])
elif category == "Angle":
    units = st.selectbox("Choose a conversion", ["Degrees to Radians", "Radians to Degrees"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    converted_value = convert_units(category, value, units)
    st.success(f"The result is {converted_value:.2f}")
