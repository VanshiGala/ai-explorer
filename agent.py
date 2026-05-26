import os
import google.generativeai as genai
from dotenv import load_dotenv
from search import search_web

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

async def run_agent(query):

    web_result = search_web(query)

    prompt = f"""
    User asked:

    {query}

    Search result:

    {web_result}

    Return useful answer.
    """

    response = model.generate_content(
        prompt
    )

    return response.text