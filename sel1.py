from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
driver.get("https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fapp%3Ddesktop%26action_handle_signin%3Dtrue%26hl%3Den%26next%3D%252F%26feature%3Dsign_in_button&passive=true&hl=en&service=youtube&uilel=3#identifier")

username = driver.find_element_by_id("Email")
#password = selenium.find_element_by_id("password")

username.send_keys("imd244@nyu.edu")
#password.send_keys("Pa55worD")

driver.find_element_by_id("next").click()

try:
    element = WebDriverWait(driver, 3).until(
        EC.title_is(("NYU Login"))
    )
finally:
 
	username = driver.find_element_by_id("netid")
	password = driver.find_element_by_id("password")

	username.send_keys("imd244")
	password.send_keys("Glitterdevilbaby90")

	driver.find_element_by_name("_eventId_proceed").click()


try:
	element = WebDriverWait(driver, 3).until(
		EC.title_is("Youtube")
	)
finally:
	driver.get("http://youtube.com/feed/history")