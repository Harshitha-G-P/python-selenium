# Selenium Python

## ⚙️ Setup Instructions

### Clone the project

```bash
git clone https://github.com/Harshitha-G-P/python-selenium
cd python-selenium
```

### Create and activate a virtual environment then Install project dependencies

#### For Windows:
```bash
pip install uv
uv venv
.\env\Scripts\activate
uv sync --all-extras --dev
```

#### For Mac:
```bash
python3 -m pip install uv
uv venv
source .venv/bin/activate
uv sync --all-extras --dev
```

### Create .env File

Create a `.env` file in the project root directory to securely store project secrets and configuration variables. This
file will be used to define key-value pairs for various parameters required by the project. Add the following properties
to the `.env` file:

| Parameter              | Description                             | Example Value                 |
|------------------------|-----------------------------------------|-------------------------------|
| EMAIL                  | Your email address for authentication   | "your@email.com"              |
| PASSWORD               | Your secret password for authentication | "your_secret_password"        |
| VRT_APIURL             | Visual Regression Tracker API URL       | "https://vrt.example.com/api" |
| VRT_PROJECT            | Visual Regression Tracker Project ID    | "project_id"                  |
| VRT_CIBUILDID          | Visual Regression Tracker Build Number  | "build_number"                |
| VRT_BRANCHNAME         | Visual Regression Tracker Branch Name   | "main"                        |
| VRT_APIKEY             | Visual Regression Tracker API Key       | "your_api_key"                |
| VRT_ENABLESOFTASSERT   | Enable Soft Assertions                  | True (or False)               |
| MAILINATOR_API_KEY     | API Key for Mailinator service          | "your_mailinator_api_key"     |
| MAILINATOR_DOMAIN_NAME | Domain name for Mailinator              | "your_mailinator_domain"      |

## 🏃‍♂️ Running Tests

```bash
pytest --driver <firefox/chrome_headless>
```

When no browser was selected then chrome will be used.

* Run according to tags:

```bash
pytest -m <tag_name> --browser <firefox/chrome_headless>
```

## 📊 Viewing Test Results

### Install Allure Commandline To View Test results

#### For Windows:

Follow the instructions [here](https://scoop.sh/) to install Scoop.<br>
Run the following command to install Allure using Scoop:

```bash
scoop install allure
```

#### For Mac:

```bash
brew install allure
```

### View Results Locally:

```bash
allure serve allure-results
```

## ℹ️ View Help And Other CLI Options

```bash
pytest --help
```

### Pre Commit

#### Run Pre Commit Checks Automatically

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

#### Bump Pre Commit Hooks Version

```bash
pre-commit autoupdate
```

#### Run Pre Commit Checks Manually On The Entire Project

```bash
pre-commit run --all-files
```
