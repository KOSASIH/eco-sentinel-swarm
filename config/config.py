import os
import json

class Config:
    def __init__(self):
        self.config = self.load_config()
        self.secrets = self.load_secrets()

    def load_config(self):
        with open('config.json', 'r') as f:
            return json.load(f)

    def load_secrets(self):
        with open('secrets.json', 'r') as f:
            return json.load(f)

    def get(self, key):
        return self.config.get(key) or self.secrets.get(key)
