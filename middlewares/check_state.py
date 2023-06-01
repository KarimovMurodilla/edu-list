import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler

from loader import storage
from keyboards.default import keyboard_buttons


class Checker(BaseMiddleware):
    """
    Simple middleware
    """
    async def on_pre_process_message(self, message: types.Message, data: dict):
        state = FSMContext(storage, message.chat.id, message.from_user.id)
        cur_state = await state.get_state()
        data = await state.get_data()

        white_list = ["/start", "🏫 Professional ta'lim muassasalari", "🏛 Akademik litseylar", "⚠️ Korrupsiya holati bo'yicha murojaat", "ℹ️ Boshqarma ma'lumotlari"]
        if not cur_state and not data and message.text not in white_list:
            await message.answer("OTFIV_Tashkent", reply_markup=keyboard_buttons.main_category())
            # raise CancelHandler()
