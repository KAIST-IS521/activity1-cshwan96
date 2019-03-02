state_undefined = 0
state_record = 1
state_field = 2
state_escaped = 3
state_non_escaped = 4

def isTextdata(ch):
	numCh = ord(ch)
	return ((0x2D <= numCh) and (numCh <= 0x7E)) or ((0x23 <= numCh) and (numCh <= 0x2B)) or numCh == 0x20 or numCh == 0x21

class CsvParser():
	def __init__(self):
		self._state = state_record
		self._line = 0
		self._column = 0
		self._row = 0
		self._cursor = 0

	def parse(self, instr, header = False):
		parsedCsv = list()
		instrlen = len(instr)

		while self._cursor < instrlen:
			curCh = instr[self._cursor]
			self._cursor += 1

			if self._state == state_record:
				parsedCsv.append(list())
				if isTextdata(curCh):
					self._state = state_non_escaped
					curCell = curCh

				if curCh == ',':
					raise Exception("field starts with , without escape")

			elif self._state == state_field:
				if isTextdata(curCh):
					self._state = state_non_escaped
					curCell = curCh

				if curCh == ',':
					raise Exception("field starts with , without escape")
				pass

			elif self._state == state_escaped:
				pass

			elif self._state == state_non_escaped:
				if curCh == ",":
					self._state = state_field
					self._column += 1
					parsedCsv[self._row].append(curCell)

				elif isTextdata(curCh):
					curCell += curCh

				elif curCh == "\r" and self._cursor < instrlen and instr[self._cursor] == "\n":
					self._cursor += 1 # skip \n
					self._state = state_record
					parsedCsv[self._row].append(curCell)
					self._row += 1
					self._column = 0

				else:
					print ord(curCh)
					raise Exception("non-textdata in non_escaped state")

		return parsedCsv

		if self._state == state_escaped:
			pass
			#raise Exception("no closing quote at the end")

		else:
			return parsedCsv

