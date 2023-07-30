from db import users_collection
from fastapi import HTTPException

def get_total_user_balance():
    if user_details := users_collection.find_one({"user_id": "local"},{"_id": 0}):
        total_user_balance = user_details.get("amount")
    else:
        total_user_balance = 0
    return total_user_balance

def update_total_user_balance(amount):
    try:
        users_collection.update_one({"user_id": "local"},{"$inc":{"amount": amount}})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB Error: {str(e)}")
    
def parse_llm_result(result):
    result = result.lower().split("\n")
    result = [x for x in result if x != ""]
    result = [x.split(":")[1].strip() for x in result if x != ""]
    return result