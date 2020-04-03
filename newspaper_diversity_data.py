import os
from selenium import webdriver
import time

os.chdir(r'/Users/sundaswiqas/Downloads')

files = [file for file in os.listdir() if 'news' in file or 'NP' in file]
for f in ['2013Minority percentages at participating ONLINE organizations copy(1).pdf', '2015 Summary Report for each NP(1).pdf']:
	files.append(f)
del files[0]
del files[-1]
print('There are ' + str(len(files)) + ' files:')
print(files)


driver = webdriver.Chrome('/Users/sundaswiqas/Desktop/chromedriver')

def get_pdf_data(file):
	try:
		driver.get('http://127.0.0.1:8080')
		time.sleep(10)
		
		file = os.path.abspath(file)
		upload_box = driver.find_element_by_id('file') # need to use send_keys with input tag when actual box is hidden
		upload_box.send_keys(file)
		
		time.sleep(15)

		import_button = driver.find_element_by_css_selector('#upload > button')
		import_button.click()

		time.sleep(15)

		autodetect_tables = driver.find_element_by_id('restore-detected-tables')
		autodetect_tables.click()

		time.sleep(15)
		
		preview_button = driver.find_element_by_id('all-data')
		preview_button.click()

		time.sleep(15)

		export_button = driver.find_element_by_id('download-data')
		export_button.click()
	except Exception as e :
		print("Could not gather data for " + file)
		print(str(e))

for file in files:
	get_pdf_data(file)

driver.quit()
