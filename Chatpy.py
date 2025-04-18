import random
import time
from datetime import datetime

# Function to simulate wave-like typing effect
def typing_wave(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.035)  # Slower for that 'wave' feel
    print()

# Chatbot predefined responses
responses = {
    "hi": ["Hello there! 👋", "Hi! How can I assist you?", "Hey, good to see you!"],
    "how are you": ["I'm great, thanks for asking! And you?", "Doing awesome — I'm a chatbot after all!"],
    "what is your name": ["I'm PyBuddy — your friendly Python chatbot!", "Call me PyBuddy! 🤖"],
    "time": [f"The current time is {datetime.now().strftime('%H:%M:%S')}."],
    "date": [f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐞",
        "Why did the computer get cold? It forgot to close its Windows! 😂",
        "Why do Java developers wear glasses? Because they don't C#! 🤓"
    ],
    "bye": ["Goodbye! See you next time! 👋", "Bye! Have a great day!"],
    "help": [
        "You can chat with me using: 'hi', 'how are you', 'time', 'date', 'joke', 'bye'."
    ]
}

# Function to get chatbot response
def get_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "Oops! I didn't get that. Type 'help' to see what you can ask me!"

# Main chat loop
def main():
    typing_wave("PyBuddy: Hello! I'm PyBuddy — your Python chatbot. Type 'help' to see what I can do!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            typing_wave("PyBuddy: Bye! Have a wonderful day! 👋")
            break
        response = get_response(user_input)
        typing_wave("PyBuddy: " + response)

# Run the chatbot
if __name__ == "__main__":
    main()
