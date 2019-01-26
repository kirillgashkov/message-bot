"""
Bot's engine that interacts with the user via social-networking site VK.
"""

from typing import Optional, Tuple, Callable
import json
from vk_api import vk_api, longpoll
from message_bot import models
from message_bot.bot.engines.base import BaseEngine
from message_bot.constants import VK_API_CREDS, HELP_OFFER_ON_ERROR


class VKEngine(BaseEngine):

    def __init__(self):
        username, password = credentials()
        self.vk_session = vk_session(username, password)
        self.vk = self.vk_session.get_api()

    def message(self, person: models.Person, m: str):
        id_ = person.ids.get('vk')
        if not id_:
            print(
                'MessageBotError: person targeted to receive message does '
                'not have VK id.'
            )
            return
        self.vk.messages.send(user_ids=id_, message=m)

    def error(self, person: models.Person, m: str, e: Exception):
        formatted_m = m + ' ' + HELP_OFFER_ON_ERROR
        id_ = person.ids.get('vk')
        if not id_:
            print(
                'MessageBotError: person targeted to receive message does '
                'not have VK id.'
            )
            return
        print('[!]', m, repr(e))
        self.vk.messages.send(user_ids=id_, message=formatted_m)

    def run(self, message_handler: Callable[[models.Person, str], None]):
        vk_longpoll = longpoll.VkLongPoll(self.vk_session)
        for event in vk_longpoll.listen():
            is_new_message = event.type != longpoll.VkEventType.MESSAGE_NEW
            is_from_user = event.from_user
            if not (is_new_message and is_from_user):
                continue
            sender_id = event.user_id
            sender = models.Person.for_id('vk', sender_id)
            message = event.text
            message_handler(sender, message)


#
# Utilities
#


def vk_session(username: str, password: str) -> Optional[vk_api.VkApi]:
    session = vk_api.VkApi(username, password)
    try:
        session.auth(token_only=True)
    except vk_api.AuthError as e:
        print(e)
        return None
    return session


def credentials() -> Tuple[str, str]:
    creds = json.load(VK_API_CREDS)
    return creds['username'], creds['password']
