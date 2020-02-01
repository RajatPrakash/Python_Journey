# reading data from internet using pandas
import pandas as pd
import lxml
data = pd.read_html('https://www.livingin-canada.com/house-prices-canada.html')
print(data[1])