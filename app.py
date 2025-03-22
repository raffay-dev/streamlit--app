import streamlit as st
st.title("My First Streamlit App")
st.write("Hello, Welcome to my Streamlit App!")

import streamlit as st
import random

st.title("🐍💦🔫 Snake Water Gun Game")

choices = {"snake": 1, "water": -1, "gun": 0}
reverse_dict = {1: "snake", -1: "water", 0: "gun"}

user_choice = st.radio("Choose one:", ["snake", "water", "gun"])
if st.button("Play"):
    computer_choice = random.choice(["snake", "water", "gun"])

    st.write(f"**You chose:** {user_choice}")
    st.write(f"**Computer chose:** {computer_choice}")

    if user_choice == computer_choice:
        st.success("It's a Draw!")
    elif (choices[user_choice] == 1 and choices[computer_choice] == -1) or \
         (choices[user_choice] == 0 and choices[computer_choice] == 1) or \
         (choices[user_choice] == -1 and choices[computer_choice] == 0):
        st.success("🎉 You Win!")
    else:
        st.error("😞 Computer Wins!")
