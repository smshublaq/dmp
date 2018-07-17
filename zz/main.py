import pandas as pd
import numpy as nu

firstDs = pd.read_csv("mittlerezahleistage.csv")
secondDs = pd.read_csv("mittlerezahlheissetage.csv")

'''
baseball = pandas.read_csv(filename)

# YOUR CODE GOES HERE
baseball['weight'] = baseball['weight'].fillna(numpy.mean(baseball["weight"]))
return baseball
'''
ds1 = pd.DataFrame(firstDs)
ds2 = pd.DataFrame(secondDs)

out = ds1.append(ds2,sort=False)

out.fillna(nu.mean())






