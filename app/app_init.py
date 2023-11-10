from flask import Flask
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


app = Flask(__name__, template_folder="../templates", static_folder="../static")
