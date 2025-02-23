from aiogram import Router, types
from aiogram.filters import Command

from keyboard import create_main_keyboard
from registration import router as registration_router
from exchange import router as exchange_router
from tips import router as tips_router
from finances import router as finances_router

router = Router()
router.include_router(registration_router)
router.include_router(exchange_router)
router.include_router(tips_router)
router.include_router(finances_router)

@router.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = create_main_keyboard()
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=keyboard)
