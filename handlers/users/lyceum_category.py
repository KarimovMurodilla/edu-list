from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from states.bundle import LyceumDetails
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons

from loader import dp, db


# ---Back button---
@dp.message_handler(text="Akademik litseylar", state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    names = await db.get_all_lyceum_names()

    await message.answer("Tanlang:", reply_markup=keyboard_buttons.show_names(names))
    await LyceumDetails.step1.set()


@dp.message_handler(state=LyceumDetails.step1)
async def bot_start(message: types.Message, state: FSMContext):
    lyceum = await db.get_lyceum_data(message.text)
    async with state.proxy() as data:
        data['lyceum'] = lyceum
        data['lyceum_name'] = message.text

    await message.answer("Tanlang:", reply_markup = keyboard_buttons.edu_data_menu())

    await LyceumDetails.next()


@dp.message_handler(state=LyceumDetails.step2)
async def process_lyceum_info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        lyceum = data.get("lyceum")

    edu_data = {
        "Umumiy ma'lumot": lyceum.malumot,
        "Rahbariyat": lyceum.rahbariyat,
        "Yo'nalishi": lyceum.yonalish,
        "Qabul": lyceum.qabul,
        "Ko'p beriladigan savollar": lyceum.savollar,
        "Bog'lanish": lyceum.boglanish,
    }

    if message.text == "Umumiy ma'lumot":
        await message.answer(edu_data.get(message.text), reply_markup=keyboard_buttons.back())
        await LyceumDetails.next()

    else:
        await message.answer(edu_data.get(message.text), reply_markup=keyboard_buttons.edu_data_menu())