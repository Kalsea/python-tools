import numpy as np
from math import log

def entropy(probs, base):

    entropy = 0

    for i in probs:
        entropy -= i * log(i, base)

    return entropy 


def MI(stock_1, stock_2):

    #how many days
    if len(stock_1) != len(stock_2):
        print('Different size of array in MI')
        exit()

    if len(stock_1) == 0:
        print('0 size of array in stock')
        exit()

    size = len(stock_1)
    base = 2

    nx, count1 = np.unique(stock_1, return_counts = True)
    nx = np.append(nx, nx[-1])

    ny, count2 = np.unique(stock_2, return_counts = True)
    ny = np.append(ny, ny[-1])

    prob1 = count1 / size
    prob2 = count2 / size

    feature = np.vstack((stock_1, stock_2))
    feature = np.transpose(feature)

    jointProbs = np.histogramdd(feature, bins = (nx,ny))[0]

    rows, cols = np.nonzero(jointProbs)
 
    prob3 = jointProbs[rows, cols] / size

    #I(X,Y) = H(X) + H(Y) - H(X,Y)
    mutual_info = entropy(prob1, base) + entropy(prob2, base) - entropy(prob3, base)

    return mutual_info
