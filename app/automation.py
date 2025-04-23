import os

def execute_automation(command):
    if "lights" in command:
        os.system("python3 light_control.py")