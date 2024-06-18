# LinkedInChecker
Checks if you have connnections on LinkedIn for a given list of companies

This Python script allows you to check your LinkedIn connections for multiple companies and save the results in a CSV file. It prompts you for your LinkedIn username and password, reads a list of company names from a companies.txt file, and generates LinkedIn search URLs to find connections.
Assumptions
- The user is using macOS.
- Python is installed on the system.

## Installation and Setup
#### Step 1: Install Python

Ensure that Python 3 is installed on your macOS system. You can check if Python is installed by running the following command in Terminal:

    python3 --version

If Python is not installed, you can install it using Homebrew:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install Python using Homebrew:

    brew install python

#### Step 2: Install Required Python Libraries

Install the required Python libraries using pip:

    pip3 install selenium webdriver_manager

#### Step 3: Download ChromeDriver

Download the ChromeDriver that matches your version of Google Chrome from the ChromeDriver [download page](https://googlechromelabs.github.io/chrome-for-testing/#stable).

- Unzip the downloaded file.
- Move the chromedriver file to a folder where you will place your Python script and companies.txt file.

#### Step 4: Prepare the companies.txt File

Create a file named companies.txt in the same directory as your Python script and chromedriver. List each company name on a new line.

## Usage

- Clone the repository or download the Python script LinkedInChecker.py to the directory where chromedriver and companies.txt are located.
- Open Terminal and navigate to the directory containing the files:

    cd /path/to/your/directory

Run the Python script:

    python3 LinkedInChecker.py

When prompted, enter your LinkedIn username and password. The script will log in to LinkedIn, check connections for each company listed in companies.txt, and save the results in a CSV file named linkedin_connections.csv.

Example:

    Enter your LinkedIn username: your_email@example.com
    Enter your LinkedIn password: **********
    Logged in successfully

The script will generate linkedin_connections.csv with the following columns:

- Company Name
- LinkedIn URL
- Number of 1st Connections
- Number of 2nd Connections

## Notes

- Ensure that your LinkedIn credentials are entered correctly.
- Be mindful of LinkedIn's usage policies to avoid account restrictions.

License

This project is licensed under the MIT License. See the LICENSE file for details.
