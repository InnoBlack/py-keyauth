# import everything
from math import exp, fabs
from unicodedata import category
from keyauth import api
import os
import time
import colorama
import sys
import platform
import hashlib



colorama.init()


if sys.version_info.minor < 10:
    print("[Security] - Python 3.10 or higher is recommended. The bypass will not work on 3.10+")
    print("You are using Python {}.{}".format(sys.version_info.major, sys.version_info.minor))

if platform.system() == 'Windows':
    os.system('cls & title keyauth system')
elif platform.system() == 'Linux':
    os.system('clear')
    sys.stdout.write("\x1b]0;Python Example\x07")
elif platform.system() == 'Darwin':
    os.system("clear && printf '\e[3J'")
    os.system('''echo - n - e "\033]0;Python Example\007"''')

print("Initializing")


def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "",
    ownerid = "",
    secret = "",
    version = "1.0",
    hash_to_check = getchecksum()
)

print(f"""
App data:
{colorama.Fore.LIGHTCYAN_EX}Number of users: {keyauthapp.app_data.numUsers}
{colorama.Fore.LIGHTMAGENTA_EX}Number of online users: {keyauthapp.app_data.onlineUsers}
{colorama.Fore.LIGHTBLUE_EX}Number of keys: {keyauthapp.app_data.numKeys}
{colorama.Fore.LIGHTGREEN_EX}Application Version: {keyauthapp.app_data.app_ver}
""")
print(f"{colorama.Fore.LIGHTRED_EX}Blacklisted? : {keyauthapp.checkblacklist()}")  # check if blacklisted, you can edit this and make it exit the program if blacklisted


def answer():
    try:
        print(f"""{colorama.Fore.LIGHTWHITE_EX}
1.Login
2.Register
        """)
        ans = input("Select Option: ")
        if ans == "1":
            user = input('Provide username: ')
            password = input('Provide password: ')
            keyauthapp.login(user, password)
        elif ans == "2":
            user = input('Provide username: ')
            password = input('Provide password: ')
            license = input('Provide License: ')
            keyauthapp.register(user, password, license)
        else:
            print("\nNot Valid Option")
            time.sleep(1)
            os.system('cls')
            answer()
    except KeyboardInterrupt:
        os._exit(1)


answer()


