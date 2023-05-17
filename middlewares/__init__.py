from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .check_state import Checker


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(Checker())