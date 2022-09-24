from importlib.abc import ExecutionLoader
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="path/to/driver")
driver = webdriver.Chrome(service=service)