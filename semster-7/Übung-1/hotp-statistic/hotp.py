import os
import secrets

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.twofactor.hotp import HOTP
from cryptography.hazmat.primitives.hashes import SHA1
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import collections


def count_frequency(arr):
    return collections.Counter(arr)


if __name__ == '__main__':

    hotp_holder = []

    key = os.urandom(20)
    hotp = HOTP(key, 8, SHA1(), backend=default_backend())

    for x in range(100000):
        hotp_value = hotp.generate(x)
        hotp_str = hotp_value.decode("utf-8")
        n = 2
        for i in range(0, len(hotp_str), n):
            hotp_holder.append(hotp_str[i:i+n])

    # matplotlib histogram
    plt.hist(hotp_holder, color='blue', edgecolor='black',
             bins=100)

    # seaborn histogram
    sns.distplot(hotp_holder, hist=True, kde=False,
                 bins=1000, color='blue',
                 hist_kws={'edgecolor': 'black'})
    # Add labels
    plt.title('Histogram of Arrival Delays')
    plt.ylabel('Occurrences')
    plt.xticks([0, 25, 50, 75, 100])
    plt.show()

    #freq = count_frequency(hotp_holder)
    #for key, value in freq.items():
    #    print(key, " -> ", value)

    hopt_holder_2 = []
    for i in range(100000):
        for x in range(4):
            hotp_value = str(secrets.randbelow(9)) + str(secrets.randbelow(9))
            hopt_holder_2.append(hotp_value)

    plt.hist(hopt_holder_2, 100,
             density=True,
             histtype='bar',
             facecolor='b',
             alpha=0.5)

    plt.xticks([0, 25, 50, 75, 100])
    plt.show()
