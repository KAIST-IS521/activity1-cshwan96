from csvparser import CsvParser
import csv
import os

def runTestCase():
	testfiles = os.listdir("./testcase/")
	print "Testing testcases : Total %d" % len(testfiles)
	for filename in testfiles:
		f = open("./testcase/" + filename, "rb")
		plain = f.read()
		f.seek(0)
		lib_csv_reader = csv.reader(f)
		
		parser = CsvParser()
		my_parsed_csv = parser.parse(plain)
		lib_parsed_csv = [x for x in lib_csv_reader]
		f.close()

		test_result = True
		for rowi in range(len(lib_parsed_csv)):
			row = lib_parsed_csv[rowi]
			for coli in range(len(row)):
				if my_parsed_csv[rowi][coli] != row[coli]:
					test_result = False
					break
		print "%s : %s" % (filename, test_result)

if __name__ == "__main__":
	runTestCase()