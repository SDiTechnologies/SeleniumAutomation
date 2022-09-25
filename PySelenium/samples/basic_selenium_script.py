import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# from webdriver_manager.chrome import ChromeDriverManager

DRIVER_PATH = os.path.join(os.environ.get("HOME"), "mods", "chromedriver")


def test_eight_components():
    # driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    # executable_path is deprecated
    driver = webdriver.Chrome(service=ChromeService(executable_path=DRIVER_PATH))

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()
