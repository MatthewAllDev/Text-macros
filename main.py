import keyboard
import configparser


def ret(data):
    keyboard.write(data)


def read_commands_in_configuration():
    config = configparser.ConfigParser()
    config.read_file(open('settings.ini', 'r', encoding="utf-8"))
    return dict(config['Commands'])


commands = read_commands_in_configuration()

keyboard.add_hotkey('Ctrl + 0', lambda: ret(commands['command_0']))
keyboard.add_hotkey('Ctrl + 1', lambda: ret(commands['command_1']))
keyboard.add_hotkey('Ctrl + 2', lambda: ret(commands['command_2']))
keyboard.add_hotkey('Ctrl + 3', lambda: ret(commands['command_3']))
keyboard.add_hotkey('Ctrl + 4', lambda: ret(commands['command_4']))
keyboard.add_hotkey('Ctrl + 5', lambda: ret(commands['command_5']))
keyboard.add_hotkey('Ctrl + 6', lambda: ret(commands['command_6']))
keyboard.add_hotkey('Ctrl + 7', lambda: ret(commands['command_7']))
keyboard.add_hotkey('Ctrl + 8', lambda: ret(commands['command_8']))
keyboard.add_hotkey('Ctrl + 9', lambda: ret(commands['command_9']))

print('The macros module launched. To exit, press Ctrl + Q. \nThe current values of macros:')
for iterator in range(9):
    print('Ctrl + ' + str(iterator) + ': ' + commands['command_' + str(iterator+1)])
print('Ctrl + 0: ' + commands['command_0'])
print('You can configure macros in the file "settings.ini".')

keyboard.wait('ctrl + Q')
