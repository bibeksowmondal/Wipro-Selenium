Selenium Automation Framework


A Python-based Selenium WebDriver automation framework for testing an e-commerce web application. The project demonstrates PyTest, Unittest, Page Object Model (POM), CSV test data, configuration management, logging, failure screenshots, and HTML reporting.

This project was developed as a Selenium Python automation capstone project with a focus on maintainability, reusability, and clean framework design.

📌 Project Overview

The framework automates key e-commerce application scenarios:

🌐 Application launch and homepage validation

🔐 Login validation using invalid credentials

🔎 Product search

📊 CSV-based test data management

⚙️ Configuration management

📸 Screenshot capture on test failure

📝 Execution logging

📋 HTML test reporting

🧪 PyTest and Unittest execution

🧩 Page Object Model implementation

🌐 Application Under Test

TutorialsNinja Demo E-Commerce Application

Application: https://tutorialsninja.com/demo/

The application is used for educational and automation testing practice.

🛠️ Technology Stack

Technology

Purpose

Python 3.11+

Programming language

Selenium WebDriver

Browser automation

PyTest

Test execution and fixtures

Unittest

Python test framework integration

Page Object Model (POM)

Maintainable framework design

CSV

External test data

ConfigParser

Configuration management

Python Logging

Execution and debugging logs

pytest-html

HTML execution reports

Google Chrome

Test browser

Git / GitHub

Version control

🏗️ Framework Architecture

The framework follows the Page Object Model (POM) approach. Test cases interact with reusable page classes instead of directly managing locators throughout the tests.

┌─────────────────────────┐
│       Test Cases        │
│     PyTest / Unittest   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       Page Objects      │
│ LoginPage / SearchPage  │
└────────────┬────────────┘
             │
      ┌──────┼────────┬────────────┐
      ▼      ▼        ▼            ▼
   Test     Config   Logger     Utilities
   Data
      │      │        │
      └──────┴────────┴────────────┐
                                   ▼
                         ┌──────────────────┐
                         │ Selenium WebDriver│
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Web Application  │
                         └──────────────────┘

📂 Project Structure

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
│   ├── conftest.py
│   ├── pytest.ini
│   ├── requirements.txt
│   └── .gitignore
│
├── .gitignore
└── README.md

Generated artifacts such as screenshots, logs, reports, caches, and the virtual environment should remain excluded through .gitignore.

🧪 Test Scenarios

1. Homepage Validation

Verifies that the application launches successfully and that the expected page title is displayed.

2. Invalid Login

Uses invalid credentials and verifies that the application displays the expected login warning message.

3. Product Search

Searches for a product and validates that the search functionality returns the expected result.

4. Unittest Homepage Test

Demonstrates Selenium execution using Python's built-in unittest framework.

📊 Test Data Management

Test data is maintained separately from test scripts using CSV.

Example:

email,password
invalid@example.com,invalidpassword

This separation allows test data to be updated without modifying the automation logic.

⚙️ Configuration Management

Application configuration is stored in:

ECommerceAutomation/config/config.ini

Example:

[application]
url=https://tutorialsninja.com/demo/

The configuration utility reads the application URL so it can be reused across tests.

📝 Logging

The framework includes a reusable Python logging utility.

Log output is written to:

logs/automation.log

Typical execution events include:

Starting login process
Opening login page
Entering email
Entering password
Clicking login button
Login process completed

Logging helps with debugging and understanding test execution flow.

📸 Screenshot on Failure

The framework supports screenshot capture when a test fails.

Screenshots are stored under:

screenshots/

This provides visual evidence for troubleshooting Selenium failures.

Generated screenshots are excluded from Git tracking through .gitignore.

📋 HTML Reporting

The project uses pytest-html to generate an execution report.

Generate a report with:

pytest --html=reports/report.html

The report is generated at:

reports/report.html

🚀 Installation & Setup

Prerequisites

Make sure the following are installed:

Python 3.11 or later

Google Chrome

Git

pip

1. Clone the Repository

git clone https://github.com/bibeksowmondal/selenium.git

2. Navigate to the Automation Project

cd selenium
cd ECommerceAutomation

3. Create a Virtual Environment

Windows:

python -m venv venv

4. Activate the Virtual Environment

PowerShell:

venv\Scripts\activate

5. Install Dependencies

pip install -r requirements.txt

▶️ Running Tests

Run the complete PyTest suite

pytest

Run with verbose output

pytest -v

Run the login test

pytest tests/test_login.py -v

Run the product search test

pytest tests/test_product_search.py -v

Generate an HTML report

pytest --html=reports/report.html

Run the Unittest test

python -m unittest tests/test_unittest_homepage.py -v

📈 Example Test Execution

A successful PyTest execution looks like:

================ test session starts ================

tests/test_homepage.py::test_open_website PASSED
tests/test_login.py::test_invalid_login PASSED
tests/test_product_search.py::test_product_search PASSED

================ 3 passed ================

✨ Framework Features

✅ Selenium WebDriver automation

✅ Python-based framework

✅ PyTest integration

✅ Unittest integration

✅ Page Object Model

✅ Reusable page classes

✅ CSV-driven test data

✅ Configuration management

✅ Logging

✅ Screenshot capture on failure

✅ HTML reporting

✅ Virtual environment support

✅ Git/GitHub version control

✅ Modular framework structure

🔮 Future Enhancements

The framework can be extended with:

Cross-browser testing

Explicit wait utilities

Parallel test execution

Selenium Grid

Jenkins CI/CD integration

Allure reporting

Excel-based test data

Database validation

API automation integration

Retry mechanisms

Environment-specific configuration

Parameterized and data-driven testing

Browser and environment selection from command line

👨‍💻 Author

Bibek Sowmondal

GitHub: https://github.com/bibeksowmondal

📄 License

This project is created for educational purposes and automation testing practice.
