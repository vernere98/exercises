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
		print('| Birthdate  |       Name       |')
		print('---' * 11)
		for entry in self.entries:
			date, name = entry.values()
			print('|',date, '|', name)
		print('\n')
		# self.read_input()

	def search_entries(self, query=''):
		search = input('Input the name you want to search: ')
		matched_entries = [entry for entry in self.entries if search in entry['name']]
		print(matched_entries, '\n')
		return matched_entries

	def edit_entry(self):
	    i = int (input("Input the index you want to edit: "))
	    print(self.entries[i],'\n')
	    choice = input("Enter (n) for the name and (d) for date: ")
	    if choice == 'n' or 'N':
	        new_name = input("New Name: ")
	        self.entries[i]['name'] = new_name
	    elif choice == 'd':
	        new_bdate = input("New Birthdate: ")
	        self.entries[i]["date"] = new_bdate
	    else:
	        print("Invalid input!")

	    print('JOURNAL UPDATED!')
	    self.view_entries()

	def delete_entries(self):
		i = int(input('Input the index you want to delete: '))
		self.entries.pop(i)

		print('\n')
		print('UPDATED JOURNAL:')
		self.view_entries()
		return self.entries
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
journal.search_entries(query='')
journal.delete_entries()
journal.edit_entry()
journal.export_entries()