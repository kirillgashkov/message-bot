"""
Constants
"""

import re
from commands import help_command


DOMAIN_NAME = 'food'

DATE_FORMAT = '%d/%m/%Y'

STUDENT_REGEX = re.compile(r'^(0?[1-9]|1[0-9]|2[0-5])$')

HELP_OFFER_ON_ERROR = (
    f'Если вам нужна помощь, отправьте "{DOMAIN_NAME} {help_command.KEYWORD}"'
)
