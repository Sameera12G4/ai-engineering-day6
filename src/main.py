from dotenv import load_dotenv
import os
from calculator import add, subtract, multiply, divide
from text_analyzer import word_count, character_count, sentence_count
from text_analyzer import unique_word_count, most_common_word
print("AI Engineering Day 6")
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
text = "Python is easy. Python is powerful."
print("Word count:", word_count(text))
print("Character count:", character_count(text))
print("Sentence count:", sentence_count(text))
print("Unique word count:", unique_word_count(text))
print("Most common word:", most_common_word(text))
load_dotenv(".env")
app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")
print("App Name:", app_name)
print("API Key:", api_key)