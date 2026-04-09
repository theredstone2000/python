# ballgame — tiny pygame clicker

A tiny Pygame demo. A ball bounces around a white window titled "ballgame". Click the ball to change its color and gain a point.

Files in this folder:
- `ball_game.py` — the game source
- `requirements.txt` — dependencies (pygame, pyinstaller)
- `build_exe.ps1` — PowerShell helper to install requirements and build a single-file `.exe`

Build and run (Windows, PowerShell)

Open PowerShell and cd to this folder:

```powershell
cd "C:\Users\adrie_3dascbn\OneDrive\Bureau\pythonggbggtfiles"
```

Install dependencies and run the game with Python 3.13 (if `python` points to 3.13):

```powershell
python -m pip install --user -r requirements.txt
python ./ball_game.py
```

Build a single-file exe (double-click to launch):

```powershell
# installs pyinstaller into user site and creates dist\ball_game.exe
./build_exe.ps1
```

If `python` is not the 3.13 interpreter you want, pass the executable name to the build script, for example:

```powershell
./build_exe.ps1 -PythonCmd "C:\\Path\\To\\Python313\\python.exe"
```

Notes
- The build script installs packages into the user site (`--user`). If you prefer a virtualenv, create and activate it prior to running the script.
- Single-file builds may be larger; antivirus heuristics sometimes flag new EXEs — if that happens, build locally or use a folder distribution (`--onedir`) instead.
