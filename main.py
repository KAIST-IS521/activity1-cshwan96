import sys
from csvparser import CsvParser

if __name__ == "__main__":
	if len(sys.argv) < 3:
		exit(1)

	filename = sys.argv[1]
	print_col = int(sys.argv[2])

	parser = CsvParser()
	with open(filename, "rb") as f:
		plain_csv_data = f.read()
	
	parsed_csv = parser.parse(plain_csv_data)

	for row in parsed_csv:
		print row[print_col - 1]
