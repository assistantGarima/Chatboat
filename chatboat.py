# Simple Python Chatbot

def chatbot():
    print("Hello! I'm a chatbot. Type 'quit' to end the conversation.")

    while True:
        # Get user input
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == 'quit':
            print("Goodbye! Have a great day!")
            break

        # Simple responses based on input
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a chatbot without a name. You can call me whatever you like!")
        elif "bye" in user_input:
            print("Chatbot: Bye! Take care!")
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")


# Run the chatbot
chatbot()
