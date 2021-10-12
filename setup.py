import cx_Freeze

executables = [cx_Freeze.Executable("main.py", base="Win32GUI")]

cx_Freeze.setup(
    name="XD",
    options={"build_exe": {"packages": ["pygame", "numpy"],
                          "include_files": ["camera.py", "engine.py", "generate_map.py", "hud.py", "mapgen.py", "mouse.py", "tiles.py", "Assets/"]}},
    description="XD",

    executables = executables
    )