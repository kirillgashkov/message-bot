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


#
# Tags
#


TAG_STRANGER = 'STRANGER'
