# Activity1. CSV Parser

Csv parser written in python2 based on [RFC4180](https://tools.ietf.org/html/rfc4180).

## Usage
```
python main.py ./testcase/test1.csv 1
```

## Test

To run a test, run following command.
```
python test.py
```

Files in "./testcase" directory is compared with default csv library in the python.

And files in "./errorcase" is tested if it returns 1 for exit code.
#### Test Output Example
	Testing testcases : Total 5
	rfcSample.csv : True
	test1.csv : True
	test2.csv : True
	test3.csv : True
	test4.csv : True
	----------------------------
	Testing errorcases : Total 4
	error1.csv : Pass
	error2.csv : Pass
	error3.csv : Pass
	error4.csv : Pass
	error5.csv : Pass

Downloaded test4.csv Sample from [Link](https://support.spatialkey.com/spatialkey-sample-csv-data/)