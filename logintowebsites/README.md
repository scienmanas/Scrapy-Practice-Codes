# Amazon Login using Scrapy Splash

This project demonstrates how to use Scrapy Splash to login to Amazon.

## Prerequisites

Before running the code, make sure you have the following installed:

- Python 3.x
- Scrapy
- Splash

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure Splash:

    - Install Docker (if not already installed)
    - Start the Splash container:

      ```bash
      docker run -p 8050:8050 scrapinghub/splash
      ```

## Usage

1. Open `settings.py` and update the `SPLASH_URL` variable with the URL of your Splash instance.

2. Open `amazon_login/spiders/login_spider.py` and update the `USERNAME` and `PASSWORD` variables with your Amazon login credentials.

3. Run the spider:

    ```bash
    scrapy crawl login
    ```

    This will start the login process and save the response to a file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Purpose

This project was created as part of the [Scrapy Playwright tutorial](https://thepythonscrapyplaybook.com/scrapy-login-form/) and [Amazon India](https://www.amazon.com) was scraped by logining in.

