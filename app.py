
import streamlit as st
import statistics

st.title("Statistical Calculator")

data = st.text_input(
    "Enter numbers separated by commas",
    "10, 12, 15, 18, 20, 25"
)

if st.button("Calculate"):
    try:
        numbers = [float(x.strip()) for x in data.split(",")]

        st.metric("Mean", round(statistics.mean(numbers), 2))
        st.metric("Median", round(statistics.median(numbers), 2))

        if len(numbers) > 1:
            st.metric(
                "Standard deviation",
                round(statistics.stdev(numbers), 2)
            )
    except ValueError:
        st.error("Please enter valid numbers.")
