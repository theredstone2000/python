from pynput import keyboard, mouse
import pynput, keyboard
import threading
import nbtlib
import json
import os

helper = 0
shift_pressed = False
shift_f6 = False
list_of_key = []
def on_press(key):
    global shift_f6
    global shift_pressed
    global list_of_key
    if key in [pynput.keyboard.Key.f6]:
        shift_f6 = shift_f6.__xor__(1)
    if key in [pynput.keyboard.Key.shift, pynput.keyboard.Key.shift_l, pynput.keyboard.Key.shift_r]:
        shift_pressed = True
    elif key == pynput.keyboard.Key.num_lock:  #spam_click
        spam_click = mouse.Controller()
        spam_click.click(mouse.Button.left, 1500)
    elif key == pynput.keyboard.Key.f4 and shift_pressed:  #spam copy and paste
        ctrlc = pynput.keyboard.Controller()
        ctrlc.press(pynput.keyboard.Key.ctrl)
        ctrlc.tap("c")
        for i in range (750):
            ctrlc.tap("v")
        ctrlc.release(pynput.keyboard.Key.ctrl)
    if shift_f6:
        list_of_key = keyboard.record()
        
        typed = keyboard.get_typed_strings(list_of_key)
        
def on_mouse_press(x, y, button, pressed, injected):
    return


listener = pynput.keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_mouse_press)
mouse_listener.start()

listener.start()


listener.join()

