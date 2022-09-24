# Selenium Automation

This project focuses on getting started with selenium automation in various languages and environments.

## Requirements

Each version of selenium webdriver has a respective set of packages and/or browser driver options, therefore it is best to note __a)__ which programming language will be used and __b)__ which browser (and version) will be accessed. For additional information, please refer to [Selenium's documentation](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/).

<!-- This needs review; It would be best to minimize the amount of packages and adjustments that will be required on a per-project basis by seperating each of the following into their own respective space. -->

## Programming Language Library Requirements
### __Python__

```bash
pip install selenium
```

### __Csharp__

```bash
# installation via dotnet-cli
dotnet add package Selenium.Webdriver
```

### __Node__

```bash
npm install selenium-webdriver
```

## The Browser Driver

A list of compatible browser drivers and their download source can be found [here](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/).


For quick reference, the ones that really matter:
- [Google Chrome](https://chromedriver.chromium.org/downloads)
- [Firefox](https://github.com/mozilla/geckodriver/releases)



Per Selenium Documentation there are 3 ways to manage the webdriver:

1. via third party driver management software
    - [webdriver manager for python](https://github.com/SergeyPirogov/webdriver_manager)
    - [webdriver manager for C#](https://github.com/rosolko/WebDriverManager.Net)
    - none available for node at this time
1. the PATH environment variable
1. a hardcoded path location

__NOTE__: For projects in this repo, a hardcoded path will be used.


## Overview Functions of a Selenium Process

1. Initiate a selenium browser session
1. Take action on a browser
1. Request browser information
1. Establish a waiting strategy
1. Find an element
1. Take action on an element
1. Request element information
1. End the session