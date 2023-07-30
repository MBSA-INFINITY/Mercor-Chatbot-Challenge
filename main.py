import textbase
from textbase.message import Message
from textbase import models
from langchain.llms import OpenAI
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
import os
from typing import List

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
# Load your OpenAI API key
models.OpenAI.api_key = OPENAI_API_KEY
# models.OpenAI.api_key = "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"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like. The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a pleasant chat!
"""

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

total_user_balance = 0
@textbase.chatbot("talking-bot")
def on_message(message):
    global total_user_balance
    print(total_user_balance)
    result = llm_chain.run(message) 
    result = result.lower().split("\n")
    result = [x for x in result if x != ""]
    result = [x.split(":")[1].strip() for x in result if x != ""]
    print(result)
    if len(result) == 4:
        source = result[0]
        amount = int(result[2])
        credit = True if result[1] == "credit" else False
        if source == "statement":
            result = f"Your previous balance was {total_user_balance}. "
            if credit:
                total_user_balance+=amount
            else:
                total_user_balance-=amount
            result += f"Your Total Balnce now is {total_user_balance}."
        else:
            new_query = f"My current balance is {total_user_balance}. {message}"
            result = llm_chain.run(new_query) 
    return result
