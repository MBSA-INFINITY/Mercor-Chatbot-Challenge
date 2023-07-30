# BudgetGPT (A Budgeting AI ChatBot)
**An Example!**
![image](https://github.com/MBSA-INFINITY/Mercor-Chatbot-Challenge/assets/85332648/de335ae7-f1da-4844-96dc-25192bc64496)

**What is my current balance?**
![image](https://github.com/MBSA-INFINITY/Mercor-Chatbot-Challenge/assets/85332648/c094bfb9-2153-470a-8fc5-474c1807fd2d)

## Steps to run the project in local
- Setup an local MongoDB database named `budgetgpt` and default collection  as `user_details`.

![image](https://github.com/MBSA-INFINITY/Mercor-Chatbot-Challenge/assets/85332648/27c8ca45-3f1c-4904-b249-5abcef472cf3)

- Add a document in that collection same as follows:-

![image](https://github.com/MBSA-INFINITY/Mercor-Chatbot-Challenge/assets/85332648/3000584a-4904-4faf-9d58-9291b06b0a66)

- Create an .env file main directory and Set the **OPENAI_API_KEY** in the `.env` file of the codebase as follow:-
  `export OPENAI_API_KEY = "YOUR_API_KEY"`

- Finally, Run the following command:

```bash
./start_server.sh
```

Now go to [http://localhost:4000](http://localhost:4000) and start chatting with your BudgetGPT! The BudgetGPT will automatically reload when you change the code.


