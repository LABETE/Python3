def main():
    for i in range(3):
        newGame = input("test")
        if newGame in ["yes", "y"]:
            yield "yes"
        elif newGame in ["no", "n"]:
            yield "no"