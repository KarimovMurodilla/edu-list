from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from states.bundle import ProfiEduDetails
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons

from loader import dp, db


# ---Professional educations---
@dp.message_handler(text="🏫 Professional ta'lim muassasalari", state='*')
async def profi_edi(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Tanlang:", reply_markup=keyboard_buttons.profi_edu())
    await ProfiEduDetails.step1.set()


@dp.message_handler(state=ProfiEduDetails.step1)
async def process_profi_edu(message: types.Message, state: FSMContext):
    school = await db.get_all_school_names()
    college = await db.get_all_college_names()
    texnikum = await db.get_all_texnikum_names()

    edu_data = {
        "🏫 Kasb-hunar maktabi": school,
        "🏫 Kollej": college,
        "🏫 OTM huzuridagi texnikum": texnikum,
    }

    if message.text in edu_data.keys():
        await message.answer("Tanlang:", reply_markup=keyboard_buttons.show_names(edu_data.get(message.text)))    
        async with state.proxy() as data:
            data["edu_type_name"] = message.text
        await ProfiEduDetails.next()


@dp.message_handler(state=ProfiEduDetails.step2)
async def process_profi_edu(message: types.Message, state: FSMContext):
    await message.answer("Tanlang:", reply_markup=keyboard_buttons.edu_data_menu())
    await ProfiEduDetails.next()

    async with state.proxy() as data:
        edu_type_name = data.get("edu_type_name")

        if edu_type_name == "🏫 Kasb-hunar maktabi":
            data['edu_type'] = await db.get_school_data(message.text)
        
        elif edu_type_name == "🏫 Kollej":
            data['edu_type'] = await db.get_college_data(message.text)
        
        elif edu_type_name == "🏫 OTM huzuridagi texnikum":
            data['edu_type'] = await db.get_texnikum_data(message.text)
        

@dp.message_handler(state=ProfiEduDetails.step3)
async def process_profi_edu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        edu_type = data.get('edu_type')

    edu_data = {
        "ℹ️ Umumiy ma'lumot": edu_type.malumot,
        "🏢 Rahbariyat": edu_type.rahbariyat,
        "🎯 Yo'nalishi": edu_type.yonalish,
        "📥 Qabul": edu_type.qabul,
        "❓Ko'p beriladigan savollar": edu_type.savollar,
        "📞 Bog'lanish": edu_type.boglanish,
    }

    if message.text in edu_data.keys():
        if message.text == "ℹ️ Umumiy ma'lumot":
            await message.answer(edu_data.get(message.text), reply_markup=keyboard_buttons.back())
            await ProfiEduDetails.next()
        else:
            await message.answer(edu_data.get(message.text), reply_markup=keyboard_buttons.edu_data_menu())