from pynput import keyboard

def conditional_press(if_true, if_false):
    def on_keypress(key):
        if not hasattr(key, 'char'):
            return
        if key.char == 'j':
            if_true()
        elif key.char == 'k':
            if_false()
    return on_keypress

def start_listening(keypress_handler):
    with keyboard.Listener(on_press=keypress_handler) as listner:
        listner.join()


