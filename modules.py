################################# MODULES ########################################
# modules can be consider a small code libery that are based on related fetures
# modules are used to break large programs into small manageable and organized files
# modules are imported from other modules using the import command
# syntax: import module1[, module2[, ... moduleN]
from math import pi
import sys
import random as r
import kansas
from enum import Enum
from RPS import rock_papper_scissors


print(pi)

# for item in dir(r)1:
#     print(item)
print(kansas.capital)
kansas.randomfact()

print(__name__)
print(kansas.__name__)

rock_papper_scissors()
