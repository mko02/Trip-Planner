from src.DataStructures import Cost

def main():
    ## Evenly split cost:
    EC = Cost(True, ("A", 2000), {"A" : 1000, "B" : 1000})
    print(EC)


if __name__ == "__main__":
    main()
