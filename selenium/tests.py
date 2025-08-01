import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


# Finds the Uniform Resourse Identifier of a file
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


# Sets up web driver using Google chrome
driver = webdriver.Chrome()


class WebPageTests(unittest.TestCase):
    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "increase")

        increase.click()

        counter = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(counter.text, "1")

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "increase")

        for _ in range(20):
            increase.click()

        counter = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(counter.text, "20")

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element(By.ID, "decrease")

        for _ in range(15):
            decrease.click()

        counter = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(counter.text, "-15")


if __name__ == "__main__":
    unittest.main()
