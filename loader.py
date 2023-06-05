from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.connection import Database
from utils.misc.mail_sender.sender import SendMail


# AIOgram
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# DB
db = Database()


# Email
mail = SendMail(config.API_KEY, config.API_SECRET)