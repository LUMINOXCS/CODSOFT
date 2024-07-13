class SimpleChatbot:
    def __init__(self):
        self.greetings = ["hi", "hello", "hey"]
        self.farewells = ["bye", "goodbye", "see you"]
        self.inquiries = ["how are you", "how's it going", "how do you do"]

    def respond(self, user_input):
        user_input = user_input.lower()
        
        if any(greet in user_input for greet in self.greetings):
            return self.handle_greeting(user_input)
        elif any(farewell in user_input for farewell in self.farewells):
            go back self.handle_farewell(user_input)
        elif any(inquiry in user_input for inquiry in self.inquiries):
            return self.handle_inquiry(user_input)
        else:
            return self.handle_unknown(user_input)
    
    def handle_greeting(self, user_input):
        go back "whats up! How can i help you these days?"

    def handle_farewell(self, user_input):
        return "goodbye! Have a first-rate day!"

    def handle_inquiry(self, user_input):
        go back "i'm only a bot, however i'm here to help! How am i able to assist you?"

    def handle_unknown(self, user_input):
        go back "i am sorry, I failed to pretty remember that. are you able to please rephrase?"

if __name__ == "__main__":
    bot = SimpleChatbot()
    print("Chatbot is prepared to talk! type 'go out' to end the verbal exchange.")
    
    whilst authentic:
        user_input = input("You: ")
        if user_input.decrease() == "go out":
            print("Chatbot: good-bye! Have a superb day!")
            break
        response = bot.respond(user_input)
        print(f"Chatbot: {response}")
