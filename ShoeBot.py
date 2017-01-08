from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def delay1():
    time.sleep(0.5)

def BuyShoes(driver):
    ShoeSize = 10.5 ## MUST BE IN HALF SIZE INCREMENTS FROM 8 TO 14!!!!!!
    Name = "Andrew"
    LastName = "Kantola"
    StreetAddress = "Street"
    CityName = "City"
    ZipCode = "60913"
    PhoneNumber = "3920167493"
    Email = "email@email.com"
    ItemWebListingAddress = "http://www.adidas.com/us/alphabounce-xeno-shoes/B39074.html"
    
    #driver = webdriver.Chrome()
    driver.get(ItemWebListingAddress)
    sizeDropdown = driver.find_element_by_xpath("""//*[@id="buy-block"]/div[1]/div[5]/div[2]/form/div[2]/div[2]/div/div/a""").click()
    delay1()
    size = driver.find_element_by_xpath("""//*[@id="buy-block"]/div[1]/div[5]/div[2]/form/div[2]/div[2]/div/div/div/div[2]/div/ul/li[{0}]/span""".format(str(((ShoeSize-8)*2)+2))).click()
    delay1()
    addToCart = driver.find_element_by_xpath("""//*[@id="buy-block"]/div[1]/div[5]/div[2]/form/div[8]/button""").click()
    delay1()
    checkout = driver.find_element_by_xpath("""//*[@id="minicart_overlay"]/div[2]/a[2]""").click()
    delay1()
    name = driver.find_element_by_xpath("""//*[@id="dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName"]""").send_keys(Name)
    lastName = driver.find_element_by_xpath("""//*[@id="dwfrm_delivery_singleshipping_shippingAddress_addressFields_lastName"]""").send_keys(LastName)
    address = driver.find_element_by_xpath("""//*[@id="dwfrm_delivery_singleshipping_shippingAddress_addressFields_address1"]""").send_keys(StreetAddress)
    city = driver.find_element_by_xpath("""//*[@id="dwfrm_delivery_singleshipping_shippingAddress_addressFields_city"]""").send_keys(CityName)
    stateDropdown = driver.find_element_by_xpath("""//*[@id="dwfrm_delivery"]/div[2]/div[2]/div/fieldset/div/div[1]/div[6]/div[1]/div/div/a""").click()
    delay1()
    state = driver.find_element_by_xpath("""//*[@id="dwfrm_delivery"]/div[2]/div[2]/div/fieldset/div/div[1]/div[6]/div[1]/div/div/div/div[2]/div/ul/li[18]""").click()
    delay1()
    zipCode = driver.find_element_by_xpath("""//*[@id="dwfrm_delivery_singleshipping_shippingAddress_addressFields_zip"]""").send_keys(ZipCode)
    phoneNumber = driver.find_element_by_xpath("""//*[@id="dwfrm_delivery_singleshipping_shippingAddress_addressFields_phone"]""").send_keys(PhoneNumber)
    email = driver.find_element_by_xpath("""//*[@id="dwfrm_delivery_singleshipping_shippingAddress_email_emailAddress"]""").send_keys(Email)
    delay1()
    shippingOption = driver.find_element_by_xpath("""//*[@id="shippingoptions"]/div/ul/li[2]""").click()
    delay1()
    reviewAndPay = driver.find_element_by_xpath("""//*[@id="dwfrm_delivery_savedelivery"]""").click()

def Startup():
    Running = True
    Bought = False
    webDriver = webdriver.Chrome()
    ##webDriver.get("http://www.adidas.com/us/ultra-boost-uncaged-chinese-new-year-shoes/BB3522.html")
    webDriver.get("http://www.adidas.com/us/alphabounce-xeno-shoes/B39074.html")
    while Running:
        print("Checking Status")
        webDriver.refresh()
        if (Bought == False and webDriver.find_element_by_xpath("""//*[@id="buy-block"]/div[1]/div[5]/div[2]/form/div[8]/button""").is_enabled()):
            BuyShoes(webDriver)
            Bought = True
            Running = False
        time.sleep(1)
    print("Shoes Have Been Added To Cart And Other Info Entered Automatically")
    input()

Startup()


    
