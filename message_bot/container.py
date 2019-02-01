"""
Provides access to shared objects.
"""

from typing import Dict

from message_bot import models


#
# Person
#


_people: Dict[str, models.Person] = dict()


def person_for_id(identifier: str) -> models.Person:
    if identifier not in _people:
        _people[identifier] = models.Person(identifier)
    return _people[identifier]
