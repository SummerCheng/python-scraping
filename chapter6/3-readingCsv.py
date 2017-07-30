from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
csvReader = csv.DictReader(dataFile)
# csvReader = csv.reader(dataFile)

for row in csvReader:
	# print (row)
	print("The album \""+row['Name']+"\" was released in "+str(row['Year']))