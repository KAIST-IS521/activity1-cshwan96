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
		
		lib_parsed_csv = [x for x in lib_csv_reader]
		my_parsed_csv = parser.parse(plain)
		f.close()
		test_result = True
		for rowi in range(len(lib_parsed_csv)):
			row = lib_parsed_csv[rowi]
			for coli in range(len(row)):
				if my_parsed_csv[rowi][coli] != row[coli]:
					test_result = False
					break
		print "%s : %s" % (filename, test_result)

def runErrorCase():
	import subprocess

	testfiles = os.listdir("./errorcase/")
	print "Testing errorcases : Total %d" % len(testfiles)
	for filename in testfiles:
		return_code = subprocess.call(["python", "./main.py", "./errorcase/" + filename, "1"])
		if return_code == 1:
			print "%s : Pass" % (filename)
		else:
			print "%s : Failed" % (filename)

if __name__ == "__main__":
	runTestCase()
	print "----------------------------"
	runErrorCase()