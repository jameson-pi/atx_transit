import csv
def getinfofromfile(filename):
	filelist=[]
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count != 0:
				filelist.append(row)
			line_count += 1
	return filelist
print(getinfofromfile("routes.csv"))