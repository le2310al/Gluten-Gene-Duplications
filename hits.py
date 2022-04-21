import glob
import pandas as pd


excel = []
for workbook in glob.glob("*.xlsx"):
	excel.append(workbook)
#print(excel)
#Use line 8 to verify that the files you wish to scan can be found by hits.py


genome =  ['1A', '1B', '1D', '2A', '2B', '2D', '3A', '3B', '3D', '4A', '4B', '4D', '5A', '5B', '5D', '6A', '6B', '6D', '7A', '7B', '7D', 'Un']
results = []

print('Gene/Chromosome, ' + ', '.join(genome))

for xlsx in excel:
	file = pd.read_excel(xlsx)
	with open('temp.txt', 'w') as text:
		file.to_string(text, index=False)

	text_2 = r"C:\FilePath\temp.txt"

	pi_string = ''
	with open(text_2) as block:
		for line in block:
			line_2 = line.lstrip()
			pi_string += line_2[:2]
	#print(xlsx.strip('.xlsx'))
	#Use line 29 to print the associated gene name over every hit count output
	results.append(f"{xlsx.strip('.xlsx')}")
	for chromosome in genome:		
		counter = pi_string.count(chromosome)
		#print(f"{chromosome}, {counter}")
		#Use line 31 to print the accociated gene location with every hit count output
		results.append(f"{counter}")
	print(f"{','.join(results)}")
	results.clear()
