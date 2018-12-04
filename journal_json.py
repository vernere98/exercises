import json


# class Journal:




# 	def __init__(self):
# 	    self.journal_id = 1
# 	    self.entries = []

# 	def read_input(self):
# 	    lines = []
# 	    with open('birthdays.json') as jason_data:
# 	        lines = jason_data.readlines()

# 	    for line in lines:
# 	    	date, text = line.split(',')
# 	    #     self.add_entry(date, text)

# 	    return lines

# 	# def view_entries(self):
# 	# 		print('Date\t   | Text')
# 	# 		print('---' * 8)
# 	#         	for entry in self.entries:
# 	#             	date, text = entry.values()
# 	#             	print(date, '|', end=' ')
# 	#            		print(text)


# 	def __str__(self):
# 	    return 'Journal ' + str(self.journal_id)



# journal = Journal()
# journal.read_input()
# # print (journal)
# journal.view_entries()


with open('birthdays.json') as jason_data:
	data = json.load(jason_data)
	for r in data['birthdays']:
		print(r['date'], r['name'])

		# with open('birthdays.json') as jason_data:
		# 	data = json.load(jason_data)
		# 	for r in data['birthdays']:
		# 	fo = open(r['id'] + "_" + r['name'] + ".txt", "wb") 
		# 	fo.write(r['date'] + "         " + r['name'] + "         ")
		# 	fo.close()

# print(r['date'], r['name'])

# def export_entries(self, file_name):
#         with open(file_name, 'w') as f:
#             f.write([
#                 '{date}|{text}'.format_map(entry)
#                 for entry in self.entries
#             ])
