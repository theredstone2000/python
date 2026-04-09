from pynput import keyboard
from datetime import datetime, timedelta
import ctypes
import time
# Liste des heures cibles
TARGETS = [
    "08:20", "09:15", "10:10", "10:25", "11:20", "12:15", 
    "13:45", "14:40", "15:35", "15:50", "16:45", "17:40"
]
TARGETS2 = ["9:42", "10:35"]
TARGETS3 = ["00:00", "01:01", "02:02", "03:03", "04:04", "05:05", "06:06", "07:07", "08:08", "09:09", "10:10", "11:11", "12:12", "13:13", "14:14", "15:15", "16:16", "17:17", "18:18", "19:19", "20:20", "21:21", "22:22", "23:23"]
shift_pressed = False
def get_target_datetimes(TARGETS):
    """Convertit les heures en datetime du jour ou demain si déjà passées."""
    now = datetime.now()
    targets = []
    for t in TARGETS:
        h, m = map(int, t.split(":"))
        target = now.replace(hour=h, minute=m, second=0, microsecond=0)
        if target < now:
            target += timedelta(days=1)
        targets.append((t, target))
    return targets


def show_popup(message):
    """Affiche un popup Windows toujours au-dessus de tout (même plein écran)."""
    MB_TOPMOST = 0x00040000 # Force la fenêtre au-dessus de tout
    MB_OK = 0x0
    ctypes.windll.user32.MessageBoxW(0, message, "Temps restant", MB_OK | MB_TOPMOST)
def on_press(key):  # sourcery skip: extract-duplicate-method
    global shift_pressed
    if key in [keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r]:
        shift_pressed = True
    elif key == keyboard.Key.f1 and shift_pressed:
        now = datetime.now()
        targets = get_target_datetimes(TARGETS)
        diffs = [(name, (time - now).total_seconds()) for name, time in targets]
        nearest = min(diffs, key=lambda x: abs(x[1]))
        name, seconds = nearest
        minutes = int(seconds // 60)
        sec = int(seconds % 60)
        msg = f"Prochaine heure : {name}\nTemps restant : {minutes} min {sec} sec"
        show_popup(msg)
    elif key == keyboard.Key.f2 and shift_pressed:
        now = datetime.now()
        targets = get_target_datetimes(TARGETS2)
        diffs = [(name, (time - now).total_seconds()) for name, time in targets]
        nearest = min(diffs, key=lambda x: abs(x[1]))
        name, seconds = nearest
        minutes = int(seconds // 60)
        sec = int(seconds % 60)
        msg = f"Prochaine heure : {name}\nTemps restant : {minutes} min {sec} sec"
        show_popup(msg)
    elif key == keyboard.Key.f3 and shift_pressed:
        now = datetime.now()
        targets = get_target_datetimes(TARGETS3)
        diffs = [(name, (time - now).total_seconds()) for name, time in targets]
        nearest = min(diffs, key=lambda x: abs(x[1]))
        name, seconds = nearest
        minutes = int(seconds // 60)
        sec = int(seconds % 60)
        msg = f"Prochaine heure : {name}\nTemps restant : {minutes} min {sec} sec"
        show_popup(msg)

def on_release(key):
    global shift_pressed
    if key in [keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r]:
        shift_pressed = False
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
print("Appuie sur Shift + F1 pour afficher le popup…")
listener.join()
while True:
    now = datetime.strftime(datetime.now(),"%H:%M")
    h, m = map(int, now.split(":"))
    if h == m:
        msg = f"il est {now} !"
        show_popup(msg)
    time.sleep(60)
