import selenium
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestNegativeLogin:
    def test_invalid_login(self):
        # Configure Chrome options
        options = Options()
        options.headless = False  # Ensure the browser is visible
        options.add_argument("--start-maximized")
        # Open browser using ChromeDriverManager
        print("Starting Chrome browser...")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        print("Browser started successfully.")


        try:
            print("Navigating to the login page...")
            # Navigate to the practice test login page
            driver.get("https://practicetestautomation.com/practice-test-login/")
            time.sleep(3)
            print("Entering username...")
            # Type username "incorrectUser" into Username field
            username_locator = driver.find_element(By.ID, "username")
            username_locator.send_keys("incorrectUser")
            print("Entering password...")
            # Type password "Password123" into Password field
            password_locator = driver.find_element(By.ID, "password")
            password_locator.send_keys("Password123")
            print("Clicking the submit button...")
            # Push Submit button
            button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
            button_locator.click()
            time.sleep(3)  # Wait for the page to load
            print("Verifying error message for invalid username...")
            # Verify error message is displayed
            error_message_locator = driver.find_element(By.ID, "error")
            assert error_message_locator.is_displayed()
            # Verify error message text is "Your username is invalid!"
            assert error_message_locator.text == "Your username is invalid!"
            print("Error message for invalid username verified successfully.")
            print("Entering username for password test...")
            # Test case 2: Negative username test
            # Type username "student" into Username field
            username_locator.clear()
            username_locator.send_keys("student")
            print("Entering incorrect password...")
            # Type password "incorrectPassword" into Password field
            password_locator.clear()
            password_locator.send_keys("incorrectPassword")
            print("Clicking the submit button for password test...")
            # Push Submit button
            button_locator.click()
            time.sleep(3)  # Wait for the page to load
            print("Verifying error message for invalid password...")
            # Verify error message is displayed
            assert error_message_locator.is_displayed()
            # Verify error message text is "Your password is invalid!"
            assert error_message_locator.text == "Your password is invalid!"
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
        finally:
            print("Closing the browser...")
            # Ensure the browser is closed properly
            driver.quit()
