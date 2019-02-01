"""
Provides API for accessing foodbot's database.
"""

import datetime
from typing import Dict, List

from message_bot import database, models
from message_bot.constants import DATE_FORMAT


#
# Engines
#


people_engine: database.engines.BaseEngine
students_engine: database.engines.BaseEngine


def set_people_engine(new_engine: database.engines.BaseEngine):
    global people_engine
    people_engine = new_engine


def set_students_engine(new_engine: database.engines.BaseEngine):
    global students_engine
    students_engine = new_engine


#
# API
#


def tags_of(person: models.Person) -> List[str]:
    tags = people_engine.read(person.id)['tags']
    return tags.split(',')


def metadata_of(student: models.Student) -> Dict[str, str]:
    return students_engine.read(student.id)


def update_student(student: models.Student):
    date = datetime.date.today().strftime(DATE_FORMAT)
    updated_fields = {
        'eating_default': f'{student.eating_default}',
        date: f'{student.is_eating}',
    }
    students_engine.update(student.id, updated_fields)
