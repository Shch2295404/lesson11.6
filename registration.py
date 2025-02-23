import aiosqlite
from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "Регистрация в телеграм-боте")
async def registration(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username or "Не указан"

    async with aiosqlite.connect('users.db') as db:
        async with db.execute('SELECT 1 FROM users WHERE telegram_id = ?', (telegram_id,)) as cursor:
            if await cursor.fetchone():
                await message.answer("Вы уже зарегистрированы.")
                return

        await db.execute('INSERT INTO users (telegram_id, username) VALUES (?, ?)', (telegram_id, username))
        await db.commit()

    await message.answer("Вы успешно зарегистрированы.")
