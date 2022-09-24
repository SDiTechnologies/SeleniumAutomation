# sample code available via selenium docs
# REQUIRES: webdriver_manager packager

# import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# get the location used by the manager and pass it to the service class
service =   Service(executable_path=ChromeDriverManager().install())

# use service instance when initializing the driver
driver = webdriver.Chrome(service=service)