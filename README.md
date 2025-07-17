# PySelenium Automation Tests

This repository contains Selenium-based automated test scripts for testing login functionality on a sample web application. The tests include both **positive** and **negative** login scenarios.

---

## **Features**
1. **Positive Login Test (`test_login.py`)**:
   - Automates the process of testing a valid login scenario.
   - Verifies successful login by checking the URL, success message, and the presence of the "Log out" button.

2. **Negative Login Test (`test_negative_login.py`)**:
   - Tests invalid login scenarios:
     - Invalid username with a valid password.
     - Valid username with an invalid password.
   - Verifies error messages for both scenarios.

---

## **Prerequisites**
- **Python**: Version 3.7 or later installed on your system.
- **Google Chrome**: Installed and up-to-date.
- **Required Python Packages**:
  - `selenium`
  - `webdriver-manager`
  - `pytest`

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
