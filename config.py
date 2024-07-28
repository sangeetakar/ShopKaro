from dotenv import load_dotenv
import os
from app import app

load_dotenv()  #to load contents of .env file

app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
# ABOVE codes to get every info from .env