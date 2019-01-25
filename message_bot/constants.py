"""
Constants
"""

import os
import re
from foodbot.commands import help_command


#
# Commands
#


DOMAIN_NAME = 'food'
DATE_FORMAT = '%d/%m/%Y'
STUDENT_REGEX = re.compile(r'^(0?[1-9]|1[0-9]|2[0-5])$')
HELP_OFFER_ON_ERROR = (
    f'Если вам нужна помощь, отправьте "{DOMAIN_NAME} {help_command.KEYWORD}"'
)


#
# Files
#


DIR_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_CREDS = os.path.join(DIR_ROOT, 'credentials', 'gspread.json')
