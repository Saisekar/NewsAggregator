# Import pandas
import pandas as pd
# Create data
data = {'score': [1,1,1,2,2,2,3,3,3]}

# Create dataframe
df = pd.DataFrame(data)

# View Rolling Average
print (df.rolling(window=3).mean())