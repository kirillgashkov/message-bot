"""
Contains models shared between other models.
"""

from typing import Dict, List


class Person:

    people = dict()

    def __init__(self, ids: Dict[str, str]):
        self.ids: Dict[str, str] = ids
        self.tags: List[str] = list()
        self.first_name: str = ''
        self.last_name: str = ''

    @classmethod
    def for_id(cls, domain, id):
        pair = (domain, id)
        if pair in cls.people:
            return cls.people[pair]
        person = Person({domain: id})
        cls.people[pair] = person
        return person


class Student(Person):

    def __init__(self, ids: Dict[str, str]):
        super().__init__(ids)
        self.list_number = None
        self.should_order = None
        self.should_order_default = None

    @classmethod
    def for_id(cls, domain, id):
        pair = (domain, id)
        if pair in cls.people:
            return cls.people[pair]
        person = Student({domain: id})
        cls.people[pair] = person
        return person
