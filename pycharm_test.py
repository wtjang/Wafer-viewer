print(3+5)

import pandas as pd

test = pd.DataFrame(index=range(0,101), columns=range(0,101))

for i in range(0,101):
    for j in range(0,101):
        if ((50-i)**2 + (50-j)**2) < 50**2:
            test.loc[i,j] = i*2+i+j
        else:
            test.loc[i,j] = 0