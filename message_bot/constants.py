"""
Contains constants shared between other models.
"""

import os


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
