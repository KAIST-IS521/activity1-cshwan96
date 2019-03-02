import sys
from csvparser import CsvParser

if __name__ == "__main__":
	"""
	if len(sys.argv) < 3:
		exit(1)

	filename = sys.argv[1]
	printCol = int(sys.argv[2])
	"""
	filename = "./testcase/test1.txt"
	parser = CsvParser()
	with open(filename, "rb") as f:
		plainCsvData = f.read()

	parsedCsv = parser.parse(plainCsvData)

	print parsedCsv
	"""
	for row in parsedCsv:
		print parsedCsv[printCol]
	"""
