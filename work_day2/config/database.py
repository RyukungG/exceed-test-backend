import os
import urllib

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv('.env')

userexceed = os.getenv('userexceed')
password = os.getenv('password')
print(password)

client = MongoClient(f"mongodb://{userexceed}:{password}@mongo.exceed19.online:8443/?authMechanism=DEFAULT")
db = client['exceed11']