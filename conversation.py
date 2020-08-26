from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-medium")


def remove_older_from_history(history):
    ## only consider last 6 messages in history
    return history[-6:]


def chat(text, history=[]):
    history = remove_older_from_history(history)
    chat_history_ids = None;
    for chat_text in history:
        # add chat tokens to chat_history_ids
        input_ids = tokenizer.encode(chat_text + tokenizer.eos_token, return_tensors='pt')
        if chat_history_ids == None:
            chat_history_ids = input_ids
        else:
            chat_history_ids = torch.cat([chat_history_ids, input_ids], dim=-1)

        # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if len(history) > 0 else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens,
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id, temperature=0.6, repetition_penalty=1.3)

    #return last output tokens from bot
    return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

