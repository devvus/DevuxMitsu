
import config
from MusicSp import app

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true",

            ),
            InlineKeyboardButton(
                text=_["S_B_2"], url=config.SUPPORT_GROUP,

            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",

            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"], callback_data="settingsback_helper",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"], url=config.SUPPORT_GROUP,

            ),
            InlineKeyboardButton(
                text=_["S_B_6"], url=config.SUPPORT_CHANNEL,

            ),
        ],
    ]
    return buttons
