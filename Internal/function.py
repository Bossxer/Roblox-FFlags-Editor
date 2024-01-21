import json
import os
from colorama import just_fix_windows_console
from termcolor import colored
import time
import pathlib
import ctypes


def add_fflag(table):
    os.system('cls')
    setup()
    flag_table = []
    for i, flag in enumerate(json.load(open("Internal/FFlags.json"))):
        flag_table.append(f"{i+1}.{flag}")
        print(f"{i+1}.{flag}")
    print(colored("Please select an Flag to add(Or Exit to go back): ", "white"))
    option = input("Option: ")
    if option == "Exit" or option == "exit":
        edit_fflags(table)
    elif int(option) < 1 or int(option) > len(flag_table):
        print(colored("Invalid Option", "red"))
        time.sleep(0.75)
        add_fflag(table)
    else:
        table.append(flag_table[int(option)-1].split(".")[1])
        print(table)
        time.sleep(0.75)
        add_fflag(table)

def remove_fflag(table):
    os.system('cls')
    setup()
    remove_table = []
    for i, flag in enumerate(table):
        remove_table.append(f"{i+1}.{flag}")
        print(f"{i+1}.{flag}")
    print(colored("Please select an Flag to remove(Or Exit to go back): ", "white"))
    option = input("Option: ")
    if option == "Exit" or option == "exit":
        edit_fflags(table)
    elif int(option) < 1 or int(option) > len(remove_table):
        print(colored("Invalid Option", "red"))
        time.sleep(0.75)
        edit_fflags(table)
    else:
        table.remove(remove_table[int(option)-1].split(".")[1])
        print(table)
        time.sleep(0.75)
        remove_fflag(table)

def add_fflag_to_file(table):
    os.system('cls')
    setup()
    updated_fflags = {}
    for flag in table:
        updated_fflags.update(json.load(open("Internal/FFlags.json"))[flag])
    with open(pathlib.Path(os.getenv('LOCALAPPDATA')) / 'Roblox/Versions/' / find_latest_modified_folder(pathlib.Path(os.getenv('LOCALAPPDATA')) / 'Roblox/Versions') / 'ClientSettings/ClientAppSettings.json', "w") as outfile:
        outfile.write(json.dumps(updated_fflags, indent=2))
    print(colored("Added FFlags to file", "green"))
    time.sleep(0.75)
    edit_fflags(table)

def edit_fflags(table):
    os.system('cls')
    setup()
    print(colored("Please select an option(type the number)", "white"))
    print(colored("1. Add FFlag", "blue"))
    print(colored("2. Remove FFlag", "light_blue"))
    print(colored("3. Add FFlag to file", "light_cyan"))
    print(colored("4. Clear FFlags", "white"))
    print(colored("5. Exit", "red"))
    option = input("Option: ")
    if option == "1":
        add_fflag(table)
    elif option == "2":
        remove_fflag(table)
    elif option == "3":
        add_fflag_to_file(table)
    elif option == "4":
        open(pathlib.Path(os.getenv('LOCALAPPDATA')) / 'Roblox/Versions/' / find_latest_modified_folder(pathlib.Path(os.getenv('LOCALAPPDATA')) / 'Roblox/Versions') / 'ClientSettings/ClientAppSettings.json', "w").close()
        print(colored("Cleared FFlags", "green"))
        time.sleep(0.75)
        edit_fflags(table)
    elif option == "5":
        main(table)


def find_latest_modified_folder(versions_folder):

    latest_modified_folder = ""
    latest_modified_time = 0

    for file_name in os.listdir(versions_folder):
        file_path = os.path.join(versions_folder, file_name)
        modification_time = os.path.getmtime(file_path)

        if modification_time > latest_modified_time:
            latest_modified_time = modification_time
            latest_modified_folder = file_path

    return latest_modified_folder

def main(table):
    os.system('cls')
    setup()
    print(colored("Please select an option(type the name)", "white"))
    print(colored("1. Edit FFlags", "light_blue"))
    print(colored("2. Default FFlags", "light_cyan"))
    print(colored("3. Exit", "red"))

    option = input("Option: ")
    if option == "1":
        edit_fflags(table)
    if option == "2":
        with open(pathlib.Path(os.getenv('LOCALAPPDATA')) / 'Roblox/Versions/' / find_latest_modified_folder(pathlib.Path(os.getenv('LOCALAPPDATA')) / 'Roblox/Versions') / 'ClientSettings/ClientAppSettings.json', "w") as outfile:
            outfile.write(json.dumps(json.load(open("Internal/FFlags.json"))["Default"], indent=2))
        print(colored("Default FFlags set", "green"))
        time.sleep(2.5)
        main(table)
    if option == "3":
        exit(table)


def CTitle(t):
    ctypes.windll.kernel32.SetConsoleTitleW(t)


def setup():
    print(colored("█████ █████ █      ███   ████     █████ ████  █████ █████  ███  ████  ", "blue", attrs=["bold"]))
    print(colored("█     █     █     █   █ █         █     █   █   █     █   █   █ █   █ ", "blue", attrs=["bold"]))
    print(colored("████  ████  █     █████ █  ██     ████  █   █   █     █   █   █ ████  ", "blue"))
    print(colored("█     █     █     █   █ █   █     █     █   █   █     █   █   █ █   █ ", "blue" ))
    print(colored("█     █     █████ █   █  ███      █████ ████  █████   █    ███  █   █ ", "blue"))
    print(colored("Alpha", "yellow"))