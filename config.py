import os

class Config:
    SECRET_KEY = os.environ.get('KEY') or 'guess'