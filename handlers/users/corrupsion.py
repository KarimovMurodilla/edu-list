from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from states.bundle import CorrupsionIssue
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons

from loader import dp, db, mail


# ---Back button---
@dp.message_handler(text="⚠️ Korrupsiya holati bo'yicha murojaat", state='*')
async def corrupsion_issue_process(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Ismingizni yuboring", reply_markup=types.ReplyKeyboardRemove())
    await CorrupsionIssue.get_name.set()


@dp.message_handler(state=CorrupsionIssue.get_name)
async def corrupsion_issue_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Telefon raqamingizni yuboring", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton("Yuborish", request_contact=True)))
    await CorrupsionIssue.next()


@dp.message_handler(content_types = 'contact', state=CorrupsionIssue.get_phone_number)
async def corrupsion_issue_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.contact.phone_number
    await message.answer("Murojaatingizni yuboring")
    await CorrupsionIssue.next()


@dp.message_handler(state=CorrupsionIssue.get_issue)
async def corrupsion_issue_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        name = data.get("name")
        contact = data.get("contact")
        issue = message.text

    # await db.reg_issue(message.from_user.id, message.from_user.username, name, contact, issue)
    mail.send_mail("⚠️ Korrupsiya holati bo'yicha murojaat", f"<p>From: {name}<br>Phone number: {contact}<br>Issue: {issue}</p>")
    await message.answer("Murojaatingiz qabul qilindi! E'tiboringiz uchun raxmat!", reply_markup=keyboard_buttons.main_category())
    await state.finish()