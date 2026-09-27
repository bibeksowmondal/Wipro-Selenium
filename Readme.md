# Selenium Automation Framework

A Python-based Selenium automation framework designed for web application testing using **Selenium WebDriver, PyTest, Unittest, Page Object Model (POM), CSV test data, configuration management, logging, screenshots, and HTML reporting**.

This project was developed as a capstone automation testing project.

---
## 🎥 Video Demonstration

A complete video demonstration of the Selenium Automation Framework is available below.

The demonstration covers the framework execution, test cases, Selenium automation, logging, screenshots, and HTML reporting.

▶️ **[Watch the Project Demonstration Video](https://drive.google.com/file/d/1MXvFti6pXsXYnJT-8ARc1ess3s94Ca4e/view?usp=drive_link)**



## 📌 Project Overview

The goal of this project is to demonstrate a scalable and maintainable Selenium automation framework using Python.

The framework automates common e-commerce application scenarios such as:

- Opening the application
- Login validation
- Product search
- Homepage validation
- Screenshot capture on test failure
- Test data management
- Configuration management
- Logging
- HTML test reporting

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Selenium WebDriver | Web UI Automation |
| PyTest | Test Execution Framework |
| Unittest | Python Unit Testing Framework |
| Page Object Model | Framework Design Pattern |
| CSV | Test Data Management |
| ConfigParser | Configuration Management |
| Logging | Execution Logs |
| PyTest HTML | HTML Test Reports |
| Google Chrome | Test Browser |
| Git & GitHub | Version Control |

---

## 🌐 Application Under Test

The framework uses the TutorialsNinja demo e-commerce application.

Application:

https://tutorialsninja.com/demo/

---

## 📂 Project Structure

```text
Selenium/
│
├── ECommerceAutomation/
│   │
│   ├── config/
│   │   └── config.ini
│   │
│   ├── pages/
│   │   ├── login_page.py
│   │   └── search_page.py
│   │
│   ├── testdata/
│   │   └── test_data.csv
│   │
│   ├── tests/
│   │   ├── test_homepage.py
│   │   ├── test_login.py
│   │   ├── test_product_search.py
│   │   └── test_unittest_homepage.py
│   │
│   ├── utilities/
│   │   ├── config_reader.py
│   │   ├── csv_reader.py
│   │   └── logger.py
│   │
│   ├── screenshots/
│   │
│   ├── reports/
│   │
│   ├── logs/
│   │
│   ├── conftest.py
│   ├── pytest.ini
│   ├── requirements.txt
│   └── .gitignore
│
└── README.md
```
🏗️ Framework Architecture

The framework follows the Page Object Model (POM) design pattern.
```text
Test Cases
    │
    ▼
Page Objects
    │
    ▼
Selenium WebDriver
    │
    ▼
Web Application

Supporting components:

                 ┌─────────────────┐
                 │    Test Cases   │
                 └────────┬────────┘
                          │
                 ┌────────▼────────┐
                 │   Page Objects  │
                 └────────┬────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   Test Data        Configuration       Logger
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                          ▼
                  Selenium WebDriver
```
🧪 Test Scenarios
1. Homepage Test

Validates that the application can be opened successfully and that the expected page title is displayed.

2. Invalid Login Test

Tests login functionality using invalid credentials and verifies that the appropriate warning message is displayed.

3. Product Search Test

Searches for a product and verifies that the search functionality works correctly.

4. Unittest Homepage Test

Demonstrates integration of Python's built-in unittest framework with Selenium.

📊 Test Data

Test data is maintained separately from the test scripts using CSV.

Example:

email,password
invalid@example.com,invalidpassword

This allows test data to be modified without changing the automation code.

⚙️ Configuration

Application configuration is maintained in:

config/config.ini

Example:

[application]
url=https://tutorialsninja.com/demo/

The configuration utility reads the application URL and allows configuration values to be reused across tests.

📸 Screenshots

Screenshots can be captured when a test fails.

Example location:

screenshots/

This helps with debugging failed Selenium tests.

📝 Logging

The framework includes a reusable logging utility.

Logs are stored in:

logs/automation.log

Example log information:

Starting login process
Opening login page
Entering email
Entering password
Clicking login button
Login process completed
📋 HTML Reporting

The project uses pytest-html to generate an HTML execution report.

Run:

pytest --html=reports/report.html

The generated report will be available at:

reports/report.html
🚀 Installation
Step 1: Clone the repository
git clone https://github.com/bibeksowmondal/selenium.git
Step 2: Navigate to the project
cd selenium
cd ECommerceAutomation
Step 3: Create a virtual environment

Windows:

python -m venv venv
Step 4: Activate the virtual environment

Windows PowerShell:

venv\Scripts\activate
Step 5: Install dependencies
pip install -r requirements.txt
▶️ Running Tests
Run all PyTest tests
pytest
Run with verbose output
pytest -v
Run a specific test
pytest tests/test_login.py -v
Run the product search test
pytest tests/test_product_search.py -v
Generate HTML report
pytest --html=reports/report.html
🧪 Running Unittest

Run the Unittest test separately:

python -m unittest tests/test_unittest_homepage.py -v
📈 Example Test Execution

Example:

================ test session starts ================

tests/test_homepage.py::test_open_website PASSED
tests/test_login.py::test_invalid_login PASSED
tests/test_product_search.py::test_product_search PASSED

================ 3 passed ================
🔧 Framework Features

The framework currently demonstrates:

✅ Selenium WebDriver
✅ Python automation
✅ PyTest
✅ Unittest
✅ Page Object Model
✅ Reusable page classes
✅ CSV test data
✅ Configuration management
✅ Logging
✅ Screenshot handling
✅ HTML reporting
✅ Virtual environment
✅ Git version control
🎯 Future Enhancements

The framework can be extended with:

Cross-browser testing
Parallel execution
Explicit wait utilities
Selenium Grid
Jenkins CI/CD integration
Allure reporting
Excel test data
Database validation
API integration
Advanced retry mechanisms
Environment-specific configuration
Data-driven testing with multiple datasets
👨‍💻 Author

Bibek Sowmondal

GitHub:

https://github.com/bibeksowmondal

📄 License

This project is created for educational and automation testing practice purposes.
