from cx_Freeze import setup, Executable
import os

# List of files your game uses (if any, like images or sounds)
# Here, you can add the extra files your game needs
# For example, if your game uses the 'images' and 'sounds' folders, do this:
# include_files = ['images/', 'sounds/']
# options = {
#       'build_exe': {
#           'include_files': include_files,
#       }
#   },

score_file = os.path.join(os.path.dirname(__file__), "scores.txt")

# Basic setup
setup(
    name = "Snake",
    version = "1.0",
    description = "Snake game created by Inês Saragoça",
    executables = [Executable("game.py", base="Win32GUI")], # Use base="Win32GUI" if it's a graphical application
    options={
        'build_exe': {
            'include_files': [score_file] # Include the scores.txt file
        }  
    }
)

# python setup.py build

