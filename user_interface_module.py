class UserInterface:
    def welcome(self):
        print("Welcome to Mindmap AI - Adaptive Intelligence System")
        print("Ask anything or type 'exit' to quit.")

    def get_user_input(self):
        return input("You: ")

    def respond(self, response):
        print(f"AI: {response}")