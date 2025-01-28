from cx_Freeze import setup, Executable

# Lista de arquivos que seu jogo usa (se houver, como imagens ou sons)
# Aqui, você pode adicionar os arquivos extras que seu jogo precisar
# Por exemplo, se o seu jogo usa a pasta 'imagens' e 'sons', faça:
# include_files = ['imagens/', 'sons/']
#options = {
#       'build_exe': {
#           'include_files': include_files,
#       }
#   },

# Configuração básica
setup(
    name = "Snake",
    version = "1.0",
    description = "Jogo na snake criado por Inês Saragoça",
    executables = [Executable("jogo.py", base="Win32GUI")]  # Use base="Win32GUI" se for uma aplicação gráfica
)
