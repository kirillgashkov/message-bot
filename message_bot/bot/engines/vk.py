"""
Bot engine based on social-networking site VK.
"""

import random
from typing import Optional, Callable

from vk_api import vk_api, bot_longpoll

from message_bot.bot.engines import BaseEngine


class VKEngine(BaseEngine):

    def __init__(self, token: str, group_id: str, help_offer: str):
        self.group_id = group_id
        self.session = vk_session(token)
        self.api = self.session.get_api()
        self.help_offer = help_offer

    def message(self, recipient_id: str, m: str):
        print(f'-> [{recipient_id}] {m}')
        self.api.messages.send(
            user_id=recipient_id,
            message=m,
            random_id=get_random_id()
        )

    def error(self, recipient_id: str, m: str, e: Optional[Exception]):
        print(f'-> [{recipient_id}] {m} {e}')
        s = f'{m}{f" {e}" if e else ""} {self.help_offer}'
        self.api.messages.send(
            user_id=recipient_id,
            message=s,
            random_id=get_random_id()
        )

    def run(self, message_handler: Callable[[str, str], None]):
        vk_longpoll = bot_longpoll.VkBotLongPoll(self.session, self.group_id)
        for event in vk_longpoll.listen():
            print(f'* {event}')
            is_new_message = event.type == bot_longpoll.VkBotEventType.MESSAGE_NEW
            is_from_user = event.from_user
            if not is_new_message or not is_from_user:
                continue
            try:
                message_handler(event.obj.peer_id, event.obj.text)
            except Exception as e:
                print(f'! {e}')


#
# Utilities
#


def vk_session(token: str) -> vk_api.VkApi:
    session = vk_api.VkApi(token=token, api_version='5.95')
    return session


def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])
