import os

# Utility functions for managing game scores
def get_score_file(game_folder):
    return os.path.join(game_folder, "scores.txt")

# Reads and returns the highest score from the score file
def max_score(score_file):
    if not os.path.exists(score_file):
        with open(score_file, "w") as f:
            f.write("0")
        return 0

    with open(score_file, "r") as f:
        return int(f.readline().strip() or 0)

# Updates the score file with the highest score between the current score and the previous high score
def update_score(score_file, new_score):
    high_score = max_score(score_file)

    with open(score_file, "w") as f:
        f.write(str(max(high_score, new_score)))

# Resets the score in the score file to 0
def reset_score(score_file):
    with open(score_file, "w") as f:
        f.write("0")