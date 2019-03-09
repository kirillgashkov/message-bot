"""
Contains constants shared between other modules.
"""

import os

from message_bot import commands


#
# General
#


DATE_FORMAT = '%d/%m/%Y'


#
# Files
#


DIR_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GSPREAD_CREDS = os.path.join(DIR_ROOT, 'credentials', 'gspread.json')
VK_API_CREDS = os.path.join(DIR_ROOT, 'credentials', 'vk_api.json')


#
# Strings
#


HELP_OFFER_ON_ERROR = (
    f'Если вам нужна помощь, отправьте "{commands.foodbot.SUPER_COMMAND} '
    f'{commands.foodbot.ShowHelpCommand.keyword}"'
)
