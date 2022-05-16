from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from anekdot import URL

keyboard = InlineKeyboardMarkup()
keyboard.row( InlineKeyboardButton('←', callback_data='left'),
			  InlineKeyboardButton('↑', callback_data='up'),
			  InlineKeyboardButton('↓', callback_data='down'),
			  InlineKeyboardButton('→', callback_data='right') )

helpKeyboard = InlineKeyboardMarkup()
td = InlineKeyboardButton('Maze', url='https://ru.wikipedia.org/wiki/Лабиринт_(жанр)')
#back = InlineKeyboardButton('Back')
helpKeyboard.add(td)

keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True)
#td = KeyboardButton("Maze")
back = KeyboardButton("Back")
keyboard2.add( back)

markup = ReplyKeyboardMarkup(resize_keyboard=True)
maze_game = KeyboardButton("Maze Game")
help = KeyboardButton("Help")
anekdot = KeyboardButton("Anekdot")

markup.add(maze_game, help, anekdot)