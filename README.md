# socialbladescraper
A scrapy project to scrape youtube channel stats from scrapy

# YouTube Top 100 Channels Scrapy Project

Welcome! This project is about scraping the top 100 YouTube channels from [Social Blade](https://socialblade.com/youtube/top/100). The HTML structure of the website was a bit complicated, but no worries, we managed to get through it!

## 🚀 Quick Start

1. **Install necessary packages**

    Make sure you have all the necessary packages installed. You can find the list in the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Spider**

    Navigate to the project directory and run the `socialblade_spider`.

    ```bash
    scrapy crawl socialblade_spider -O data.csv
    ```

## 📦 Output

The scraped data will be saved in a CSV file. You can easily open it using spreadsheet software like Microsoft Excel or Google Sheets to analyze the data.

## 🔍 What Was Tricky?

- **Unclear HTML Structure:** The website structure wasn’t very friendly, but we rolled up our sleeves and decoded the necessary parts to scrape the data accurately.

- **HTTP Errors:** We encountered some HTTP 403 and 302 errors during the process. To navigate around these, we utilized headers and cache strategies.

## 📚 Resources

- **Scrapy Documentation:** If you want to dig deeper or face any issues, Scrapy’s official documentation is a great resource: [Scrapy Documentation](https://docs.scrapy.org/en/latest/)

## 🙌 Contributions

Feel free to dive in! Open an issue, submit enhancements, or fix bugs. Your contributions are always welcome!

## 📃 License

This project is open-source and available to everyone. You can use, modify, and distribute it as you like. Enjoy your scraping journey!

---
