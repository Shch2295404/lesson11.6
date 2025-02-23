from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def create_main_keyboard():
    buttons = [
        ["Регистрация в телеграм-боте", "Курс валют"],
        ["Советы по экономии", "Личные финансы"]
    ]
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=btn) for btn in row] for row in buttons],
        resize_keyboard=True
    )
