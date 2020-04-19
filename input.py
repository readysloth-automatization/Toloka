from pynput import keyboard

keyboard_controller = keyboard.Controller()
def press_once(key):
    keyboard_controller.press(key)
    keyboard_controller.release(key)

def conditional_press(if_true = None, if_false = None, another = None):
    def on_keypress(key):
        if key == keyboard.Key.esc:
            raise keyboard.Listener.StopException
        if key == keyboard.Key.enter:
            another()
        if not hasattr(key, 'char'):
            return
        if key.char == 'j':
            press_once('1')
        elif key.char == 'k':
            press_once('2')
        else:
            return
        press_once(keyboard.Key.down)
    return on_keypress

def start_listening(keypress_handler):
    with keyboard.Listener(on_press=keypress_handler) as listner:
        listner.join()


