from aiogram import Bot, types, Dispatcher, executor, types
from markup import keyboard, keyboard2, markup, helpKeyboard
from mg import get_map_cell
from anekdot import list_of_jokes
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
cols, rows = 8, 8

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    sti = open('static/AnimatedSticker7.tgs', 'rb')
    await bot.send_sticker(message.chat.id, sti)

    await bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b> {1.first_name} </b>, игровой бот.".format(
                         message.from_user, await bot.get_me()), parse_mode='html', reply_markup=markup)

maps = {}

def get_map_str(map_cell, player):
    map_str = ""
    for y in range(rows * 2 - 1):
        for x in range(cols * 2 - 1):
            if map_cell[x + y * (cols * 2 - 1)]:
                map_str += "⬛"
            elif (x, y) == player:
                map_str += "🔴"
            else:
                map_str += "⬜"
        map_str += "\n"

    return map_str

@dp.message_handler(content_types=['text'])
async def play_maze(message):
    map_cell = get_map_cell(cols, rows)

    user_data = {
        'map': map_cell,
        'x': 0,
        'y': 0
    }

    maps[message.chat.id] = user_data

    if message.chat.type == 'private':
        if message.text == 'Maze Game':
            await bot.send_message(message.from_user.id, get_map_str(map_cell, (0, 0)), reply_markup=keyboard)
        elif message.text == 'Help':
            await bot.send_message(message.chat.id, 'Это помощь', reply_markup=helpKeyboard)
        elif message.text == 'Anekdot':
            await bot.send_message(message.chat.id, 'Здравствуйте! Чтобы посмеяться введите любую цифру:')
        elif message.text == 'Back':
            await bot.send_message(message.chat.id, 'Back', reply_markup=markup)

    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]

@dp.callback_query_handler(lambda call: True)
async def callback_func(query: types.CallbackQuery):
    user_data = maps[query.message.chat.id]
    new_x, new_y = user_data['x'], user_data['y']

    if query.data == 'left':
        new_x -= 1
    if query.data == 'right':
        new_x += 1
    if query.data == 'up':
        new_y -= 1
    if query.data == 'down':
        new_y += 1

    if new_x < 0 or new_x > 2 * cols - 2 or new_y < 0 or new_y > rows * 2 - 2:
        return None
    if user_data['map'][new_x + new_y * (cols * 2 - 1)]:
        return None

    user_data['x'], user_data['y'] = new_x, new_y

    if new_x == cols * 2 - 2 and new_y == rows * 2 - 2:
        await bot.edit_message_text( chat_id=query.message.chat.id,
                               message_id=query.message.message_id,
                               text="Вы выиграли" )
        return None

    await bot.edit_message_text( chat_id=query.message.chat.id,
                           message_id=query.message.message_id,
                           text=get_map_str(user_data['map'], (new_x, new_y)),
                           reply_markup=keyboard)


@dp.message_handler()
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
