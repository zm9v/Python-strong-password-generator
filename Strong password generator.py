import random
import colorama
from colorama import *
List = 'QWERTYUIOPASDFGHJKLZX&CVBNMqwertyuiopasdfghjklzxcvbnm0123456789$!.-_£'
Number_of_characters = input(f'{Fore.RED}Length of the password : ')
try:
    Pass = random.choices(List, k=int(Number_of_characters))
    print(f'{Fore.RED}Your password : {"".join(Pass)}')
    print(f'{Fore.RED}Done :)')
    input(f'{Fore.RED}Press enter to close...')
except:
    print(f'{Fore.RED}invaild input :(')
    input(f'{Fore.RED}Press enter to close...')
