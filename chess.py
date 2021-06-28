""" Script to scrape top 100 FIDE rating lists from ratings.fide.com """

import random
import math
import time
from get_html import get_html

base_string = 'https://ratings.fide.com/toparc.phtml?cod='

"""
We use steps of 4 because the lists alternate
between Open, Women, Juniors and Junior Women.
Change the start to 2, 3 or 4 to get one of these lists instead.
Change the end from 626 if you are not getting the latest rating lists.
"""
for i in range(1,626,4):
    #Random sleep to avoid overloading servers and simulate human behavior
    time.sleep(random.randint(0,1) + random.random())
    filename = str(math.ceil(i/4)) + '.html'
    get_html(base_string+str(i), basepath='pages/', filename = filename)
    #Random sleep to avoid overloading servers and simulate human behavior
    if random.randint(1,12) == 5:
        time.sleep(random.randint(5,15) + random.random())
