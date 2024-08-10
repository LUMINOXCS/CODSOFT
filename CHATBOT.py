def chatbot_response(user_input):
    user_input = user_input.lower()    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help!"
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm a simple chatbot created to assist you with basic queries."
    elif "time" in user_input:
        return "I'm unable to tell time, but your device should have a clock!"
    elif "weather" in user_input:
        return "I can't check the weather, but it might be sunny somewhere!"
    else:
        return "I'm not sure I understand. Could you try rephrasing that?"


if __name__ == "__main__":
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_message = input("You: ")
        if user_message.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_message)
        print("Chatbot:", response)
