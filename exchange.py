import aiohttp
from aiogram import Router, F
from aiogram.types import Message
from config import Config

router = Router()

@router.message(F.text == "Курс валют")
async def exchange_rates(message: Message):
    url = f'https://v6.exchangerate-api.com/v6/{Config.EXCHANGE_API_KEY}/latest/USD'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                await message.answer("Ошибка при получении курса валют.")
                return
            data = await response.json()

    usd_to_rub = data.get('conversion_rates', {}).get('RUB')
    usd_to_eur = data.get('conversion_rates', {}).get('EUR')

    if usd_to_rub and usd_to_eur:
        eur_to_rub = usd_to_rub / usd_to_eur
        await message.answer(f"1 USD = {usd_to_rub:.2f} RUB\n1 EUR = {eur_to_rub:.2f} RUB")
    else:
        await message.answer("Не удалось получить данные о курсе валют.")
