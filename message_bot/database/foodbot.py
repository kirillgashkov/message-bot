"""
Provides API for accessing foodbot's database.
"""

import datetime
from typing import Optional, Dict

from message_bot import database, models
from message_bot.constants import DATE_FORMAT


#
# Engines
#


engine: database.engines.BaseEngine


def set_engine(new_engine: database.engines.BaseEngine):
    global engine
    engine = new_engine


#
# API
#


def set_eating_default(person: models.Person, new_default: bool):
    engine.update(person.id, {'eating_default': str(new_default)})


def set_eating(
        person: models.Person,
        date: datetime.date,
        new_value: Optional[bool]
        ):
    date_as_str = date.strftime(DATE_FORMAT)
    value_as_str = str(new_value).upper() if new_value is not None else ''
    engine.update(person.id, {date_as_str: value_as_str})


def get_eatings(
        date: datetime.date
        ) -> Dict[models.Person, Optional[bool]]:
    date_as_str = date.strftime(DATE_FORMAT)
    table = engine.read_all()

    eatings = dict()
    for student_id, fields in table.items():
        value = string_to_bool(fields.get(date_as_str))
        if value is not None:
            eating = value
        else:
            default = fields.get('eating_default')
            eating = string_to_bool(default)
        student = database.people.get_person_by_id(student_id)
        eatings[student] = eating

    return eatings


#
# Utilities
#


def string_to_bool(s) -> Optional[bool]:
    if s == 'TRUE':
        return True
    elif s == 'FALSE':
        return False
    else:
        return None
