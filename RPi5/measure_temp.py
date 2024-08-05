# !pip install vcgencmd

from vcgencmd import Vcgencmd

vcgm = Vcgencmd()

temp = vcgm.measure_temp()

print("T = ", temp)




