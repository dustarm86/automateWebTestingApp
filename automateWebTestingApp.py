import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


# Test Suite Variables to Run
test1 = "fakeIntent1"
test2 = "fakeIntent2"
test3 = ""
test4 = ""
test5 = ""

start_time=time.time()
print("\nScript Started! Opening web browser now...")

# Headless Browser option
#options = Options()
#options.add_argument('-headless')
s = Service('/Users/fakeUN/python/geckodriver')
browser = webdriver.Firefox(service=s)
# opens fakeWebApp login URL
browser.get('http://fakeWebAppURL.com/login')
assert 'fakeWebApp' in browser.title
browser.maximize_window()
time.sleep(1)

usernameButton = browser.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/form/div[2]/div[1]/input")
usernameButton.click()
usernameButton.send_keys("dev@fakeEmail.com")
passwordButton = browser.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/form/div[2]/div[2]/input")
passwordButton.click()
passwordButton.send_keys("fakePassword1234", Keys.ENTER)
time.sleep(1.5)

# opens NLP testing parameters URL
browser.get('http://fakeWebAppUrlTestSelectionPage.com')
assert 'fakeWebApp' in browser.title
time.sleep(1.5)

# selects fakeAgent from the agent dropdown within fakeWebApp
agentButton = browser.find_element(By.XPATH, "/html/body/app-root/app-api-test/app-api-vrex-agent/div/div/mat-accordion/mat-expansion-panel/div/div/div/form/div[1]/div[1]/select/option[6]").click()

# selects HOST  from the host dropdown within fakeWebApp
hostButton = browser.find_element(By.XPATH, "/html/body/app-root/app-api-test/app-api-vrex-agent/div/div/mat-accordion/mat-expansion-panel/div/div/div/form/div[1]/div[2]/select/option[41]").click()

# selects Test Suite and then sends keyboard commands for tests to run from the Test Suite dropdown within fakeWebApp
testSuiteButton = browser.find_element(By.XPATH, "/html/body/app-root/app-api-test/app-api-vrex-agent/div/div/mat-accordion/mat-expansion-panel/div/div/div/form/div[4]/div/ng-select/div/div/div[3]/input")
testSuiteButton.click()
testSuiteButton.send_keys(Keys.BACKSPACE)

# modify the parameter after send.keys to choose the test suite(s) to run
# the test suite variables you choose above are passed here, add/remove tests following the format below as needed
testSuiteButton.send_keys((test1, Keys.ENTER), (test2, Keys.ENTER))

print("\nTesting parameters within fakeWebApp selected and Test started.")

testButton = browser.find_element(By.XPATH, "/html/body/app-root/app-api-test/app-api-vrex-agent/div/div/mat-accordion/mat-expansion-panel/div/div/div/form/app-test-runner/div/div/button").click()

time.sleep(10)
browser.quit()

print("\nTest complete. The program took ", (time.time() - start_time) / 60, " minutes to run.")