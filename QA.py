from transformers import pipeline, AutoModel, AutoTokenizer, BertTokenizer, BertForQuestionAnswering
BERT_MODEL = "twmkn9/bert-base-uncased-squad2"
qa_bert_pipeline = pipeline('question-answering', model=BERT_MODEL, tokenizer=BERT_MODEL)


with open('personality.txt', 'r') as file:
    personality = file.read()
print("personality: ", personality)

def find_answers(questions=[]):
    responses = []
    for question in questions:
        responses.append(find_answer(question))
    return responses


def find_answer(question=""):
    try:
        return qa_bert_pipeline(context=personality, question=question)
    except Exception as e:
        print("QA exception: ", str(e))
        return None
