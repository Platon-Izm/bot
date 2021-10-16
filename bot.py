import telebot
from math import sqrt
from decimal import Decimal
#getting a token from a text file
file = open('token.txt', 'r', encoding='utf-8')
token = file.read()
file.close()
bot = telebot.TeleBot(token)
#start
@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['start'])

#command receive function
def get_text_messages(message):
    #redirect to 'get_figure'
    if message.text == '/figure':
		#keyboard
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        square = telebot.types.KeyboardButton("/square")
        circle = telebot.types.KeyboardButton("/circle")
        rectangle = telebot.types.KeyboardButton("/rectangle")
        right_triangle = telebot.types.KeyboardButton("/right_triangle")
		
        markup.add(square, circle, rectangle, right_triangle)
        bot.send_message(message.from_user.id, 'Какую фигуру разобрать?', reply_markup=markup)
        bot.register_next_step_handler(message, get_figure)
    #redirect to degrees function
    elif message.text=='/degrees':
        bot.send_message(message.from_user  .id, 'Введи число сторон')
        bot.register_next_step_handler(message, degrees)
    #redirect to diagonals function
    elif message.text=='/diagonals':
        bot.send_message(message.from_user.id, 'Введи число вершин')
        bot.register_next_step_handler(message, diagonals)
#get figure function
def get_figure(message):
	
    if message.text=='/circle':
        bot.send_message(message.from_user.id, 'Введи радиус',reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, circle)

    elif message.text=='/square':
        bot.send_message(message.from_user.id, "Введи длину стороны", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, square)
	
    elif message.text=='/rectangle':
        bot.send_message(message.from_user.id, "Введи длины сторон через пробел", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, rectangle)
    
    elif message.text=='/right_triangle':
        bot.send_message(message.from_user.id, "Введи длины сторон через пробел", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, right_triangle)

#circle function
def circle (message):
    #get the radius from the message
    r=float(message.text)
    #declaring the number pi
    pi=3.14
    #calculating the area of a circle
    s=pi*r**2
    #calculating the circumference
    c=2*pi*r
    #sending calculations
    bot.send_message(message.from_user.id, f'Площадь: {s}')
    bot.send_message(message.from_user.id, f'Длина: {c}')

#square function
def square(message):
    #getting the length of a side from a message
    n=Decimal(message.text)
    #area calculations
    s=n**2
    #perimeter calculation
    p=n*4
    #sending calculations
    bot.send_message(message.from_user.id, f'Площадь: {s}')
    bot.send_message(message.from_user.id, f'Периметр: {p}')

#rectangle function
def rectangle(message):
    bruh=message.text.split()
    #getting length and width from message
    a=Decimal(bruh[0])
    b=Decimal(bruh[1])
    #area calculation
    s=a*b
    #calculating the perimeter
    p=a*2+b*2
    #diagonal calculations
    d=sqrt(a**2+b**2)
    #sending calculations
    bot.send_message(message.from_user.id, f'Площадь: {s}')
    bot.send_message(message.from_user.id, f'Периметр: {p}')
    bot.send_message(message.from_user.id, f'Диагональ: {d}')

#right_triangle function
def right_triangle(message):
    bruh=message.text.split()
    #getting length and width from message
    a=float(bruh[0])
    b=float(bruh[1])
    #area calculation
    s=(a*b)/2
    #hypotenuse calculating
    hypotenuse=sqrt(a**2+b**2)
    #perimeter calculation
    p=a+b+hypotenuse
    #sending calculations
    bot.send_message(message.from_user.id, f'Площадь: {s}')
    bot.send_message(message.from_user.id, f'Периметр: {p}')
    bot.send_message(message.from_user.id, f'Гипотенуза: {hypotenuse}')

#degrees function
def degrees(message):
    #getting the number of parties from a message
    n=int(message.text)
    #calculating the number of degrees
    e=180*(n-2)
    #sending calculations
    bot.send_message(message.from_user.id, f'Сумма углов: {e}')

#diagonal function
def diagonals(message):
    #getting the number of parties from a message
    n=int(message.text)
    #calculating the number of diagonals
    d=n*(n-3)/2
    #sending calculations
    bot.send_message(message.from_user.id, f'Количество диагоналей: {int(d)}')

#run
bot.polling(none_stop=True)
