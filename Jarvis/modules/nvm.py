#    Copyright (C) 2020-2021 by @AmarnathCdj & @InukaAsith
#    Chatbot system written by @AmarnathCdj databse added and recoded for pyrogram by @InukaAsith
#    This programme is a part of Jarvis (TG bot) project
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#    Kang with the credits
#    Special credits to @AmarnathCdj
import re

import emoji
import requests

IBM_WATSON_CRED_URL = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/bd6b59ba-3134-4dd4-aff2-49a79641ea15"
IBM_WATSON_CRED_PASSWORD = "UQ1MtTzZhEsMGK094klnfa-7y_4MCpJY1yhd52MXOo3Y"
url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
from google_trans_new import google_translator
from pyrogram import filters

from Jarvis import BOT_ID
from Jarvis.db.mongo_helpers.aichat import add_chat, get_session, remove_chat
from Jarvis.function.pluginhelpers import admins_only, edit_or_reply
from Jarvis.services.pyrogram import pbot as Jarvis

translator = google_translator()


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


daisy_chats = []
en_chats = []
# AI Chat (C) 2020-2021 by @InukaAsith
"""
@Jarvis.on_message(
    filters.voice & filters.reply & ~filters.bot & ~filters.via_bot & ~filters.forwarded,
    group=2,
)
async def hmm(client, message):
    if not get_session(int(message.chat.id)):
        message.continue_propagation()
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    previous_message = message
    required_file_name = message.download()
    if IBM_WATSON_CRED_URL is None or IBM_WATSON_CRED_PASSWORD is None:
        await message.reply(
            "You need to set the required ENV variables for this module. \nModule stopping"
        )
    else:
        headers = {
            "Content-Type": previous_message.voice.mime_type,
        }
        data = open(required_file_name, "rb").read()
        response = requests.post(
            IBM_WATSON_CRED_URL + "/v1/recognize",
            headers=headers,
            data=data,
            auth=("apikey", IBM_WATSON_CRED_PASSWORD),
        )
        r = response.json()
        print(r)
        await client.send_message(message, r)
"""


@Jarvis.on_message(filters.command("chatbot") & ~filters.edited & ~filters.bot)
@admins_only
async def hmm(_, message):
    global daisy_chats
    if len(message.command) != 2:
        await message.reply_text(
            "I only recognize `/chatbot on` and /chatbot `off only`"
        )
        message.continue_propagation()
    status = message.text.split(None, 1)[1]
    chat_id = message.chat.id
    if status == "ON" or status == "on" or status == "On":
        lel = await edit_or_reply(message, "`Processing...`")
        lol = add_chat(int(message.chat.id))
        if not lol:
            await lel.edit("Jarvis AI Already Activated In This Chat")
            return
        await lel.edit(
            f"Jarvis AI Successfully Added For Users In The Chat {message.chat.id}"
        )

    elif status == "OFF" or status == "off" or status == "Off":
        lel = await edit_or_reply(message, "`Processing...`")
        Escobar = remove_chat(int(message.chat.id))
        if not Escobar:
            await lel.edit("Jarvis AI Was Not Activated In This Chat")
            return
        await lel.edit(
            f"Jarvia AI Successfully Deactivated For Users In The Chat {message.chat.id}"
        )

    elif status == "EN" or status == "en" or status == "english":
        if not chat_id in en_chats:
            en_chats.append(chat_id)
            await message.reply_text("English AI chat Enabled!")
            return
        await message.reply_text("AI Chat Is Already Disabled.")
        message.continue_propagation()
    else:
        await message.reply_text(
            "I only recognize `/chatbot on` and /chatbot `off only`"
        )


@Jarvis.on_message(
    filters.text & filters.reply & ~filters.bot & ~filters.via_bot & ~filters.forwarded,
    group=2,
)
async def hmm(client, message):
    if not get_session(int(message.chat.id)):
        message.continue_propagation()
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        test = msg
        test = test.replace("daisy", "Aco")
        test = test.replace("Daisy", "Aco")
        querystring = {
            "bid": "178",
            "key": "sX5A2PcYZbsN5EY6",
            "uid": "mashape",
            "msg": {test},
        }
        headers = {
            "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "Daisy")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        pro = result
        try:
            await Jarvis.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError as e:
            print(e)
    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            # print (rm)
            lan = translator.detect(rm)
        test = rm
        if not "en" in lan and not lan == "":
            test = translator.translate(test, lang_tgt="en")

        # test = emoji.demojize(test.strip())

        # Kang with the credits bitches @InukaASiTH
        test = test.replace("jarvis", "Aco")
        test = test.replace("Jarvis", "Aco")
        querystring = {
            "bid": "178",
            "key": "sX5A2PcYZbsN5EY6",
            "uid": "mashape",
            "msg": {test},
        }
        headers = {
            "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "Daisy")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        pro = result
        if not "en" in lan and not lan == "":
            pro = translator.translate(pro, lang_tgt=lan[0])
        try:
            await Jarvis.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError as e:
            print(e)


@Jarvis.on_message(filters.text & filters.private & filters.reply & ~filters.bot)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
        lan = translator.detect(rm)
    test = rm
    if not "en" in lan and not lan == "":
        test = translator.translate(test, lang_tgt="en")

    # test = emoji.demojize(test.strip())

    # Kang with the credits bitches @InukaASiTH
    test = test.replace("jarvis", "Aco")
    test = test.replace("Jarvis", "Aco")
    querystring = {
        "bid": "178",
        "key": "sX5A2PcYZbsN5EY6",
        "uid": "mashape",
        "msg": {test},
    }
    headers = {
        "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "Daisy")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    pro = result
    if not "en" in lan and not lan == "":
        pro = translator.translate(pro, lang_tgt=lan[0])
    try:
        await Jarvis.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError as e:
        print(e)


@Jarvis.on_message(
    filters.regex("darkjarvis|darkJarvia|DarkJarvis|jarvis|Jarvis")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel
)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
        lan = translator.detect(rm)
    test = rm
    if not "en" in lan and not lan == "":
        test = translator.translate(test, lang_tgt="en")

    # test = emoji.demojize(test.strip())

    # Kang with the credits bitches @InukaASiTH
    test = test.replace("jarvis", "Aco")
    test = test.replace("Jarvis", "Aco")
    querystring = {
        "bid": "178",
        "key": "sX5A2PcYZbsN5EY6",
        "uid": "mashape",
        "msg": {test},
    }
    headers = {
        "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "Jarvis")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    pro = result
    if not "en" in lan and not lan == "":
        pro = translator.translate(pro, lang_tgt=lan[0])
    try:
        await Jarvis.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError as e:
        print(e)


__help__ = """
<b> Chatbot </b>
<i> PRESENTING DAISY AI 3.0. THE ONLY AI SYSTEM WHICH CAN DETECT & REPLY UPTO 200 LANGUAGES </i>
 - /chatbot <i>ON/OFF</i>: Enables and disables AI Chat mode (EXCLUSIVE)
* DaisyAI can detect and reply upto 200 languages by now *
 - /chatbot EN : Enables English only chatbot
 
<b> Lydia </b>
<i> PRESENTING DAISY'S LYDI
<b> Assistant </b>
 - /ask <i>question</i>: Ask question from daisy
 - /ask <i> reply to voice note</i>: Get voice reply
 
<i> Lydia AI can be unstable sometimes </i>
"""

__mod_name__ = "AI Assistant"
