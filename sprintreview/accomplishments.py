import os
import pandas as pd

class Accomplishments():

	def __init__(self, root_path, conf, date):
		self.root_path = root_path
		self.pack_path = 'sprintreview'
		self.conf = conf
		self.date = date
		self.report_filename = 'Accomplishments {}.txt'.format(self.date)


	def get_sprint_xl(self):

		self.S = pd.read_excel(self.conf['sprints_xl_filepath'], engine='openpyxl')


	def filter_sprint_xl(self):

		self.S = self.S[self.S['Sprint Date'] == self.date]


	def reduce_sprint_xl(self):

		sel = [
			'Category',
			'Subcategory',
			'Task',
			'Status',
			'Act Effort Pct',
			'Impediment',
			]
		self.S = self.S[sel]


	def sort_sprint_xl(self):

		self.S.sort_values(
			by=['Category', 'Act Effort Pct'],
			ascending=[True, False],
			inplace=True
			)


	def format_sprint_xl(self):

		self.S['Act Effort Pct'] = self.S['Act Effort Pct'].round(2)


	def sprint_xl_to_txt(self):

		cat_len = self.S.Category.str.len().max()
		subcat_len = self.S.Subcategory.str.len().max()
		status_len = self.S.Status.str.len().max()

		self.dst_text = 'Sprint End Date: {}\n\n'.format(self.date)
		
		for index, row in self.S.iterrows():
			self.dst_text += \
				'{}\nCategory: {}{}| Subcat: {}{}| Effort Pct: {}\n\n'.format(
				row["Task"],
			    row["Category"],
			    " "*(cat_len-len(row["Category"])+2),
			    row["Subcategory"],
			    " "*(subcat_len-len(row["Subcategory"])+2),
			    row["Act Effort Pct"],
			    )


	def get_txt(self):

		return self.dst_text


	def send_to_reports(self):

		report_filepath = os.path.join(
			self.conf['digest_path'],
			self.report_filename
			)

		with open(report_filepath, 'w') as f:
			f.write(self.dst_text)
