import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
Data_Root = os.path.abspath(os.path.join(
                os.path.dirname(__file__),
                os.pardir + "/DataStructures")
)
sys.path.append(PROJECT_ROOT)
sys.path.append(Data_Root)
print(sys.path)

from DataStructures.Cost import Cost


def main():
    # Evenly split cost:
    ec = Cost(True, ("A", 2500), {"A": 1000, "B": 1000, "C": 500})
    relation = ec.calculate_cost()
    
if __name__ == "__main__":
    main()
