import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from DataStructures.Cost import *
from DataStructures.Member import *


def test_calculate():
    m1 = Member("m1", "red")
    m2 = Member("m2", "blue")
    m3 = Member("m3", "red")
    expected = {m1: 20.0, m2: 30.0}
    c = Cost(m1, 50.0, expected, "c1", "", "")
    assert c.calculate_debt() == {m2: 30.0}
    expected = {m1: 20.0, m2: 30.0, m3: 50.0}
    c = Cost(m2, 100.0, expected, "c2", "", "")
    assert c.calculate_debt() == {m1: 20.0, m3: 50.0}


def result(relation):
    result = ""
    for debtor in relation.keys():
        result = result + debtor.get_name() + " has to pay " + str(relation[debtor]) + '\n'
    return result


def main():
    test_calculate()


if __name__ == "__main__":
    main()