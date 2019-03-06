state_record = 1
state_field = 2
state_escaped = 3
state_non_escaped = 4

def isTextdata(ch):
	numCh = ord(ch)
	return ((0x2D <= numCh) and (numCh <= 0x7E)) or ((0x23 <= numCh) and (numCh <= 0x2B)) or numCh == 0x20 or numCh == 0x21

def isEscapedText(ch):
	# without \" because 2DQUOTE is handled later
	return isTextdata(ch) or ch in [",", "\r", "\n"]

class CsvParser():
	def __init__(self):
		self._state = state_record

	def parse(self, instr, header = False):
		parsed_csv = list()
		instrlen = len(instr)
		_cursor = 0
		while _cursor < instrlen:
			cur_ch = instr[_cursor]
			_cursor += 1

			if self._state == state_record:
				# only state_record state append new rows to parsed_csv
				parsed_csv.append(list())
				if isTextdata(cur_ch):
					self._state = state_non_escaped
					cur_cell = cur_ch
				elif cur_ch == "\"":
					self._state = state_escaped
					cur_cell = ""
				if cur_ch == ',':
					self._state = state_field
					parsed_csv[-1].append("")

			elif self._state == state_field:
				# same as state_record except not append rows
				if isTextdata(cur_ch):
					self._state = state_non_escaped
					cur_cell = cur_ch
				elif cur_ch == "\"":
					self._state = state_escaped
					cur_cell = ""
				if cur_ch == ',':
					parsed_csv[-1].append("")

			elif self._state == state_escaped:
				# state for escaped : DQUOTE *(TEXTDATA / COMMA / CR / LF / 2DQUOTE) DQUOTE 
				if isEscapedText(cur_ch):
					cur_cell += cur_ch
				elif cur_ch == "\"":
					# check for 2DQUOTE
					if _cursor < instrlen and instr[_cursor] == "\"":
						_cursor += 1 # skip \"
						cur_cell += "\""
						continue
					# escape condition for state_escaped
					elif _cursor < instrlen:
						nextCh = instr[_cursor]
						_cursor += 1 # skip nextCh
						if nextCh == ",":
							self._state = state_field
							parsed_csv[-1].append(cur_cell)
						elif (nextCh == "\r" and _cursor < instrlen and instr[_cursor] == "\n"):
							_cursor += 1 # skip \n
							self._state = state_record
							parsed_csv[-1].append(cur_cell)
						else:
							continue
				else:
					raise Exception("Not EscapedText in escaped state")

			elif self._state == state_non_escaped:
				if isTextdata(cur_ch):
					cur_cell += cur_ch
				elif cur_ch == ",":
					self._state = state_field
					parsed_csv[-1].append(cur_cell)
				elif cur_ch == "\r" and _cursor < instrlen and instr[_cursor] == "\n":
					_cursor += 1 # skip \n
					self._state = state_record
					parsed_csv[-1].append(cur_cell)
				else:
					raise Exception("Non-textdata in non_escaped state")

		if self._state == state_escaped:
			if cur_ch != "\"":
				raise Exception("End of file before closing quote")
			parsed_csv[-1].append(cur_cell)


		elif self._state == state_non_escaped:
			parsed_csv[-1].append(cur_cell)

		return parsed_csv