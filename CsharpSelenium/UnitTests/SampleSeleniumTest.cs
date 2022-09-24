using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace UnitTests;

[TestClass]
public class SampleSeleniumTest
{
    protected IWebDriver driver;

    // Python and JS implementations require the full path to the exe; this requires path to the directory only?
    string _driverPath = @$"{Environment.GetEnvironmentVariable("HOME")}/mods";

    [TestInitialize]
    public void CreateDriver()
    {
        // new DriverManager().SetUpDriver(new ChromeConfig());
        // driver = new ChromeDriver();
        driver = new ChromeDriver(_driverPath);
    }

    [TestCleanup]
    public void QuitDriver()
    {
        driver.Quit();
    }

    [TestMethod]
    public void ChromeSession()
    {
        driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");

        var title = driver.Title;
        Assert.AreEqual("Web form", title);

        driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);

        var textBox = driver.FindElement(By.Name("my-text"));
        var submitButton = driver.FindElement(By.TagName("button"));
        
        textBox.SendKeys("Selenium");
        submitButton.Click();
        
        var message = driver.FindElement(By.Id("message"));
        var value = message.Text;
        Assert.AreEqual("Received!", value);
    }
}