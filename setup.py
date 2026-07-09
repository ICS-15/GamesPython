from cx_Freeze import setup, Executable
import os

snake_score = os.path.join("snake", "scores.txt")
brick_score = os.path.join("brickBreaker", "scores.txt")

# Define build options for cx_Freeze
build_options = {
    "include_files": [
        snake_score,
        brick_score,
        "snake",
        "brickBreaker",
        "utils",
    ]
}

# Setup configuration for cx_Freeze
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
# In case you want to build the executable, run the following command in the terminal:
# python setup.py build

