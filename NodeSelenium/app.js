const { By, Builder } = require("selenium-webdriver");
const { suite } = require("selenium-webdriver/testing");
const assert = require("assert");
const chrome = require("selenium-webdriver/chrome");
const path = require("path");
const driverPath = path.join(process.env["HOME"], "mods", "chromedriver");

// this script is an alternative to using the approach dictated by use of const suite available by require('selenium-webdriver/testing');
// explanation: suite(fn) doesn't use hardcoded service supplied in Builder().setChromeService(service).build() and instead uses a function that depends on PATH to determine available selenium browser exe's

// for more information see index.js getAvailableBrowsers() and suite init()

let service;
let driver;

async function begin() {
  console.log("building driver...");
  service = new chrome.ServiceBuilder(driverPath);
  console.log(service);
  driver = await new Builder()
    .forBrowser("chrome")
    .setChromeService(service)
    .build();
}

async function run() {
  console.log("testing browser...");
  await driver.get("https://www.selenium.dev/selenium/web/web-form.html");

  let title = await driver.getTitle();
  assert.equal("Web form", title);

  await driver.manage().setTimeouts({ implicit: 500 });

  let textBox = await driver.findElement(By.name("my-text"));
  let submitButton = await driver.findElement(By.css("button"));

  await textBox.sendKeys("Selenium");
  await submitButton.click();

  let message = await driver.findElement(By.id("message"));
  let value = await message.getText();
  assert.equal("Received!", value);
}

async function end() {
  await driver.quit();
}

async function main() {
  await begin();
  await run();
  await end();
}

main();
