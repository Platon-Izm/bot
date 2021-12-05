import telebot
from deductions import circle, square, rectangle, right_triangle, degrees, diagonals

# getting a token from a text file
file = open('token.txt', 'r', encoding='utf-8')
token = file.read()
file.close()
bot = telebot.TeleBot(token)


# start
@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['start'])
# command receive function
def get_text_messages(message):
	# redirect to 'get_figure'
	if message.text == '/figure':
		# keyboard
		markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
		square = telebot.types.KeyboardButton("/square")
		circle = telebot.types.KeyboardButton("/circle")
		rectangle = telebot.types.KeyboardButton("/rectangle")
		right_triangle = telebot.types.KeyboardButton("/right_triangle")

		markup.add(square, circle, rectangle, right_triangle)
		bot.send_message(message.from_user.id, 'Какую фигуру разобрать?', reply_markup=markup)
		bot.register_next_step_handler(message, get_figure)
	# redirect to degrees function
	elif message.text == '/degrees':
		bot.send_message(message.from_user.id, 'Введи число сторон')
		bot.register_next_step_handler(message, degrees)
	# redirect to diagonals function
	elif message.text == '/diagonals':
		bot.send_message(message.from_user.id, 'Введи число вершин')
		bot.register_next_step_handler(message, diagonals)


# get figure function
def get_figure(message):
	if message.text == '/circle':
		bot.send_message(message.from_user.id, 'Введи радиус', reply_markup=telebot.types.ReplyKeyboardRemove())
		bot.register_next_step_handler(message, circle)

	elif message.text == '/square':
		bot.send_message(message.from_user.id, "Введи длину стороны", reply_markup=telebot.types.ReplyKeyboardRemove())
		bot.register_next_step_handler(message, square)

	elif message.text == '/rectangle':
		bot.send_message(message.from_user.id, "Введи длины сторон через пробел",
						 reply_markup=telebot.types.ReplyKeyboardRemove())
		bot.register_next_step_handler(message, rectangle)

	elif message.text == '/right_triangle':
		bot.send_message(message.from_user.id, "Введи длины сторон через пробел",
						 reply_markup=telebot.types.ReplyKeyboardRemove())
		bot.register_next_step_handler(message, right_triangle)


# run
bot.polling(none_stop=True)
