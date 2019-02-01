"""
Provides API for accessing database with people.
"""

from message_bot import models, database
from message_bot.constants import TAG_STRANGER


#
# Engine
#


engine: database.engines.BaseEngine


def set_engine(new_engine: database.engines.BaseEngine):
    global engine
    engine = new_engine


#
# API
#


_people = dict()


def person(identifier: str) -> models.Person:
    if identifier not in _people:
        fields = engine.read(identifier)
        if fields is None:
            new_person = models.Person(identifier, [TAG_STRANGER], dict())
        else:
            tags = fields.pop('tags')
            new_person = models.Person(identifier, tags.split(','), fields)
        _people[identifier] = new_person
    return _people[identifier]
