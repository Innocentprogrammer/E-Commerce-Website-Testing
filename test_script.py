from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

url = "https://demowebshop.tricentis.com/"
driver.get(url)
sleep(1)
driver.maximize_window()

# ## Test Script for Register Page

# sleep(2)
# driver.find_element('class name','ico-register').click()
# sleep(1)
# driver.find_element('id','gender-male').click()
# sleep(1)
# driver.find_element('id','FirstName').send_keys('Mratyunjay')
# sleep(1)
# driver.find_element('id','LastName').send_keys('Saxena')
# sleep(1)
# driver.find_element('id','Email').send_keys('msaxena8@gmail.com')
# sleep(1)
# driver.find_element('id','Password').send_keys('Mjs7579@')
# sleep(1)
# driver.find_element('id','ConfirmPassword').send_keys('Mjs7579@')
# sleep(1)
# driver.find_element('id','register-button').click()
# sleep(1)
# driver.find_element('class name','button-1.register-continue-button').click()

# ## Test Script for Login Page

sleep(2)
driver.find_element('class name','ico-login').click()
sleep(1)
driver.find_element('id','Email').send_keys("msaxena8@gmail.com")
sleep(1)
driver.find_element('id','Password').send_keys("Mjs7579@")
sleep(1)
driver.find_element('id','RememberMe').click()
sleep(1)
driver.find_element('class name','button-1.login-button').click()

# ## Test Script for Search Functionality

sleep(3)
driver.find_element('id','small-searchterms').send_keys('Laptop')
sleep(1)
driver.find_element('class name','button-1.search-box-button').click()

### Test Script for Cart Functionality

sleep(2)
driver.find_element('class name','button-2.product-box-add-to-cart-button').click()
sleep(1)
driver.find_element('xpath','//a[@href="/cart"]').click()
sleep(1)
driver.find_element('name','removefromcart').click()
sleep(1)
driver.find_element('class name','button-2.update-cart-button').click()
sleep(1)
driver.find_element('xpath','//img[@src="/Themes/DefaultClean/Content/images/logo.png"]').click()

sleep(4)
driver.close()