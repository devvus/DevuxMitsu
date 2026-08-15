
import config
from MusicSp import app
from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], url=config.SUPPORT_GROUP,
                style=ButtonStyle.SUCCESS,
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
                style=ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"], callback_data="settings_back_helper",
                style=ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"], url=config.SUPPORT_GROUP,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["S_B_6"], url=config.SUPPORT_CHANNEL,
                style=ButtonStyle.PRIMARY,
            ),
        ],
    ]
    return buttons
