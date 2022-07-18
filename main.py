#!/usr/bin/env python3
from src.audiosources.sinus import Sinus
from src.audiosources.square import Square


def main():
    sin = Sinus(300.0, 44100, 4, 1.0)
    sq = Square(300.0, 44100, 3, 0.1)
    sq.save("test.wav")

if __name__ == "__main__":
    main()
