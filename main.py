from selenium import webdriver
import time

def startDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox') 
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-software-rasterizer')
    driver = webdriver.Chrome("./chromedriver", options=options)
    return driver

def login(driver, email, password):
    driver.get("https://www.chocolatesjet.com/fabricadechocolates/")
    emailField = driver.find_element_by_id("email")
    emailField.send_keys(email)
    passField = driver.find_element_by_id("password")
    passField.send_keys(password)
    driver.find_element_by_id("login-button").click()
    time.sleep(2)
    print(driver.find_element_by_id("user-name").get_attribute("innerHTML"))
    pass

def completeLevel(driver):
    pipes = driver.find_elements_by_xpath("//*[@data-type='i'] | //*[@data-type='l']")
    for pipe in pipes:
        pipeType = pipe.get_attribute("data-type")
        current = int(pipe.get_attribute("data-current-rotation"))
        expected = int(pipe.get_attribute("data-expected-rotation"))
        clicks = int((expected - current) / 90)
        if clicks < 0:
            clicks = clicks + 2 if pipeType == 'i' else clicks
            clicks = clicks + 4 if pipeType == 'l' else clicks
        for x in range(clicks):
            pipe.click()
    pass

def main():
    driver = startDriver()
    login(driver, "emai@domain.com", "password")
    driver.get("https://www.chocolatesjet.com/fabricadechocolates/juego.php")
    
    completeLevel(driver)
    time.sleep(.15)
    modalStyle = driver.find_element_by_class_name("custom-modal-wrapper").get_attribute("style")
    while modalStyle != "display: block;":
        modalStyle = driver.find_element_by_class_name("custom-modal-wrapper").get_attribute("style")
        pass
    nextButton = driver.find_element_by_id("form-button")
    nextButton.click()

    modalTitle = driver.find_element_by_class_name("custom-modal-title").get_attribute("innerHTML")
    while modalTitle != "Fin del juego":
        time.sleep(.15)
        completeLevel(driver)
        modalStyle = driver.find_element_by_class_name("custom-modal-wrapper").get_attribute("style")
        while modalStyle != "display: block;":
            modalStyle = driver.find_element_by_class_name("custom-modal-wrapper").get_attribute("style")
            modalTitle = driver.find_element_by_class_name("custom-modal-title").get_attribute("innerHTML")
            modalText = driver.find_element_by_class_name("custom-modal-text").get_attribute("innerHTML")
            pass
        nextButton = driver.find_element_by_id("form-button")
        nextButton.click()
        pass
    
    time.sleep(.2)
    print(modalTitle)
    print(modalText)

if __name__ == '__main__':
    main()
