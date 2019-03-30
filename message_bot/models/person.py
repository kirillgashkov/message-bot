"""
An object that holds person's ID, tags and optionally fields.
"""

import dataclasses
from typing import Set, Dict, Any


@dataclasses.dataclass
class Person:
    id: str
    tags: Set[str]
    fields: Dict[str, Any]

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


#
# Tags
#


TAG_STRANGER = 'STRANGER'
