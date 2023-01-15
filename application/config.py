import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config():
  DEBUG=True
  DATABASE = os.path.join(BASE_DIR, "../database.db")
  SECRET_KEY = 'hjdfhhjdijmcvkjesikhj'