from tkinter import Y
from Trip import Time


def main():
    t = Time(11, 20, 12, 30)
    print(t.getDate())
    t.date = t.date + 1
    print(t.getDate())

if __name__ == "__main__":
    main()
