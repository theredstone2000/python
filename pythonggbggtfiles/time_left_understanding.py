
from pynput import keyboard
from datetime import datetime, timedelta
import ctypes

# Liste des heures cibles
TARGETS = [
    "08:20", "09:15", "10:10", "10:25", "11:20", "12:15", 
    "13:45", "14:40", "15:35", "15:50", "16:45", "17:40"
]

shift_pressed = False

def get_target_datetimes():
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
    MB_TOPMOST = 0x00040000  # Force la fenêtre au-dessus de tout
    MB_OK = 0x0
    ctypes.windll.user32.MessageBoxW(0, message, "Temps restant", MB_OK | MB_TOPMOST)

def on_press(key):
    global shift_pressed
    if key in [keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r]:
        shift_pressed = True
    elif key == keyboard.Key.f1 and shift_pressed:
        now = datetime.now()
        targets = get_target_datetimes()
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

