"""
Provides API for accessing database with people.
"""

from typing import Optional

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


def get_person_by_id(identifier: str) -> models.Person:
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


_student_identifiers = dict()


def _initialize_student_identifiers():
    table = engine.read_all()

    student_identifiers = dict()
    for identifier, fields in table.items():
        list_number = fields['list_number']
        if list_number is None:
            continue
        student_identifiers[list_number] = identifier

    global _student_identifiers
    _student_identifiers = student_identifiers


def get_student_by_listnum(listnum: int) -> Optional[models.Person]:
    if not _student_identifiers:
        _initialize_student_identifiers()
    identifier = _student_identifiers.get(listnum)

    if identifier is None:
        return None

    return get_person_by_id(identifier)
