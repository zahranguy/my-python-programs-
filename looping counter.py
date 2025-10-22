import time

a = "*"
b = 2
while b == 2: 
    print(a) 
    a = a + "*" 
#    time.sleep(0.1)
    if len(a) > 10:
        b = 3

# should output
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
