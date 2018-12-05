import json

class Journal:
	# xRead from an input file
    # Add entry to journal
    # View entries
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
				print(r['date'], '|', r['name'])

	# def add_entry(self, date, name)


	def view_entries(self):
		print('---' * 11)
		print('Date\t   | Name\t        |')
		print('---' * 11)
		self.read_input()


	def export_entries(self, file_name):
	        with open(file_name, 'w') as f:
	            f.writelines([
	                '{date}|{text}'.format_map(entry)
	                for entry in self.entries
	            ])


	
	def __str__(self):
	    return 'Journal' + str(self.journal_id)



journal = Journal()
journal.read_input()
print(journal)
journal.view_entries()
journal.export_entries(file_name='journal_backup.txt')
