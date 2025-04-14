import streamlit as st


st.title("Simple BMI Calculator")

weight = st.number_input("Enter your weight (in kg):", min_value=1.0)


height = st.number_input("Enter your height (in cm):", min_value=50.0)


if st.button("Calculate BMI"):

    
    if height > 0:
       
        height_in_meters = height / 100

        
        bmi = weight / (height_in_meters ** 2)

       
        st.write(f"Your BMI is: **{bmi:.2f}**")

        if bmi < 18.5:
            st.info("You are underweight.")
        elif bmi < 25:
            st.success("You have a normal weight.")
        elif bmi < 30:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Height must be greater than 0.")


