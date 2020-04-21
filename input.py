from pynput import keyboard

keyboard_controller = keyboard.Controller()


def raiser(e):
    raise e


def press_multiple(*keys):
    for key in keys:
        press_once(key)


def press_once(key):
    keyboard_controller.press(key)
    keyboard_controller.release(key)


def conditional_press(function_dict):
    def on_keypress(key):
        switch = {
            keyboard.Key.esc: lambda: raiser(keyboard.Listener.StopException),
            keyboard.Key.enter: function_dict[keyboard.Key.enter],
            'char': {
                'j': lambda: press_multiple('1', keyboard.Key.down),
                'k': lambda: press_multiple('2', keyboard.Key.down),
                'J': lambda: press_multiple(keyboard.Key.up, '1', keyboard.Key.down),
                'K': lambda: press_multiple(keyboard.Key.up, '2', keyboard.Key.down),
            }
        }

        if key in switch:
            switch[key]()
        if hasattr(key, 'char') and key.char in switch['char']:
            switch['char'][key.char]()
    return on_keypress


def start_listening(keypress_handler):
    with keyboard.Listener(on_press=keypress_handler) as listner:
        listner.join()
