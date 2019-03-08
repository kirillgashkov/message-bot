"""
Contains utility functions and classes shared between other database submodules.
"""

import collections


class DatabaseView(collections.Mapping):

    def __init__(self, data: dict):
        self._data = data

    def __getitem__(self, key):
        item = self._data[key]

        if type(item) is dict:
            return DatabaseView(item)

        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)
