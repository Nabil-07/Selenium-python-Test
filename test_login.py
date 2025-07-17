from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


class TestLogin:
    def test_valid_login(self):
        # Configure Chrome options
        options = Options()
        options.headless = False  # Ensure the browser is visible
        options.add_argument("--start-maximized")  # Start browser maximized

        # Open browser using ChromeDriverManager
        print("Starting Chrome browser...")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        print("Browser started successfully.")

        try:
            # Navigate to the practice test login page
            print("Navigating to the login page...")
            driver.get("https://practicetestautomation.com/practice-test-login/")
            time.sleep(3)

            # Type username "student" into Username field
            print("Entering username...")
            username_locator = driver.find_element(By.ID, "username")
            username_locator.send_keys("student")

            # Type password "Password123" into Password field
            print("Entering password...")
            password_locator = driver.find_element(By.ID, "password")
            password_locator.send_keys("Password123")

            # Push Submit button
            print("Clicking the submit button...")
            button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
            button_locator.click()
            time.sleep(3)  # Wait for the page to load

            # Verify new page URL contains the expected URL
            print("Verifying the URL...")
            current_url = driver.current_url
            assert current_url == "https://practicetestautomation.com/logged-in-successfully/"

            # Verify new page contains expected text
            print("Verifying the success message...")
            new_page_text = driver.find_element(By.XPATH, "//h1[@class='post-title']")
            actual_text = new_page_text.text
            assert actual_text == "Logged In Successfully"

            # Verify button "Log out" is displayed on the new page
            print("Verifying the logout button...")
            logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
            assert logout_button_locator.is_displayed()

        except Exception as e:
            print(f"An error occurred: {e}")
            raise

        finally:
            # Ensure the browser is closed properly
            print("Closing the browser...")
            driver.quit()