from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from anekdot import URL

keyboard = InlineKeyboardMarkup()
keyboard.row( InlineKeyboardButton('←', callback_data='left'),
			  InlineKeyboardButton('↑', callback_data='up'),
			  InlineKeyboardButton('↓', callback_data='down'),
			  InlineKeyboardButton('→', callback_data='right') )

keyboard2 = InlineKeyboardMarkup()
maze = InlineKeyboardButton('Maze', url='https://ru.wikipedia.org/wiki/Лабиринт_(жанр)')
#back = InlineKeyboardButton('Back', callback_data=)
keyboard2.add(maze)

markup = ReplyKeyboardMarkup(resize_keyboard=True)
maze_game = KeyboardButton("Maze Game")
help = KeyboardButton("Help")
anekdot = KeyboardButton("Anekdot")
out = KeyboardButton("Out")

markup.add(maze_game, help, anekdot, out)