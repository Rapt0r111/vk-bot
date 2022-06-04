import datetime
import json
import random
import time
from threading import Thread

import numpy as np
import requests

import vk_api
from bs4 import BeautifulSoup
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

import config
from weather import weather, weather_today, weather_tomorrow

vk_session = vk_api.VkApi(token=config.token)
vk = vk_session.get_api()
group_id = config.group_id



headers = {"accept": "*/*",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (XHTML, like Gecko) "
                         "Chrome/95.0.4638.69 Safari/537.36"}


def get_url(url):
    s = requests.Session()
    return s.get(url=url, headers=headers)


def get_user_info(user_id):
    return vk.users.get(user_ids=user_id)


def get_random_id():
    return np.random.randint(0, 100000000)


def attach(peer_id, query_json, id_group, value, first, last, times):
    for _ in range(times):
        ok = True
        while ok:
            # noinspection PyBroadException
            try:
                vk.messages.send(attachment=f"{value}-{id_group}_{np.random.randint(first, last)}",
                                 peer_id=peer_id, forward=[query_json], random_id=get_random_id())
                ok = False
            except:
                pass


def answer_message(message_id, peer_id, text='', stick=False, attachment='', times=1):
    query_json = json.dumps({"peer_id": peer_id, "conversation_message_ids": [message_id], "is_reply": True})
    if attachment == 'аниме':
        attach(peer_id=peer_id, query_json=query_json, id_group=96295942, value='photo', first=457296373,
               last=457326946, times=times)
    elif attachment == 'яой':
        vk.messages.send(peer_id=peer_id, message='Хуй вам. До свидания. Контент 18+ запрещён!',
                         random_id=get_random_id())
    elif attachment == 'подрочил':
        vk.messages.send(peer_id=peer_id, forward=[query_json], random_id=get_random_id(),
                         attachment="photo-200946724_457239654")
    elif attachment == 'хорни':
        attach(peer_id=peer_id, query_json=query_json, id_group=189048536, value='photo', first=457245731,
               last=457252600, times=times)
    elif text != '':
        vk.messages.send(peer_id=peer_id, forward=[query_json], message=text, random_id=get_random_id())
    if stick:
        vk.messages.send(peer_id=peer_id, sticker_id=63820, random_id=get_random_id())


def a_time():
    while True:
        if int(datetime.datetime.now().hour) == 21 and int(datetime.datetime.now().minute) == 00 and int(
                datetime.datetime.now().second) == 0:
            vk.messages.send(peer_id=2000000003, message="""
ХОХЛЫ РАВНЯЙСЬ

🐷🐖🐷🐖🐖🐷
👕👕👕👕👕👕
👖👖👖👖👖👖

ОТСТАВИТЬ

РАВНЯЙСЬ

🐷🐖🐖🐖🐖🐖
👕👕👕👕👕👕
👖👖👖👖👖👖

СМИРНО
🐷🐷🐷🐷🐷🐷
👕👕👕👕👕👕
👖👖👖👖👖👖   """, random_id=get_random_id())
            time.sleep(1)
        if int(datetime.datetime.now().hour) == 5 and int(datetime.datetime.now().minute) == 0 and int(
                datetime.datetime.now().second) == 0:
            vk.messages.send(peer_id=2000000003, message=
"""
ХОХЛЫ РАВНЯЙСЬ

🐷🐖🐷🐖🐖🐷
👕👕👕👕👕👕
👖👖👖👖👖👖

ОТСТАВИТЬ

РАВНЯЙСЬ

🐷🐖🐖🐖🐖🐖
👕👕👕👕👕👕
👖👖👖👖👖👖

СМИРНО
🐷🐷🐷🐷🐷🐷
👕👕👕👕👕👕
👖👖👖👖👖👖   """, random_id=get_random_id())
            time.sleep(1)
        time.sleep(0.33)


answers = ("Это несомненно", "Перспективы хорошие", "Можете не сомневаться",
           "Мой ответ нет", "Мои источники говорят нет", "Точно да",
           "Думаю да", " Нет", "Да", "Без сомнений")
rules = ("""😍😘😍🤪🥰Stay Together. Fan club. 😍🥰😘🥰😛
Просим саблюдать 😙
1 Никаво ни абижать, не абзываца сина и обидна ☺
2 мотерица 🤬можна но не многа😋
3 увожать и слушать одминов биседы 🤓
4 Флуд нильзя 🚫
5 преглошать толька с розришения одминов😤
6 Ауф бомбила😱😱😱
7 бфу фигня🤢🤢
8 долга афк = кик😈
9 любить Шлепу 😍😍
10 ни называть Шлепу Степой!!!!!!😡😡😡😡
За нарушения правел бан (кик из биседы) 🤬🤯😡🥵""")


def magic_ball(question):
    if question != '' and question:
        return answers[random.randint(0, len(answers) - 1)]
    else:
        return "Спроси еще раз"


