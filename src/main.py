from grid import Grid
from game_of_life import GameOfLife
import sys

def main():
    app = GameOfLife(100, 70, 60, False)
    app.loop()

    sys.exit()

if __name__ == "__main__":
    main()