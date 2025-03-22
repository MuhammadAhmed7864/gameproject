import streamlit as st
import random

# Apply custom CSS styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .main {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .stTextInput>div>div>input, .stNumberInput>div>div>input {
            border-radius: 10px;
            border: 1px solid #ccc;
            padding: 10px;
        }
        .stButton>button {
            background-color: #007BFF;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .success {
            color: green;
            font-size: 18px;
            font-weight: bold;
        }
        .error {
            color: red;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state variables
if "target_number" not in st.session_state:
    st.session_state.target_number = None
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "max_attempts" not in st.session_state:
    st.session_state.max_attempts = None
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("🎯 Number Guessing Game")

# Allow user to set a custom range
st.subheader("🔢 Set the Range")
min_value = st.number_input("Minimum Value", value=1, step=1, min_value=1)
max_value = st.number_input("Maximum Value", value=100, step=1, min_value=min_value + 1)

# Select difficulty level
st.subheader("🎮 Choose Difficulty Level")
difficulty = st.radio("Select difficulty", ("Easy (Unlimited)", "Medium (10 tries)", "Hard (5 tries)"))

if difficulty == "Easy (Unlimited)":
    st.session_state.max_attempts = None
elif difficulty == "Medium (10 tries)":
    st.session_state.max_attempts = 10
elif difficulty == "Hard (5 tries)":
    st.session_state.max_attempts = 5

# Start the game
if st.button("🚀 Start Game"):
    st.session_state.target_number = random.randint(min_value, max_value)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.success(f"Game started! Guess a number between {min_value} and {max_value}.")

# Game logic
if st.session_state.target_number is not None and not st.session_state.game_over:
    user_guess = st.number_input("🔍 Enter your guess:", min_value=min_value, max_value=max_value, step=1)

    if st.button("✅ Submit Guess"):
        st.session_state.attempts += 1

        if user_guess < st.session_state.target_number:
            st.warning("📉 Too low! Try again.")
        elif user_guess > st.session_state.target_number:
            st.warning("📈 Too high! Try again.")
        else:
            st.markdown("<p class='success'>🎉 Congratulations! You guessed the number in {}</p>".format(st.session_state.attempts), unsafe_allow_html=True)
            st.session_state.game_over = True

        # Check if attempts exceeded for difficulty mode
        if st.session_state.max_attempts is not None and st.session_state.attempts >= st.session_state.max_attempts:
            st.markdown(f"<p class='error'>❌ Game Over! The correct number was {st.session_state.target_number}. Try again!</p>", unsafe_allow_html=True)
            st.session_state.game_over = True

# Reset game
if st.button("🔄 Reset Game"):
    st.session_state.target_number = None
    st.session_state.attempts = 0
    st.session_state.max_attempts = None
    st.session_state.game_over = False
    st.experimental_rerun()

st.markdown("</div>", unsafe_allow_html=True)
