from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from collections import namedtuple
import os

Config = namedtuple("Config", ["api_key"])

class Api:
    def __init__(self):
        load_dotenv()
        self.api_key = Config(os.getenv("OPENAI_API_KEY"))