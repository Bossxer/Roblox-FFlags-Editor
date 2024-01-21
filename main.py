#imports
import json
import os
from Internal import *
from colorama import just_fix_windows_console
from termcolor import colored
import time
import pathlib
import ctypes

#setup
just_fix_windows_console()
function.CTitle("FFlag Editor - Stable")
function.setup()
selected_fflags = []

try:
    with open(pathlib.Path(os.getenv('LOCALAPPDATA')) / 'Roblox/Versions/' / function.find_latest_modified_folder(pathlib.Path(os.getenv('LOCALAPPDATA')) / 'Roblox/Versions') / 'ClientSettings/ClientAppSettings.json', "r") as outfile:
        print("Opened ClientSettings folder")
except:
    print(colored("Failed to open ClientSettings folder, creating it.", "red"))
    pathlib.Path(pathlib.Path(os.getenv('LOCALAPPDATA')) / 'Roblox/Versions/' / function.find_latest_modified_folder(pathlib.Path(os.getenv('LOCALAPPDATA')) / 'Roblox/Versions') / 'ClientSettings').mkdir(parents=True, exist_ok=False)

if __name__ == "__main__":
    function.main(selected_fflags)
