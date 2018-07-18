import pandas as pd
import numpy as nu

from ggplot import *
from pandas import Timestamp

firstDs = pd.read_csv("/data/raw/mittlerezahleistage.csv")
secondDs = pd.read_csv("/data/raw/mittlerezahlheissetage.csv")

ds1 = pd.DataFrame(firstDs)
ds2 = pd.DataFrame(secondDs)

out = ds1.append(ds2,sort=False)

out.to_csv("/processed/ice_hot.csv")

mergedDs = pd.read_csv("/processed/ice_hot.csv")

mergedDF = pd.DataFrame(mergedDs)

g = ggplot(mergedDF, aes('eistg_flvb','perimeter')) + \
  geom_point(colour='steelblue')


g.save("/reports/figures/figure.png")

print(g)

