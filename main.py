import os
import ast
import json
import configparser

from os import system
from colorama import Fore, Back, Style, init

class Config:
	config_path = "config.ini"
	configparser = configparser.ConfigParser(allow_no_value = True, interpolation = None)

	@staticmethod
	def get(block, name):
		Config.configparser.read(Config.config_path, encoding='utf-8')
		try:
			result = Config.configparser.get(block, name)
			return(result)
		except:
			return(False)

	@staticmethod
	def set(block, name, value):
		Config.configparser.read(Config.config_path, encoding='utf-8')
		Config.configparser.set(block, name, value)
		with open(Config.config_path, "w") as config_file:
			Config.configparser.write(config_file)

class Helper:
	@staticmethod
	def error_print(text):
		print(Fore.RED + text + Style.RESET_ALL)

	@staticmethod
	def error_exit(text):
		print(Fore.RED + " " + text + "\n" + Style.RESET_ALL)
		input(" ENTER TO EXIT\n")
		sys.exit()

	def readFile(path):
		if os.path.isfile(path):
			result = []
			with open(path, 'r', encoding = 'utf-8', errors = 'ignore') as file_in:
				result.append(file_in.read())
			return(result)

class ProductFilter():
	def __init__(self, key_list, file_path):
		self.key_list = key_list
		self.file_path = file_path

	def start(self):
		files = os.listdir(self.file_path)
		c = 1
		for filename in files:
			file = Helper.readFile(self.file_path + filename)
			for item in file:
				param_products = ast.literal_eval(item)
				for pr in param_products:
					finding = [el for el in self.key_list if str(el) in str(pr['productCode'])]
					if finding:
						print(Fore.WHITE + "("+str(c)+")" + Fore.GREEN + " Name: " + Fore.WHITE + "'" + pr['name'] + "'" + Fore.GREEN + "  Product code: " + Fore.CYAN + str(pr['productCode']) + Fore.GREEN + "  Price: " + Fore.WHITE + str(pr['price']) +" "+ pr['currency'])
						c += 1
		system(f"title RESULT: TOTAL FOUND {str(c)} ")
if __name__ == '__main__':
	init()
	if os.name == "nt":
		os.system('cls')
		system(f"title Software for check .json() file \\ especially for LiteSoft Agency")
	else:
		os.system('clear')
	title = f"""
	╔═══╗╔═══╗╔══╗╔══╗ ╔╗╔╗╔══╗╔════╗   ╔══╗╔══╗╔╗  ╔════╗╔═══╗╔═══╗
	║╔═╗║║╔═╗║║╔╗║║╔╗╚╗║║║║║╔═╝╚═╗╔═╝   ║╔═╝╚╗╔╝║║  ╚═╗╔═╝║╔══╝║╔═╗║
	║╚═╝║║╚═╝║║║║║║║╚╗║║║║║║║    ║║     ║╚═╗ ║║ ║║    ║║  ║╚══╗║╚═╝║
	║╔══╝║╔╗╔╝║║║║║║ ║║║║║║║║    ║║     ║╔═╝ ║║ ║║    ║║  ║╔══╝║╔╗╔╝
	║║   ║║║║ ║╚╝║║╚═╝║║╚╝║║╚═╗  ║║     ║║  ╔╝╚╗║╚═╗  ║║  ║╚══╗║║║║ 
	╚╝   ╚╝╚╝ ╚══╝╚═══╝╚══╝╚══╝  ╚╝     ╚╝  ╚══╝╚══╝  ╚╝  ╚═══╝╚╝╚╝ 
"""
	print(Fore.GREEN + str(title) + Style.RESET_ALL)

	if not os.path.isfile("config.ini"):
		Help.error_exit("ERROR: 'config.ini' - file does not exist")

	keys = Config.get('SETTINGS', 'key')
	key_list = ast.literal_eval(keys)
	file_path = Config.get('PATH', 'file_path')

	if key_list == "":
		Help.error_exit("ERROR: 'config.ini' | [SETTINGS] key - can't be empty")
	if file_path == "":
		Help.error_exit("ERROR: 'config.ini' | [SETTINGS] file_path - can't be empty")

	print(Fore.WHITE + f" [INFO] SEARCH BY: {Fore.CYAN + keys + Style.RESET_ALL}")
	print(Fore.WHITE + f" [INFO] TOTAL FILES: {Fore.CYAN + str(len(key_list)) + Style.RESET_ALL}")
	print(Fore.WHITE + f" [INFO] FILE PATH: {Fore.CYAN + file_path + Style.RESET_ALL}")
	action = int(input(
		Fore.GREEN + "\n 	[SELECT ACTION]\n" + Style.RESET_ALL  + \
		Fore.GREEN + " [1]" + Style.RESET_ALL + " - START CHECK\n" + \
		Fore.GREEN + " ->  " + Style.RESET_ALL))

	if action == 1:
		soft = ProductFilter(key_list, file_path)
		soft.start()

	input(" PRESS ENTER TO EXIT")

# dev t.me/cayse