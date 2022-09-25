# avoid use of unittests module for this example:
# TODO: follow up with unittests module implementation example

# credit: https://automatetheboringstuff.com/2e/chapter20/

import os
import pandas as pd
import pyautogui as pag
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

from .data import formData, keyPresses


class PracticalExampleAutomation:

    _DEFAULT_PATH: str = os.path.join(os.environ.get("HOME"), "mods", "chromedriver")
    # _test_url courtesy of Al Sweigart - automate the boring stuff with python
    _test_url: str = "https://autbor.com/form"
    # _service = ChromeService(executable_path=_driver_path)
    # _options = webdriver.ChromeOptions

    def __init__(self, driver_path: str | None = _DEFAULT_PATH):
        self._service = ChromeService(executable_path=driver_path)

    def test_page_loads(self):
        # driver = webdriver.Chrome()
        with webdriver.Chrome(service=self._service) as driver:
            driver.get(self._test_url)

            title = driver.title
            assert title == "Generic Form"

            driver.implicitly_wait(20.0)

            driver.quit()

    def test_fill_form(self):
        with webdriver.Chrome(service=self._service) as driver:

            driver.get(self._test_url)
            driver.implicitly_wait(20.0)
            driver.quit()

    # def test_fill_form_from_source(self, driver, data:list(dict)):
    #     pass

    def fill_form(self, driver, data: dict):
        pass

        # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="")

    def test_fill_example(self):
        # this is almost verbatim with the following modifications:
        #   - dictionary is rendered into a dataframe for iteration
        #   - use of webdriver allows script the begin browser session
        df = pd.DataFrame(data=formData)

        sourceInputs = keyPresses.get("source")
        robocopInputs = keyPresses.get("robocop")

        with webdriver.Chrome(service=self._service) as driver:
            driver.get(self._test_url)
            driver.implicitly_wait(10.0)
            for idx, person in df.iterrows():
                print("Press CTRL+C to halt execution NOW!!!")
                time.sleep(5)
                print(f"Entering {person['name']}'s information...")

                ## SELENIUM DEBUG
                driver.implicitly_wait(0.5)

                # tab into first cell; even if unable to access directly from driver.findElementById this will work to bring the first input field into focus
                pag.write(["\t", "\t", "\t", "\t"], 0.5)

                # begin writing values to fields
                pag.write(person["name"] + "\t", 0.5)
                pag.write(person["fear"] + "\t", 0.5)

                ## input keys for dropdown listitems
                source = person["source"]
                currKeyPresses = []
                inputKey, numberOfPresses = sourceInputs.get(source)

                # convert tuple to series of input commands + add other necessary key presses to advance
                currKeyPresses.extend([inputKey] * numberOfPresses)
                currKeyPresses.extend(["enter"])
                currKeyPresses.extend(["\t"])

                print(
                    f"value: {source} key: {inputKey} presses: {numberOfPresses} :: {currKeyPresses}"
                )
                pag.write(currKeyPresses, 1.0)

                ## input keys for radio buttons
                robocop = person["robocop"]
                currKeyPresses = []
                inputKey, numberOfPresses = robocopInputs.get(robocop)

                currKeyPresses.extend([inputKey] * numberOfPresses)
                currKeyPresses.extend(["\t", "\t"])
                print(
                    f"value: {robocop} key: {inputKey} presses: {numberOfPresses} :: {currKeyPresses}"
                )
                pag.write(currKeyPresses, 1.0)

                pag.write(person["comments"] + "\t", 0.5)

                time.sleep(1.0)
                # submit form
                pag.press("enter")
                time.sleep(10.0)

                # tab to link for another submission
                pag.write(["\t"], 0.5)
                # advance to next submission
                pag.press("enter")
