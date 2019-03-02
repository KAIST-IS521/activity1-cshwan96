import sys
from csvparser import CsvParser

if __name__ == "__main__":
	if len(sys.argv) < 3:
		exit(1)

	filename = sys.argv[1]
	print_col = int(sys.argv[2])
	if print_col < 1:
		sys.exit(1)

	parser = CsvParser()
	with open(filename, "rb") as f:
		plain_csv_data = f.read()

	try:
		parsed_csv = parser.parse(plain_csv_data)
	except Exception as e:
		sys.exit(1)

	for row in parsed_csv:
		# check for column count of all rows
		if len(row) < print_col:
			sys.exit(1)

	for row in parsed_csv:
		print row[print_col - 1]

	sys.exit(0)