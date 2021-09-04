# Ethernal Api Source

import time
import colorama

from past.builtins import raw_input
from modules.commands import Commands
from modules.adminLogin import adminlog

loaded, adminLogged = False
na = {}

colorama.init(autoreset=True, convert=True)

print(colorama.Fore.LIGHTYELLOW_EX + "Ethernal API - Version 1.0\n \nType 'help', 'info' for more \n")


# List to string
def listtostring(s):
    str1 = " "
    return str1.join(s)


while True:
    com = str(raw_input("> "))
    text = com.split()
    if text[0] == 'help' and loaded == False:
        print("print <Text> - print the text"
              "\nmath <Expression> - calculator, example - math 1 + 1"
              "\nhelp - show all available commands"
              "\ninfo - show information"
              "\nload - load additional commands and signatures"
              "\nexit - exit from app")

    elif text[0] == 'help' and loaded == True:
        print("print <Text> - print the text"
              "\nmath <Expression> - calculator, example - math 1 + 1"
              "\nhelp - show all available commands"
              "\ninfo - show information"
              "\nunload - unload additional commands and signatures"
              "\nexec - execute script, for tabulation use '\\n\\t'"
              "\nexecs - you can write your script, and execute his with '/end'"
              "\nadmin - you can switch to admin"
              "\ndebug - enable debug mod"
              "\nexit - exit from app")

    # com - info
    elif text[0] == 'info':
        print(colorama.Fore.LIGHTYELLOW_EX + "Ethernal API - Version 1.0, ")
        # holder

    # com - math
    elif text[0] == 'math':
        x = float(text[1])
        o = str(text[2])
        y = float(text[3])

        if o == '+':
            out = x + y
            print(x, o, y, '=', out)
        if o == '-':
            out = x - y
            print(x, o, y, '=', out)
        if o == '*':
            out = x * y
            print(x, o, y, '=', out)
        if o == '/':
            if y != 0:
                out = x + y
                print(x, o, y, '=', out)
            else:
                print(colorama.Fore.RED + "Error - ZeroDivision")

    # com - print
    elif text[0] == 'print':
        print(listtostring(text[1:]))
        print('')

    # com - exec
    elif text[0] == 'exec' and loaded:
        esc = ''
        command = input("/> ")
        csa = {}
        if command == 'echo off':
            while True:
                command = input("/> ")
                if command == 'echo on':
                    try:
                        print(f"\n{colorama.Fore.LIGHTYELLOW_EX}Execution Output:\n")
                        exec(esc, csa, csa)
                        print("")
                        break
                    except:
                        print(colorama.Fore.RED + "Error corrupted while compiling")
                        break
                elif command != 'echo on':
                    esc += command + '\n'
        else:
            try:
                exec(command, csa, csa)
            except:
                print(colorama.Fore.RED + "Error corrupted while compiling -")

    elif text[0] == 'exec' and not loaded:
        print(colorama.Fore.RED + "Error - Signatures not loaded, type 'load'!")

    elif text[0] == 'execs' and not loaded:
        print(colorama.Fore.RED + "Error - Signatures not loaded, type 'load'!")

    # com - load
    elif text[0] == 'load':
        print(colorama.Fore.LIGHTYELLOW_EX + "loading...")
        time.sleep(1)
        print(colorama.Fore.GREEN + "\nAdditional Signatures are loaded")
        loaded = True

    # com - unload
    elif text[0] == 'unload':
        print(colorama.Fore.LIGHTYELLOW_EX + "unloading...")
        time.sleep(1)
        print(f"\n{colorama.Fore.GREEN}Additional Signatures are loaded")
        loaded = False

    # com - admin
    elif text[0] == 'admin' and loaded:
        if not adminLogged:
            adminLogged = adminlog()
            if adminLogged:
                print(colorama.Fore.GREEN + "Successfully Loged in")
            else:
                print(colorama.Fore.RED + "Error - not logged")
        elif adminLogged:
            adminLogged = False

    elif text[0] == 'admin' and not loaded:
        print(colorama.Fore.RED + "Error - Signatures not loaded, type 'load'!")

    # com - exit
    elif text[0] == 'exit':
        input(colorama.Fore.RED + "You are sure?")
        break

    # com - debug
    elif text[0] == 'debug' and loaded and adminLogged:
        esc = ''
        command = input("/> ")
        if command == 'echo off':
            while True:
                command = input("echo/> ")
                if command == 'echo on':
                    try:
                        print(f"\n{colorama.Fore.LIGHTYELLOW_EX}Execution Output:\n")
                        exec(esc)
                        print("")
                        break
                    except:
                        print(colorama.Fore.RED + "Error corrupted while compiling")
                        break
                elif command != 'echo on':
                    esc += command + '\n'
        else:
            try:
                exec(command)
            except:
                print(colorama.Fore.RED + "Error corrupted while compiling -")

    elif text[0] == 'debug' and not loaded and not adminLogged:
        print(
            colorama.Fore.RED + "Error - Signatures not loaded and your not logged as admin, type 'load' and 'admin'!")

    elif text[0] == 'file':
        print("File interaction console, type 'help'")
        while True:
            ccom = str(raw_input("file/> "))
            texts = ccom.split()
            if ccom == 'help':
                print("open <filePath> - open file, and write him into variable")
            elif texts[0] == 'open':
                fp = texts[1]
                of = open(fp, 'r')

                while True:
                    cc = input("file/"+fp+"/>")
                    if cc == 'read':
                        print(of.read())

                    elif cc == 'execute':
                        exec(of.read(), na, na)

                    elif cc == 'exit':
                        break

            elif ccom == 'exit':
                break

    # coms from modules.commands
    else:
        Commands.mainc(text, loaded, adminLogged)
