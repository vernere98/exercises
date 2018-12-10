import json

class Journal:
	# xRead from an input file
    # xAdd entry to journal
    # xView entries
    # Search entries
    # Edit entries
    # Delete entries
    # Export entries
    

	def __init__(self):
		self.journal_id = 1
		self.entries = []

	def read_input(self):
		data = []
		with open('birthdays.json') as json_data:
			data = json.load(json_data)

			for r in data['birthdays']:
				date = r['date']
				name = r['name']
				#print(r['date'], '|', r['name'])
				self.add_entry(date, name)

	def add_entry(self, date, name):
		self.entries.append({
			'date': date,
			'name': name
			})


	def view_entries(self):
		print('---' * 11)
		print('|  Date    |        Name        |')
		print('---' * 11)
		for entry in self.entries:
			date, name = entry.values()
			print(date, '|', name)
		# self.read_input()

	def delete_entries(self):
		with open('birthdays.json') as json_data:
			data = json.loads(json_data.read())

		for entry in data['birthdays']:
			del entry['name']
				# if 'date' in entry:
				# 	del entry['name']
		# json_data.write(data)


	def export_entries(self):
		with open('birthdays.txt', 'w') as json_data:
			json_data.writelines([
				'{date}|{name}\n'.format_map(entry)
				for entry in self.entries
				])
			# data = json.dump(data, json_data)


	
	def __str__(self):
	    return 'Journal' + str(self.journal_id)



journal = Journal()
journal.read_input()
print(journal)
journal.view_entries()
journal.delete_entries()
journal.export_entries()