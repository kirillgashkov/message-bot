"""
Provides API for accessing database with people.
"""

from message_bot import models, database
from message_bot.models.person import TAG_STRANGER


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


def get_person(identifier: str) -> models.Person:
    if identifier in _people:
        return _people[identifier]

    raw_fields = engine.read(identifier)
    if raw_fields is None:
        new_person = models.Person(identifier, {TAG_STRANGER}, dict())
    else:
        fields = dict(raw_fields)
        tags = fields.pop('tags')
        new_person = models.Person(identifier, set(tags.split(',')), fields)

    _people[identifier] = new_person
    return new_person
