import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class UsingUnittest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path = "./chromedriver")

  def test_hello_world(self):
    driver = self.driver
    driver.get("https://twitter.com/platzi")

    search_input = driver.find_elements_by_class_name('r-r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-1sp51qo r-1swcuj1 r-1dz5y72 r-1ttztb7 r-13qz1uu')
    search_input.click()

    search_input.send_keys("NathFilms")
    search_input.send_keys(Keys.ENTER)
    nath = driver.find_elements_by_class_name('r-1w50u8q')
    nath.click()

    # search_bar.send_keys(Keys.ENTER)
  
  def tearDown(self):
    print('Browser is about to close...')
    sleep(5)
    self.driver.close()

if __name__ == "__main__":
  unittest.main()