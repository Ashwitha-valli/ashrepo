import streamlit as st
import random

# Function to create the portfolio section
def create_portfolio():
    st.title("My Portfolio")
    st.header("Hello, I'm ASHWITHA K!")
    st.write("Welcome to my personal portfolio. Here are a few details about me:")
    
    
    st.subheader("About Me")
    st.write("""
        I am passionate about coding
    """)
    
    st.subheader("Skills & Expertise")
    st.write("""
        - Python
        
    """)
    
    st.subheader("Connect with me!")
    st.write("""
        You can reach me at:
        - Email: ashwitha437@gmail.com
    """)

# Function to handle the user guessing game logic
def user_guessing_game():
    st.header("User Guessing Game")
    st.write("""
        In this game, you will try to guess a number that the machine has picked.
        The machine will give you feedback on whether your guess is too high or too low.
    """)
    
    # Set dynamic range for guessing
    low = st.slider("Select the lowest number", min_value=1, max_value=100, value=1)
    high = st.slider("Select the highest number", min_value=low + 1, max_value=200, value=100)
    
    # Generate the random number and save it in session state
    if "number_to_guess" not in st.session_state:
        st.session_state.number_to_guess = random.randint(low, high)
    
    # Track attempts
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    
    st.write(f"Guess a number between {low} and {high}.")
    
    # Handle the guess input
    guess = st.number_input("Your guess:", min_value=low, max_value=high, step=1, key="user_guess_input")
    
    if guess:
        st.session_state.attempts += 1  # Increase attempt count
        if guess < st.session_state.number_to_guess:
            st.write("Too low! Try again.")
        elif guess > st.session_state.number_to_guess:
            st.write("Too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed the correct number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts.")
            # Reset after correct guess
            del st.session_state.number_to_guess
            del st.session_state.attempts

    # Button to reset the game
    if st.button("Start New Game"):
        del st.session_state.number_to_guess
        del st.session_state.attempts

# Function for the machine guessing game logic
def machine_guessing_game():
    st.header("Machine Guessing Game")
    st.write("""
        In this game, the machine will try to guess the number you are thinking of.
        The machine will ask you whether its guess is too high, too low, or correct.
    """)
    
    # Set dynamic range for guessing
    low = st.slider("Select the lowest number", min_value=1, max_value=100, value=1)
    high = st.slider("Select the highest number", min_value=low + 1, max_value=200, value=100)
    
    st.write(f"Think of a number between {low} and {high}, and the machine will try to guess it.")
    
    # Binary search for optimal guesses
    attempts = 0
    while low <= high:
        guess = (low + high) // 2
        st.write(f"Machine guesses: {guess}")
        
        feedback = st.radio("Is the guess correct?", ("Correct", "Too low", "Too high"), key=f"machine_guess_feedback_{attempts}")
        
        attempts += 1
        
        if feedback == "Correct":
            st.write(f"Machine guessed your number {guess} in {attempts} attempts.")
            break
        elif feedback == "Too low":
            low = guess + 1
        elif feedback == "Too high":
            high = guess - 1

# Main function to control the flow of the app
def main():
    st.title("Streamlit Portfolio and Guessing Game")
    
    # Sidebar for navigation
    menu = ["Portfolio", "User Guessing Game", "Machine Guessing Game"]
    choice = st.sidebar.selectbox("Select an option", menu)
    
    if choice == "Portfolio":
        create_portfolio()
    elif choice == "User Guessing Game":
        user_guessing_game()
    elif choice == "Machine Guessing Game":
        machine_guessing_game()

if __name__ == "__main__":
    main()
