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


class Journal:

	def __init__(self):
		self.journal_id = 0
		self.entries = []
        

	def read_input(self):
		data = []
		with open('birthdays.json') as json_data:
			data = json.load(json_data)

			for r in data:
				date, name = r.split(',')
				self.add_entry(date, name)

			return data
	
	def add_entry(self, date, name):
		self.entries.append({
            'date': date,
            'name': name
        })

	def export_entries(self, file_name):
	    with open(file_name, 'w') as f:
	        f.writelines([
	            '{date} {name}'.format_map(entry)
	            for entry in self.entries
            ])

def __str__(self):
	return 'Journal ' + str(self.journal_id)

	# def write(path,filename,data):
	# 	file_path = './' + path + '/' +filename + '.json'
	# 	with open(file_path, 'w') as f:
	# 		json.dump(data,f)

	# path = './'
	# filename = 'birthday1'

	# data ={}
	# data['test'] = 'test2'
	# data['hello'] = 'sds'

	# write(path,filename,data)

journal = Journal()
journal.read_input()
journal.export_entries(file_name='journal_backup.json')