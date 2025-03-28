# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_adminPage(self):
    self.driver.get("http://127.0.0.1:5001/teton/1.6/index.html")
    self.driver.set_window_size(1198, 697)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    self.driver.find_element(By.ID, "username").click()
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").send_keys("username:")
    self.driver.find_element(By.ID, "password").click()
    elements = self.driver.find_elements(By.ID, "password")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "password").send_keys("password")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
  
  def test_directoryPage(self):
    self.driver.get("http://127.0.0.1:5001/teton/1.6/index.html")
    self.driver.set_window_size(1198, 697)
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    elements = self.driver.find_elements(By.ID, "directory-grid")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.ID, "directory-list")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "directory-list").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
    assert len(elements) > 0
  
  def test_homePage(self):
    self.driver.get("http://127.0.0.1:5001/teton/1.6/index.html")
    self.driver.set_window_size(1198, 697)
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us!")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join Us!").click()
    self.driver.find_element(By.NAME, "fname").click()
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("zackaryy")
    self.driver.find_element(By.NAME, "lname").click()
    elements = self.driver.find_elements(By.NAME, "lname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "lname").send_keys("sssinclairrr")
    self.driver.find_element(By.NAME, "bizname").click()
    elements = self.driver.find_elements(By.NAME, "bizname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "bizname").send_keys("clean upppp")
    self.driver.find_element(By.NAME, "biztitle").click()
    elements = self.driver.find_elements(By.NAME, "biztitle")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "biztitle").send_keys("boss")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("email@gmail.com")
  
  def test_joinPage(self):
    self.driver.get("http://127.0.0.1:5001/teton/1.6/index.html")
    self.driver.set_window_size(1198, 697)
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    self.driver.find_element(By.NAME, "fname").click()
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("zzzzz")
    self.driver.find_element(By.NAME, "lname").click()
    elements = self.driver.find_elements(By.NAME, "lname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "lname").send_keys("ssssss")
    self.driver.find_element(By.NAME, "bizname").click()
    elements = self.driver.find_elements(By.NAME, "bizname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "bizname").send_keys("worker")
    self.driver.find_element(By.NAME, "biztitle").click()
    elements = self.driver.find_elements(By.NAME, "biztitle")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("boss")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.NAME, "email").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "email").send_keys("noemail@email.com")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "cellphone")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "cellphone").send_keys("2813308004")
    self.driver.find_element(By.NAME, "submit").click()
  
