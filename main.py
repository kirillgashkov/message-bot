"""
Message bot's main file.
"""

import datetime
import json

from message_bot import bot, commands, database
from message_bot.constants import GSPREAD_CREDS, VK_API_CREDS


def main():
    print('setting the engines... ', end='')
    _set_engines()
    print('done')
    print('initializing the databases... ', end='')
    _init_databases()
    print('done')
    print('ready.')
    try:
        bot.run(_message_handler)
    except KeyboardInterrupt:
        _deinit_databases()


def _set_engines():
    people_database_engine = database.engines.GsheetEngine(
        GSPREAD_CREDS, 'message-bot', 'people')
    foodbot_database_engine = database.engines.GsheetEngine(
        GSPREAD_CREDS, 'message-bot', 'foodbot')

    with open(VK_API_CREDS) as f:
        creds = json.load(f)
    bot_engine = bot.engines.VKEngine(
        creds['access_token'],
        creds['group_id'],
        'Если вам нужна помощь, отправьте "food help".'
    )

    database.people.set_engine(people_database_engine)
    database.foodbot.set_engine(foodbot_database_engine)
    bot.set_engine(bot_engine)


def _init_databases():
    database.people.engine.pull()
    database.foodbot.engine.pull()


def _deinit_databases():
    database.people.engine.push()
    database.foodbot.engine.push()


def _message_handler(sender_id: str, message: str):
    sender = database.people.get_person_by_id(sender_id)
    elements = message.split()

    if len(elements) == 0:
        msg = (
            'InputError: пустое сообщение.'
        )
        bot.error(sender_id, msg)
        return
    super_command = elements[0]

    if len(elements) == 1:
        command = ''
        args = list()
    else:
        command = elements[1]
        args = elements[2:]

    today = datetime.date.today()

    commands.run_command(super_command, command, today, sender, args)


if __name__ == '__main__':
    main()
