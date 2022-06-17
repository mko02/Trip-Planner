from src.DataStructures.Cost import Cost


def main():
    # Evenly split cost:
    ec = Cost(True, ("A", 2500), {"A": 1000, "B": 1000, "C": 500})
    relation = ec.calculate_cost()
    
if __name__ == "__main__":
    main()
