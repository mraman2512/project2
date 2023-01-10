## 1 st part LOGIN part.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

username = "aman"
password = "Aman@1234"


driver = webdriver.Chrome("chromedriver")

# driver.maximize_window()

driver.get("http://workmanager.simplify3x.com/en/login")
# find username/email field and send the username itself to the input field
driver.find_element("name", "_username").send_keys(username)
# find password input field and insert password as well
driver.find_element("name", "_password").send_keys(password)
# click login button
driver.find_element(By.CLASS_NAME, "btn-block").click()


### second part after login .
driver.find_element(By.CLASS_NAME, "messages-menu-empty").click()
import time
time.sleep(3)

## for selecting one value from customer dropdown
x = driver.find_element(By.ID, 'timesheet_edit_form_customer')
drop = Select(x)
drop.select_by_index(4)
time.sleep(2)
## selecting value from project section.
y = driver.find_element(By.ID, 'timesheet_edit_form_project')
drop = Select(y)
drop.select_by_index(1)
time.sleep(2)
driver.find_element(By.ID, "timesheet_edit_form_description").send_keys("Working on devops ark backend services")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "modal-form-save").click()
time.sleep(3)

from flask import Flask
import platform
app = Flask(__name__)


@app.route('/')
def hello_name():
    return f'Hello Aman K welcome from hostname : {platform.node()}!'


if __name__ == '__main__':
    app.run(host="localhost", port=8080)