def rnd_fact(url):
    # noinspection PyBroadException
    try:
        response = get_url(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.find('table', {'class': 'text'}).text
    except:
        return 'В данный момент хуй вам. Попробуйте позже :) С уважением, Нина Павловна.'


def rnd_ask(url):
    # noinspection PyBroadException
    try:
        response = get_url(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.find('table', {'class': 'text'}).text
        return data.split('—')[0]
    except:
        return 'В данный момент хуй вам. Попробуйте позже :) С уважением, Нина Павловна.'


longpoll = VkBotLongPoll(vk_session, group_id)


def check_number(message):
    # noinspection PyBroadException
    try:
        if int(message.split()[1]) > 5 or int(message.split()[1]) <= 0:
            return 1
        else:
            return int(message.split()[1])
    except:
        return 1


def who_question():
    j = vk.messages.getConversationMembers(peer_id=2000000003).get('items')
    while True:
        x = int(j[np.random.randint(0, len(j))].get('member_id'))
        if x >= 0:
            return f'Я думаю - это @id{x} ({get_user_info(int(x))[0].get("first_name")})'
        else:
            pass

def main():
    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    message = event.object.message.get('text').lower()
                    peer_id = event.object.message.get('peer_id')
                    user_id = event.object.message.get('from_id')
                    user_info = get_user_info(int(user_id))
                    print(user_info[0].get('first_name') + ' ' + user_info[0].get('last_name') + ': ' + message)
                    message_id = event.object.message.get('conversation_message_id')
                    if event.from_chat:
                        if user_id != 320585774 and 'я гей' in message:
                            answer_message(message_id=message_id, peer_id=peer_id, text="Не правда", stick=True)
                        elif '!аниме' in message:
                            answer_message(message_id=message_id, peer_id=peer_id, stick=False, attachment='аниме',
                                           times=check_number(message))
                        elif '!хорни' in message:
                            answer_message(message_id=message_id, peer_id=peer_id, stick=False, attachment='хорни',
                                           times=check_number(message))
                        elif '!яой' in message:
                            answer_message(message_id=message_id, peer_id=peer_id, stick=False, attachment='яой',
                                           times=check_number(message))
                        elif '!подрочил' in message:
                            answer_message(message_id=message_id, peer_id=peer_id, stick=False, attachment='подрочил',
                                           times=check_number(message))
                        elif 'иди нахуй' in message or 'пошёл нах' in message or 'пошел нах' in message or 'или нах' in message:
                            answer_message(message_id=message_id, peer_id=peer_id, text="Сам иди нахуй :(", stick=False)
                        elif 'фамилия ' in message and 'ян' in message:
                            answer_message(message_id=message_id, peer_id=peer_id, text="Чухалёнов", stick=False)
                        elif '!факт' in message:
                            vk.messages.send(peer_id=peer_id, message=rnd_fact(url='https://randstuff.ru/fact/'),
                                             random_id=get_random_id())
                        elif '!мудрость' in message:
                            vk.messages.send(peer_id=peer_id, message=rnd_ask(url='https://randstuff.ru/saying/'),
                                             random_id=get_random_id())
                        #elif 'стас' in message or 'станис' in message:
                        #    answer_message(text="Вообще-то он Native English Speaker", message_id=message_id,
                        #                   peer_id=peer_id, stick=False)
                        elif '!шар' in message:
                            answer_message(message_id=message_id, peer_id=peer_id,
                                           text=magic_ball(question=message[4:].split()), stick=False)
                        elif '!правила' in message:
                            vk.messages.send(peer_id=peer_id, message=rules, random_id=get_random_id())
                        elif ' бот ' in message:
                            answer_message(peer_id=peer_id, message_id=message_id,
                                           text='А ты кожаный ублюдок. И вообще иди нахуй.', stick=False)
                        elif '!кто' in message or '!кого' in message:
                            answer_message(peer_id=peer_id, message_id=message_id,
                                           text=who_question(), stick=False)
                        elif '!погода' in message:
                            answer_message(peer_id=peer_id, message_id=message_id,
                                           text=weather(str('погода Калининград сейчас'+message[7:])), stick=False)
                            answer_message(peer_id=peer_id, message_id=message_id,
                                           text=weather_today(), stick=False)
                        elif '!завтра' in message:
                            answer_message(peer_id=peer_id, message_id=message_id,
                                           text=weather(str('погода Калининград завтра'+message[7:])), stick=False)
                            answer_message(peer_id=peer_id, message_id=message_id,
                                           text=weather_tomorrow(), stick=False)
                        # elif '!авито' in message:
                        #     x=parser.par()
                        #     print(x)
                        #     for i in x:
                        #         vk.messages.send(peer_id=peer_id, random_id=get_random_id(),
                        #                message=i)

        except Exception as e:
            print(e)

def input_cmd():
    while True:
        command = input()
        if command[:7] == '!Выведи':
            vk.messages.send(peer_id=2000000003, message=command[7:], random_id=get_random_id())


if __name__ == '__main__':
    t1 = Thread(target=a_time, args=(), daemon=True)
    print(datetime.datetime.now())
    t2 = Thread(target=main, args=())
    t3 = Thread(target=input_cmd, args=())
    t1.start()
    t2.start()
    t3.start()
