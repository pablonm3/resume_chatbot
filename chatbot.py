from simpletransformers.conv_ai import ConvAIModel
#example: https://towardsdatascience.com/how-to-train-your-chatbot-with-simple-transformers-da25160859f4
from QA import find_answer
from conversation import chat

QA_TRESHOLD = 0.1


class Chatbot():
    def __init__(self):
        self.user_history_map = dict();

    def add_to_history(self, msg, answer, user_id):
        if(user_id not in self.user_history_map):
            self.user_history_map[user_id] = []
        self.user_history_map[user_id].append(msg)
        self.user_history_map[user_id].append(answer)


    def chat(self, user_id, msg=''):
        answer = find_answer(msg)
        print('answer from find_answer: ', answer)
        if(answer==None or answer["score"] < QA_TRESHOLD):
            if (user_id not in self.user_history_map):
                self.user_history_map[user_id] = []
            answer = chat(msg, self.user_history_map[user_id])
            print('answer from chat: ', answer)
        else:
            answer = answer["answer"]
        self.add_to_history(msg, answer, user_id)
        return answer