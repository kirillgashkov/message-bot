"""
Database engine will use local JSON file.
"""

import os.path
import json

from message_bot import database


class JSONEngine(database.engines.BaseEngine):

    def __init__(self, fp: str):
        super().__init__()
        self.filepath = fp
        self.pull()

    def push(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.table, f)

    def pull(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                new_table = json.load(f)
        else:
            new_table = dict()
        self.table = new_table
