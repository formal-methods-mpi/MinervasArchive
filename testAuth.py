import os
from langchain.llms import OpenAI
from langchain.chat_models import AzureChatOpenAI
exec(open('auth.py').read())
moderator = AzureChatOpenAI(request_timeout=60,temperature=0.1, model="moderator", deployment_name=os.getenv("OPENAI_MODERATOR_NAME"))
moderator.predict("hi!")
