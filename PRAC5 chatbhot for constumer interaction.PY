# develop a chatbot for any suitable customer interaction application
# All code is commented as it contains 2 code chatbot 1 and 2 so as per your choice uncomment any one code and run..
# Chatbot 1
'''import re
import random

# Predefined responses
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?"],
    "goodbye": ["Goodbye! Have a great day!", "Thanks for visiting. Take care!"],
    "thanks": ["You're welcome!", "Glad I could help!"],
    "hours": ["We are open from 9 AM to 6 PM, Monday to Friday."],
    "location": ["Our store is located at 123 Main Street, Downtown."],
    "order_status": ["Please provide your order ID to check the status."],
    "default": ["I'm not sure I understand. Could you please rephrase?"]
}

# Patterns to recognize
patterns = {
    "greeting": re.compile(r"\b(hello|hi|hey)\b", re.I),
    "goodbye": re.compile(r"\b(bye|goodbye|see you)\b", re.I),
    "thanks": re.compile(r"\b(thank you|thanks|thx)\b", re.I),
    "hours": re.compile(r"\b(hours|open|closing)\b", re.I),
    "location": re.compile(r"\b(location|where|address)\b", re.I),
    "order_status": re.compile(r"\b(order|status|track)\b", re.I),
}

# Function to get response
def get_response(user_input):
    for intent, pattern in patterns.items():
        if pattern.search(user_input):
            return random.choice(responses[intent])
    return random.choice(responses["default"])

# Function to run chatbot
def run_chatbot():
    print("Welcome to HelpBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit", "bye"):
            print("Bot:", random.choice(responses["goodbye"]))
            break
        response = get_response(user_input)
        print("Bot:", response)

# Main entry point
if __name__ == "__main__":
    run_chatbot()'''

# Chatbot 2
import random
import time
from datetime import datetime, timedelta


class ElementaryChatbot:
    def __init__(self):
        self.name = "HelpBot"
        self.responses = {
            "greeting": [
                "Hello! Welcome to our customer service. How can I help you today?",
                "Hi there! How can I assist you?",
                "Greetings! What can I do for you today?"
            ],
            "farewell": [
                "Thank you for contacting us. Have a great day!",
                "Goodbye! Don't hesitate to reach out if you have more questions.",
                "Have a wonderful day! Come back anytime."
            ],
            "help": [
                "I can help with order status, returns, product information, and general questions.",
                "I can assist with tracking orders, processing returns, or answering product questions.",
                "My expertise includes order inquiries, refunds, and general customer support."
            ],
            "order_status": [
                "To check your order status, please provide your order number.",
                "I can look up your order status if you share your order ID.",
                "For order status, I'll need your order reference number."
            ],
            "return": [
                "Our return policy allows returns within 30 days of purchase. Would you like to start a return?",
                "You can initiate returns within 30 days. Do you need help with a return?",
                "Returns are accepted within a month of delivery. Need assistance with a return?"
            ],
            "product_info": [
                "I can provide information about our products. What would you like to know?",
                "What product are you interested in learning about?",
                "I can give you details about any of our products. Which one interests you?"
            ],
            "default": [
                "I'm not sure I understand. Could you rephrase that?",
                "I didn't quite get that. Can you ask in a different way?",
                "I'm still learning. Could you try asking that differently?"
            ]
        }

        self.order_status_db = {
            "ORD123": "Shipped - Expected delivery on " + (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d"),
            "ORD456": "Processing - Should ship within 2 business days",
            "ORD789": "Delivered on " + (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
        }

        self.products_db = {
            "laptop": "We have premium laptops with 16GB RAM, 1TB SSD, and 2-year warranty starting at $999.",
            "phone": "Our latest smartphones feature 5G, 128GB storage, and 48MP cameras starting at $699.",
            "headphones": "Noise-cancelling headphones with 30-hour battery life available for $199."
        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        if any(word in user_input for word in ["hi", "hello", "hey", "greetings"]):
            return random.choice(self.responses["greeting"])
        elif any(word in user_input for word in ["bye", "goodbye", "see you", "exit"]):
            return random.choice(self.responses["farewell"])
        elif any(word in user_input for word in ["help", "support", "assistance"]):
            return random.choice(self.responses["help"])
        elif any(word in user_input for word in ["order", "status", "track"]):
            return random.choice(self.responses["order_status"])
        elif any(word in user_input for word in ["return", "refund", "exchange"]):
            return random.choice(self.responses["return"])
        elif any(word in user_input for word in ["product", "item", "info", "spec"]):
            return random.choice(self.responses["product_info"])
        elif any(word in user_input for word in ["thank", "thanks", "appreciate"]):
            return "You're welcome! Is there anything else I can help with?"
        elif any(word in user_input for word in ["time", "date", "day"]):
            return f"The current time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        else:
            # Check for order number pattern
            if "ord" in user_input:
                for order_num in self.order_status_db:
                    if order_num.lower() in user_input:
                        return f"Order {order_num}: {self.order_status_db[order_num]}"

            # Check for product inquiries
            for product in self.products_db:
                if product in user_input:
                    return self.products_db[product]

            return random.choice(self.responses["default"])

    def chat(self):
        print(f"{self.name}: {random.choice(self.responses['greeting'])}")

        while True:
            user_input = input("You: ")

            if user_input.lower() in ['quit', 'exit', 'bye']:
                print(f"{self.name}: {random.choice(self.responses['farewell'])}")
                break

            response = self.get_response(user_input)

            # Simulate typing delay for more natural interaction
            print(f"{self.name} is typing...", end='\r')
            time.sleep(random.uniform(0.5, 1.5))
            print(f"{self.name}: {response}")


if __name__ == "__main__":
    bot = ElementaryChatbot()
    bot.chat()
