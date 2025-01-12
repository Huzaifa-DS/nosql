from pymongo import MongoClient
from datetime import datetime

class MongoDBManager:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
    
    def log_action(self, user, action, recommendations):
        log_entry = {
            "user": user,
            "action": action,
            "recommendations": recommendations,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.db.user_logs.insert_one(log_entry)
    
    def get_logs(self):
        return list(self.db.user_logs.find())
