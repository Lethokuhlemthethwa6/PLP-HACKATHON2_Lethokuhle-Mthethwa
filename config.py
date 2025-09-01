import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "hackathon_secret")
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "yourpassword"
    MYSQL_DB = "mood_journal"
