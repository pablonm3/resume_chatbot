import unittest
from QA import find_answers
from conversation import chat
from chatbot import Chatbot


class MyTestCase(unittest.TestCase):
    def test_QA(self):
        questions = ["How old are you?", "what do you do?", "how do you see yourself in 5 years",
                     "Tell me about yourself", "what do you like?", "What are your biggest strengths?",
                     "why should we hire you?", "What do you consider to be your biggest professional achievement?",
                     "Describe your dream job.", "What kind of work environment do you like best?",
                     "Tell me how you think other people would describe you", "what is your biggest weakness?",
                     "What do you like to do outside of work?",
                     "What questions do you have for me?"]
        result = find_answers(questions)
        print("result: ", result)
        self.assertEqual(len(questions), len(result))

    def test_chatbot_nohistory(self):
        result = chat("hi")
        print("result: ", result)
        #self.assertEqual(len(questions), len(result))


    def test_chatbot_history(self):
        history = ['I am 25 years old', 'my name is pablo', 'I love pancakes', 'I live in USA']
        result = chat("how old am I?", history)
        print("result: ", result)
        result = chat("what's my name?", history)
        print("result: ", result)
        result = chat("what's mi favourite food?", history)
        print("result: ", result)
        result = chat("where do I live?", history)
        print("result: ", result)
        #self.assertEqual(len(questions), len(result))

    def test_app(self):
        USER_ID = "key1"
        chatbot = Chatbot()
        print(chatbot.chat(USER_ID, 'I love Pizza'))
        print(chatbot.chat(USER_ID, 'what do I like?'))
        print(chatbot.chat(USER_ID, 'whats my favorite food?'))


if __name__ == '__main__':
    unittest.main()
