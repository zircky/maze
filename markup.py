from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup()
keyboard.row( InlineKeyboardButton('←', callback_data='left'),
			  InlineKeyboardButton('↑', callback_data='up'),
			  InlineKeyboardButton('↓', callback_data='down'),
			  InlineKeyboardButton('→', callback_data='right') )

keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True)
td = KeyboardButton("Maze")
back = KeyboardButton("Back")
keyboard2.add(td, back)

markup = ReplyKeyboardMarkup(resize_keyboard=True)
maze_game = KeyboardButton("Maze Game")
help = KeyboardButton("Help")
anekdot = KeyboardButton("Anekdot")

markup.add(tank_game, maze_game, help, anekdot)