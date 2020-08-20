"""
Author: Rakesh Yadav
Aim: To make a conversational chatbot by using ML, NLTK & tkinter
        through python.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat-bot named as TechnoBot
chatbot = ChatBot('TechnoBot')

listOfTrainingQueries = ["hello! What is your name?",
                         "My name is TechnoBot and I am a bot.",
                         "Hi, How can I help you?",
                         "I am fine!, What about you?",
                         "Oops! I Don't understand your query...   "
                         ]

trainer = ListTrainer(chatbot)
trainer.train(listOfTrainingQueries)

print("\n ***************##############*******************\n\t....... YOU ARE TALKING TO TECHNOBOT .........\n\n")

while True:
    query = input()
    if query == "exit":
        break
    bot_response = chatbot.get_response(query)
    print("Bot: ", bot_response)
