{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNRUV6NgjIYX3sjRw9j3U+R",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sehrish-mumtaz/simple-calculator-for-task/blob/main/Game.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import random\n",
        "\n",
        "# Streamlit app title\n",
        "st.title(\"Number Guessing Game\")\n",
        "\n",
        "# Define a function for the game logic\n",
        "def play_game():\n",
        "    # Set the range of the random number\n",
        "    lower_limit = 1\n",
        "    upper_limit = 100\n",
        "\n",
        "    # Generate a random number\n",
        "    if 'random_number' not in st.session_state:\n",
        "        st.session_state.random_number = random.randint(lower_limit, upper_limit)\n",
        "        st.session_state.attempts = 0  # Initialize attempts\n",
        "\n",
        "    # Show instructions\n",
        "    st.write(f\"I'm thinking of a number between {lower_limit} and {upper_limit}. Can you guess it?\")\n",
        "\n",
        "    # User input for guess\n",
        "    guess = st.number_input(\"Enter your guess\", min_value=lower_limit, max_value=upper_limit, step=1)\n",
        "\n",
        "    # Button to submit the guess\n",
        "    if st.button(\"Submit Guess\"):\n",
        "        st.session_state.attempts += 1  # Increment the attempt counter\n",
        "\n",
        "        # Check the guess and provide feedback\n",
        "        if guess < st.session_state.random_number:\n",
        "            st.write(\"Too low! Try again.\")\n",
        "        elif guess > st.session_state.random_number:\n",
        "            st.write(\"Too high! Try again.\")\n",
        "        else:\n",
        "            st.success(f\"Congratulations! You guessed the number {st.session_state.random_number} correctly in {st.session_state.attempts} attempts.\")\n",
        "            if st.button(\"Play Again\"):\n",
        "                del st.session_state.random_number  # Reset the game\n",
        "                del st.session_state.attempts\n",
        "\n",
        "# Run the game\n",
        "play_game()\n"
      ],
      "metadata": {
        "id": "HCViRpEBfV4D"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}