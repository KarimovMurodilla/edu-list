from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from states.bundle import ProfiEduDetails, LyceumDetails
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons

from loader import dp, db


# ---Start---
@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = message.from_user
    user_in_db = await db.get_user(user.id)

    if not user_in_db:
        await db.reg_user(user.id, user.username, user.first_name)
    await message.answer("OTFIV_Tashkent", reply_markup=keyboard_buttons.main_category())


# ---Back button---
@dp.message_handler(text='🔙 Ortga qaytish', state='*')
async def bot_start(message: types.Message, state: FSMContext):
    cur_state = await state.get_state()
    
    # Schools
    if cur_state == 'ProfiEduDetails:step1' or not cur_state or cur_state == 'ProfiEduDetails:step2':
        await state.finish()
        await message.answer("OTFIV_Tashkent", reply_markup=keyboard_buttons.main_category())

    elif cur_state == 'ProfiEduDetails:step3':
        async with state.proxy() as data:
            await message.answer("Tanlang:", reply_markup=keyboard_buttons.profi_edu())    
            await ProfiEduDetails.step1.set()

    elif cur_state == 'ProfiEduDetails:step4':
        await message.answer("Tanlang:", reply_markup=keyboard_buttons.edu_data_menu())
        await ProfiEduDetails.step3.set()

    # Lyceums
    elif cur_state == 'LyceumDetails:step1':
        await state.finish()
        await message.answer("OTFIV_Tashkent", reply_markup=keyboard_buttons.main_category())

    elif cur_state == 'LyceumDetails:step2':
        names = await db.get_all_lyceum_names()

        await message.answer("Tanlang:", reply_markup=keyboard_buttons.show_names(names))
        await LyceumDetails.step1.set()

    elif cur_state == 'LyceumDetails:step3':
        async with state.proxy() as data:
            name = data['lyceum_name']
            lyceum = await db.get_lyceum_data(name)
            data['lyceum'] = lyceum

        await message.answer("Tanlang:", reply_markup = keyboard_buttons.edu_data_menu())

        await LyceumDetails.step2.set()