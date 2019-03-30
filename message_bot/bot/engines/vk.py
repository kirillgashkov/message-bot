"""
Bot engine based on social-networking site VK.
"""

from typing import Optional, Callable

from vk_api import vk_api, longpoll

from message_bot.bot.engines import BaseEngine


class VKEngine(BaseEngine):

    def __init__(self, username: str, password: str):
        self.vk_session = vk_session(username, password)
        self.vk_api = self.vk_session.get_api()

    def message(self, recipient_id: str, m: str):
        self.vk_api.messages.send(user_ids=recipient_id, message=m)

    def error(self, recipient_id: str, m: str, e: Optional[Exception]):
        s = f'{m}'
        self.vk_api.messages.send(user_ids=recipient_id, message=s)

    def run(self, message_handler: Callable[[str, str], None]):
        vk_longpoll = longpoll.VkLongPoll(self.vk_session)
        for event in vk_longpoll.listen():
            is_new_message = event.type != longpoll.VkEventType.MESSAGE_NEW
            is_from_user = event.from_user
            if not is_new_message or not is_from_user:
                continue
            message_handler(event.user_id, event.text)


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
