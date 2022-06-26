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
# sys.path[0] = PROJECT_ROOT

import DataStructures
from DataStructures.Event import Event

e1 = Event("e1", "1:00", "1", "test", "home", "none")
print(e1.getLabel())

