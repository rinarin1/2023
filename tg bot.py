import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

logging.basicConfig(level = logging.INFO)

TOKEN = '5992867934:AAHotzhdPRlUgDHfq_W62f_lzy_S0-h5Ig0'

bot = Bot(TOKEN)
dp = Dispatcher(bot)

db = {}
w = 0

@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
    db[message.from_user.id] = {'понедельник' : '', 'вторник' : '', 'среда' : '', 'четверг' : '', 'пятница' : '', 'суббота' : '', 'воскресенье' : ''}

#@dp.message_handler()
#async def p(message: types.Message):
#    f = message.text
#    d = open('bot.txt', 'w')
#    d.write(f)
#    d.close
#    await message.answer(f)

#@dp.message_handler(lambda message: message.text == 'добавить расписание' or message.text == 'изменить расписание')
#async def week(message: types.Message):
#    buttons = [types.InlineKeyboardButton(text = "понедельник", callback_data = "d_1"),
#                types.InlineKeyboardButton(text = "вторник", callback_data = "d_2"),
#                types.InlineKeyboardButton(text = "среда", callback_data = "d_3"),
#                types.InlineKeyboardButton(text = "четверг", callback_data = "d_4"),
#                types.InlineKeyboardButton(text = "пятница", callback_data = "d_5"),
#                types.InlineKeyboardButton(text = "суббота", callback_data = "d_6"),
#                types.InlineKeyboardButton(text = "воскресенье", callback_data = "d_7")]
#    keyboard = types.InlineKeyboardMarkup(row_width = 1)
#    keyboard.add(*buttons)
#    await message.answer('Выбери день недели:', reply_markup = keyboard)

#@dp.callback_query_handler(Text(startswith = "d_"))
#async def callbacks_timetable(call: types.CallbackQuery):
#    action = call.data.split("_")[1]
#    if action == "1":
#        m = message.text
#        db[message.from_user.id]['понедельник'] = m
#    elif action == "2":
#        m = message.text
#        db[message.from_user.id]['вторник'] = m
#    elif action == "3":
#        m = message.text
#        db[message.from_user.id]['среда'] = m
#    elif action == "4":
#        m = message.text
#        db[message.from_user.id]['четверг'] = m
#    elif action == "5":
#        m = message.text
#        db[message.from_user.id]['пятница'] = m
#    elif action == "6":
#        m = message.text
#        db[message.from_user.id]['суббота'] = m
#    elif action == "7":
#        m = message.text
#        db[message.from_user.id]['воскресенье'] = m

@dp.message_handler(lambda message: message.text == 'изменить/добавить расписание')
async def edit_timetable(message: types.Message):
    w = 2
    await message.answer('Выбери день недели')  

@dp.message_handler(lambda message: message.text == 'расписание')
async def timetable_output(message: types.Message):
    w = 1
    await message.answer('Выбери день недели')
   
@dp.message_handler(lambda message: message.text == 'понедельник')
async def monday(message: types.Message):
    if w == 1:
        await message.answer(db[message.from_user.id]['понедельник'])
    if w == 2:
        await message.answer(db[message.from_user.id]['понедельник'])
        await message.answer('''Напиши свое расписание:
1.
2.
3.
4.
5.
6.
7.
8.
 и тд.''')
        w = 3
   
@dp.message_handler(lambda message: message.text == 'вторник')
async def tuesday(message: types.Message):
    if w == 1:
        await message.answer(db[message.from_user.id]['вторник'])
    if w == 2:
        await message.answer(db[message.from_user.id]['вторник'])
        await message.answer('''Напиши свое расписание:
1.
2.
3.
4.
5.
6.
7.
8.
 и тд.''')
        w = 4

@dp.message_handler(lambda message: message.text == 'среда')
async def wednesday(message: types.Message):
    if w == 1:
        await message.answer(db[message.from_user.id]['среда'])
    if w == 2:
        await message.answer(db[message.from_user.id]['среда'])
        await message.answer('''Напиши свое расписание:
1.
2.
3.
4.
5.
6.
7.
8.
 и тд.''')
        w = 5

@dp.message_handler(lambda message: message.text == 'четверг')
async def thursday(message: types.Message):
    if w == 1:
        await message.answer(db[message.from_user.id]['четверг'])
    if w == 2:
        await message.answer(db[message.from_user.id]['четверг'])
        await message.answer('''Напиши свое расписание:
1.
2.
3.
4.
5.
6.
7.
8.
 и тд.''')
        w = 6

@dp.message_handler(lambda message: message.text == 'пятница')
async def friday(message: types.Message):
    if w == 1:
        await message.answer(db[message.from_user.id]['пятница'])
    if w == 2:
        await message.answer(db[message.from_user.id]['пятница'])
        await message.answer('''Напиши свое расписание:
1.
2.
3.
4.
5.
6.
7.
8.
 и тд.''')
        w = 7

@dp.message_handler(lambda message: message.text == 'суббота')
async def saturday(message: types.Message):
    if w == 1:
        await message.answer(db[message.from_user.id]['суббота'])
    if w == 2:
        await message.answer(db[message.from_user.id]['суббота'])
        await message.answer('''Напиши свое расписание:
1.
2.
3.
4.
5.
6.
7.
8.
 и тд.''')
        w = 8

@dp.message_handler(lambda message: message.text == 'воскресенье')
async def sunday(message: types.Message):
    if w == 1:
        await message.answer(db[message.from_user.id]['воскресенье'])
    if w == 2:
        await message.answer(db[message.from_user.id]['воскресенье'])
        await message.answer('''Напиши свое расписание:
1.
2.
3.
4.
5.
6.
7.
8.
 и тд.''')
        w = 9

@dp.message_handler(Text(startswith = '1.'))
async def timetable(message: types.Message):
    if w == 3:
        m = message.text
        db[message.from_user.id]['понедельник'] = m
        await message.answer('Расписание на этот день добавлено/изменено.')
    if w == 4:
        m = message.text
        db[message.from_user.id]['вторник'] = m
        await message.answer('Расписание на этот день добавлено/изменено.')
        w = 0
    if w == 5:
        m = message.text
        db[message.from_user.id]['среда'] = m
        await message.answer('Расписание на этот день добавлено/изменено.')
        w = 0
    if w == 6:
        m = message.text
        db[message.from_user.id]['четверг'] = m
        await message.answer('Расписание на этот день добавлено/изменено.')
        w = 0
    if w == 7:
         m = message.text
        db[message.from_user.id]['пятница'] = m
        await message.answer('Расписание на этот день добавлено/изменено.')
        w = 0
    if w == 8:
        m = message.text
        db[message.from_user.id]['суббота'] = m
        await message.answer('Расписание на этот день добавлено/изменено.')
        w = 0
    if w == 9:
        m = message.text
        db[message.from_user.id]['воскресенье'] = m
        await message.answer('Расписание на этот день добавлено/изменено.')
        w = 0


#@dp.callback_query_handler(Text(startswith = "l_"))
#async def callbacks_timetable(call: types.CallbackQuery):
#    action = call.data.split("_")[1]
#    if action == "1":
#        await call.message()
#    elif action == "2":
#        await call.message()
#    elif action == "3":
#        await call.message()
#    elif action == "4":
#        await call.message()
#    elif action == "5":
#        await call.message()
#    elif action == "6":
#        await call.message()
#    elif action == "7":
#        await call.message()
#    elif action == "8":
#        await call.message()

executor.start_polling(dp)