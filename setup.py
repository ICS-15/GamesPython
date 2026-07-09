from cx_Freeze import setup, Executable
import os

snake_score = os.path.join("snake", "scores.txt")
brick_score = os.path.join("brickBreaker", "scores.txt")

build_options = {
    "include_files": [
        snake_score,
        brick_score,
        "snake",
        "brickBreaker",
        "utils",
    ]
}

setup(
    name="Python Games",
    version="1.0",
    description="Snake and Brick Breaker by Inês Saragoça",
    options={"build_exe": build_options},
    executables=[
        Executable(
            "main.py",
            base="Win32GUI"
        )
    ],
)

# python setup.py build

