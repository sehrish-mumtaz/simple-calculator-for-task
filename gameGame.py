import streamlit as st
import random

# Streamlit app title
st.title("Number Guessing Game")

# Define a function for the game logic
def play_game():
    # Set the range of the random number
    lower_limit = 1
    upper_limit = 100
    
    # Generate a random number
    if 'random_number' not in st.session_state:
        st.session_state.random_number = random.randint(lower_limit, upper_limit)
        st.session_state.attempts = 0  # Initialize attempts
        
    # Show instructions
    st.write(f"I'm thinking of a number between {lower_limit} and {upper_limit}. Can you guess it?")
    
    # User input for guess
    guess = st.number_input("Enter your guess", min_value=lower_limit, max_value=upper_limit, step=1)
    
    # Button to submit the guess
    if st.button("Submit Guess"):
        st.session_state.attempts += 1  # Increment the attempt counter
        
        # Check the guess and provide feedback
        if guess < st.session_state.random_number:
            st.write("Too low! Try again.")
        elif guess > st.session_state.random_number:
            st.write("Too high! Try again.")
        else:
            st.success(f"Congratulations! You guessed the number {st.session_state.random_number} correctly in {st.session_state.attempts} attempts.")
            if st.button("Play Again"):
                del st.session_state.random_number  # Reset the game
                del st.session_state.attempts

# Run the game
play_game()
