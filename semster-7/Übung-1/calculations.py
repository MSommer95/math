import secrets
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from collections import Counter

digit_holder = []
hotp_holder = []

for i in range(1000000):
    hotp_value = ''
    for x in range(8):
        hotp_value += str(secrets.randbelow(9))
    hotp_holder.append(hotp_value)


for x in range(len(hotp_holder)):
    for i in range(0, 8, 2):
        current_value = hotp_holder[x][i] + hotp_holder[x][i+1]
        digit_holder.append(current_value)


plt.hist(digit_holder, 100,
         density=True,
         histtype='bar',
         facecolor='b',
         alpha=0.5)

plt.show()