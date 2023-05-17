from aiogram import types


def main_category():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Professional ta'lim muassasalari")
    btn2 = types.KeyboardButton("Akademik litseylar")
    menu.add(btn1, btn2)

    return menu


def profi_edu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Kasb-hunar maktabi")
    btn2 = types.KeyboardButton("Kollej")
    btn3 = types.KeyboardButton("OTM huzuridagi texnikum")
    btn4 = types.KeyboardButton("Ortga qaytish")
    menu.add(btn1, btn2, btn3, btn4)

    return menu


def edu_data_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Umumiy ma'lumot")
    btn2 = types.KeyboardButton("Rahbariyat")
    btn3 = types.KeyboardButton("Yo'nalishi")
    btn4 = types.KeyboardButton("Qabul")
    btn5 = types.KeyboardButton("Ko'p beriladigan savollar")
    btn6 = types.KeyboardButton("Bog'lanish")
    btn7 = types.KeyboardButton("Ortga qaytish")
    menu.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    return menu


def back():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton("Ortga qaytish")
    menu.add(back)

    return menu


def show_names(names):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    for name in names:
        menu.add(name)

    back = types.KeyboardButton("Ortga qaytish")

    menu.add(back)
    return menu
   