import telebot
from math import sqrt
from decimal import Decimal


def circle(message):
	r = float(message.text)
	pi = 3.14
	s = pi * r ** 2
	c = 2 * pi * r
	bot.send_message(message.from_user.id, f'Площадь: {s}')
	bot.send_message(message.from_user.id, f'Длина: {c}')


def square(message):
	n = Decimal(message.text)
	s = n ** 2
	p = n * 4
	bot.send_message(message.from_user.id, f'Площадь: {s}')
	bot.send_message(message.from_user.id, f'Периметр: {p}')


def rectangle(message):
	bruh = message.text.split()
	a = Decimal(bruh[0])
	b = Decimal(bruh[1])
	s = a * b
	p = a * 2 + b * 2
	d = sqrt(a ** 2 + b ** 2)
	bot.send_message(message.from_user.id, f'Площадь: {s}')
	bot.send_message(message.from_user.id, f'Периметр: {p}')
	bot.send_message(message.from_user.id, f'Диагональ: {d}')


def right_triangle(message):
	bruh = message.text.split()
	a = float(bruh[0])
	b = float(bruh[1])
	s = (a * b) / 2
	hypotenuse = sqrt(a ** 2 + b ** 2)
	p = a + b + hypotenuse
	bot.send_message(message.from_user.id, f'Площадь: {s}')
	bot.send_message(message.from_user.id, f'Периметр: {p}')
	bot.send_message(message.from_user.id, f'Гипотенуза: {hypotenuse}')


def degrees(message):
	n = int(message.text)
	e = 180 * (n - 2)
	bot.send_message(message.from_user.id, f'Сумма углов: {e}')


def diagonals(message):
	n = int(message.text)
	d = n * (n - 3) / 2
	bot.send_message(message.from_user.id, f'Количество диагоналей: {int(d)}')
