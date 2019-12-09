package edu.uno.tests;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;

import org.junit.*;

import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;

import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class SearchForFastFood {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
	System.setProperty("webdriver.gecko.driver", //
    		  "C:/Users/tkori/workspace4830/project_webapp_testing_windows/lib/win/geckodriver.exe");
	driver = new FirefoxDriver();
    baseUrl = "https://www.katalon.com/";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testSearchForFastFood() throws Exception {
    driver.get("http://127.0.0.1:5000/");
    driver.findElement(By.linkText("Login")).click();
    driver.findElement(By.id("username")).click();
    driver.findElement(By.id("username")).clear();
    driver.findElement(By.id("username")).sendKeys("new");
    driver.findElement(By.id("password")).clear();
    driver.findElement(By.id("password")).sendKeys("new");
    driver.findElement(By.id("remember_me")).click();
    driver.findElement(By.id("submit1")).click();
    driver.findElement(By.id("searchimg")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [addSelection | name=category | label=Delivery]]
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='Menu Search'])[2]/following::option[1]")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [addSelection | name=cuisine | label=American]]
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='Menu Search'])[2]/following::option[16]")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [addSelection | name=establishment | label=Fast Food]]
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='Menu Search'])[2]/following::option[94]")).click();
    driver.findElement(By.xpath("//input[@type='submit']")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='Add'])[4]/following::div[1]")).click();
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
