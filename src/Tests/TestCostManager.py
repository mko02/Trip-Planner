import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from DataStructures.Cost import *
from DataStructures.Member import *
from DataStructures.CostManager import *


def test_add_cost():
    m1 = Member("m1", "red")
    m2 = Member("m2", "red")
    m3 = Member("m3", "red")
    members = (m1, m2, m3)
    cm = CostManager()
    cm.add_member(m1)
    cm.add_member(m2)
    cm.add_member(m3)
    c1 = Cost(m1, 100.0, {m1: 10.0, m2: 90.0}, "c1", "", "")
    cm.add_cost(c1)
    print(cm)
    # assert cm.get_balance() == {m1: {m2: 0, m3: 0}, m2: {m1: 90, m3: 0}, m3: {m1: 0, m2: 0}}
    c2 = Cost(m2, 110.0, {m1: 20.0, m2: 10.0, m3: 80}, "c2", "", "")
    cm.add_cost(c2)
    print(cm)
    # assert cm.get_balance() == {m1: {m2: 0, m3: 0}, m2: {m1: 70, m3: 0}, m3: {m1: 0, m2: 80}}


def main():
    test_add_cost()


if __name__ == "__main__":
    main()