import aiosqlite
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

router = Router()

class FinancesForm(StatesGroup):
    category_1 = State()
    category_2 = State()
    category_3 = State()
    expenses_1 = State()
    expenses_2 = State()
    expenses_3 = State()

@router.message(F.text == "Личные финансы")
async def finances(message: Message, state: FSMContext):
    await state.set_state(FinancesForm.category_1)
    await message.answer("Введите первую категорию расходов:")

@router.message(FinancesForm.category_1)
async def category_1(message: Message, state: FSMContext):
    await state.update_data(category_1=message.text)
    await state.set_state(FinancesForm.expenses_1)
    await message.answer("Введите сумму расходов для первой категории:")

@router.message(FinancesForm.expenses_1)
async def expenses_1(message: Message, state: FSMContext):
    try:
        expense = float(message.text)
    except ValueError:
        await message.answer("Ошибка! Введите числовое значение суммы расходов.")
        return

    await state.update_data(expenses_1=expense)
    await state.set_state(FinancesForm.category_2)
    await message.answer("Введите вторую категорию расходов:")

@router.message(FinancesForm.category_2)
async def category_2(message: Message, state: FSMContext):
    await state.update_data(category_2=message.text)
    await state.set_state(FinancesForm.expenses_2)
    await message.answer("Введите сумму расходов для второй категории:")

@router.message(FinancesForm.expenses_2)
async def expenses_2(message: Message, state: FSMContext):
    try:
        expense = float(message.text)
    except ValueError:
        await message.answer("Ошибка! Введите числовое значение суммы расходов.")
        return

    await state.update_data(expenses_2=expense)
    await state.set_state(FinancesForm.category_3)
    await message.answer("Введите третью категорию расходов:")

@router.message(FinancesForm.category_3)
async def category_3(message: Message, state: FSMContext):
    await state.update_data(category_3=message.text)
    await state.set_state(FinancesForm.expenses_3)
    await message.answer("Введите сумму расходов для третьей категории:")

@router.message(FinancesForm.expenses_3)
async def expenses_3(message: Message, state: FSMContext):
    try:
        expense = float(message.text)
    except ValueError:
        await message.answer("Ошибка! Введите числовое значение суммы расходов.")
        return

    data = await state.get_data()
    telegram_id = message.from_user.id

    async with aiosqlite.connect('users.db') as db:
        await db.execute('''
            INSERT INTO finances (telegram_id, category_1, category_2, category_3, expenses_1, expenses_2, expenses_3)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            telegram_id, data["category_1"], data["category_2"], data["category_3"],
            data["expenses_1"], data["expenses_2"], expense
        ))
        await db.commit()

    await state.clear()
    await message.answer("Ваши данные о расходах успешно сохранены! 🎯")
