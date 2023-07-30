import textbase
from textbase.message import Message
from fastapi import HTTPException
from textbase import models
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from helpers import get_total_user_balance, update_total_user_balance, parse_llm_result
import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
models.OpenAI.api_key = OPENAI_API_KEY
llm = OpenAI(openai_api_key=OPENAI_API_KEY)


template = """think of this statement "{statement}" as a transaction and give me whether this is a statement/question , the amount, reason and whether it was credit/debit in the following format
source:  statement/question
Credit/Debit: 
Amount:
Reason:
"""
prompt = PromptTemplate(template=template, input_variables=["statement"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

question_template = """{question}"""
question_prompt = PromptTemplate(template=question_template, input_variables=["question"])
question_llm_chain = LLMChain(prompt=question_prompt, llm=llm)

@textbase.chatbot("talking-bot")
def on_message(message):
    total_user_balance = get_total_user_balance()
    result = llm_chain.run(message) 
    result = parse_llm_result(result)
    print(result)
    if len(result) == 4:
        source = result[0]
        credit = True if result[1] == "credit" else False
        if source == "statement":
            amount = int(result[2])
            result = f"Your previous balance was {total_user_balance}. "
            if credit:
                update_total_user_balance(amount)
                total_user_balance+=amount
            else:
                update_total_user_balance(amount)
                total_user_balance-=amount
            result += f"Your Total Balnce now is {total_user_balance}."
        else:
            new_query = f"{message.content}. My current balance is {total_user_balance}. Give answer in one line!"
            print("new_query: ", new_query)
            return question_llm_chain.run(new_query) 
    else:
        raise HTTPException(status_code=500, detail=f"Server Error: Couldn't parse the result!")
    return result
