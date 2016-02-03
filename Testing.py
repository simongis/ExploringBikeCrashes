import csv
import urllib2
import pandas as pd

# This approach with urllib2 works fine
url = 'http://vicroadsopendata.vicroadsmaps.opendata.arcgis.com/datasets/c2a69622ebad42e7baaa8167daa72127_0.csv?where=BICYCLIST%20%3E%3D%201&inSR=102100&geometry=%7B%22xmin%22%3A13844444.803560872%2C%22ymin%22%3A-4749031.404608972%2C%22xmax%22%3A18499154.078013726%2C%22ymax%22%3A-4015235.9330714755%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D'
response = urllib2.urlopen(url)
cr = csv.reader(response)

#for row in cr:
#    print row
    
# But with pandas, I get nothing returned console hangs?
bc = pd.read_csv(response)


    
# Lets get it into Pandas for easier analysis
#df = pd.read_csv(cr)
#print(df)