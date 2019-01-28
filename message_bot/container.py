"""
Provides access to shared objects.
"""

from typing import Dict, Tuple

from message_bot import models


#
# Person
#


_people: Dict[Tuple[str, str], models.Person] = dict()


def person_for_id(name: str, identifier: str) -> models.Person:
    key = name, identifier
    if key not in _people:
        _people[key] = models.Person({name: identifier})
    return _people[key]
