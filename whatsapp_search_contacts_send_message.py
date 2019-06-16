from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime

currentTime = datetime.datetime.now()
if currentTime.hour < 12:
	greeting_msg = 'Good morning, '
	print('Good morning, ')
elif 12 <= currentTime.hour < 18:
	greeting_msg = 'Good afternoon, '
	print('Good afternoon, ')
else:
	greeting_msg = 'Good evening, '
	print('Good evening, ')
# Replace below path with the absolute path
# to chromedriver in your computer
''' Chrome_version of 75.0.3770.90 
https://chromedriver.storage.googleapis.com/index.html?path=75.0.3770.90/	
'''

driverPath = 'C:Users/khushal/Documents/Python Scripts/chromedriver'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=options)  # , executable_path=driverPath)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

def get_contact_list_from_chat_window():
	time.sleep(5)
	contacts_list = []
	for person in driver.find_elements_by_class_name('_3NWy8'):
		contacts_list.append(person.text)
	print(contacts_list)
	return contacts_list

person_contact_list = get_contact_list_from_chat_window()

friends_lists = ['Kedar Surve','Hillel Awaskar']
friends_lists = ['Hillel Awaskar']#,'Hillel Awaskar']

string = "Automated Message sent using Python!!!" 	#Replace this string with your own message

group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.ZP8RM")))
search = driver.find_elements_by_class_name('_2zCfw')
#print(search)
for friend in friends_lists:
	search[0].clear()
	search[0].send_keys(friend)
	wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button._1XCAr")))
	time.sleep(3)
	persons = driver.find_elements_by_class_name('_3NWy8')
	#print(len(persons))
	for person in persons:
		print(person.text)
		if person.text not in person_contact_list:
			person.click()
			message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
			message.send_keys(string + greeting_msg + person.text)
			sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
			sendbutton.click()
		else:
			print("*")
			string = "Automated Message sent using Python!!!"  # Replace this string with your own message
			x_arg = '//span[contains(@title,' + person.text + ')]'
			group_title = wait.until(EC.presence_of_element_located((
				By.XPATH, x_arg)))
			group_title.click()
			message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
			message.send_keys(string + greeting_msg + person.text)
			sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
			sendbutton.click()

driver.close()