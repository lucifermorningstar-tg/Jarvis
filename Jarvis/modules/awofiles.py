import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import SaitamaRobot.modules.awo_strings as awo_strings
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from SaitamaRobot.modules.helper_funcs.extraction import extract_user



@run_async
def awofile(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.AWOFILES_STRINGS))


@run_async
def yumeko(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.IGRIS_STRINGS))
                                                
@run_async
def randomlink(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(fun_strings.IGRIS_IMG), caption=f'*Command Me {name}*')
     

__help__ = """
 • `/runs`*:* reply a random string from an array of replies
 • `/slap`*:* slap a user, or get slapped if not a reply 🌝
 • `/shrug`*:* get shrug XD
 • `/table`*:* get flip/unflip :v
 • `/bluetext`*:* check urself :V
 • `/rlg`*:* Join ears,nose,mouth and create an emo ;-;
 • `/shout <keyword>`*:* write anything you want to give loud shout
 • `/weebify <text>`*:* returns a weebified text
 • `/sanitize`*:* always use this before `/pat` or any contact
 • `/pat`*:* pats a user, or get patted (^-^)
  - - - - - - - - - -
• *Games* 🎲 *:*
 • `/truth`*:* Get ready to reveal a surprising truth🤫
 • `/dare`*:* A dare is on way 😈
 • `/yumeko`*:* Awakening of pshycho Demon
 • `/insult`*:* Insult the person
 • `/decide`*:* Randomly answers yes/no/maybe/idk
 • `/toss`*:* Tosses A coin
 • `/roll`*:* Roll a dice & get you a number
"""

INSULT_HANDLER = DisableAbleCommandHandler("insult", insult)
ARISE_HANDLER = DisableAbleCommandHandler("arise", arise)                                      
YUMEKO_HANDLER = DisableAbleCommandHandler("yumeko", yumeko)
TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)
SANITIZE_HANDLER = DisableAbleCommandHandler("sanitize", sanitize)
RUNS_HANDLER = DisableAbleCommandHandler("runs", runs)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat)
ROLL_HANDLER = DisableAbleCommandHandler("roll", roll)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
BLUETEXT_HANDLER = DisableAbleCommandHandler("bluetext", bluetext)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)

dispatcher.add_handler(INSULT_HANDLER)
dispatcher.add_handler(ARISE_HANDLER)                                          
dispatcher.add_handler(YUMEKO_HANDLER)
dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(SANITIZE_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(BLUETEXT_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)

__mod_name__ = "Fun"
__command_list__ = [
    "runs", "slap", "roll", "toss", "shrug", "bluetext", "rlg", "decide",
    "table", "pat", "sanitize"
]
__handlers__ = [
    RUNS_HANDLER,YUMEKO_HANDLER,ARISE_HANDLER,TRUTH_HANDLER, DARE_HANDLER, SLAP_HANDLER, PAT_HANDLER, ROLL_HANDLER, TOSS_HANDLER,
    SHRUG_HANDLER, BLUETEXT_HANDLER, RLG_HANDLER, DECIDE_HANDLER, TABLE_HANDLER,INSULT_HANDLER, 
    SANITIZE_HANDLER
]
