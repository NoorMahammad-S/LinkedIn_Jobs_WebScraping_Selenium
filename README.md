# Job Listing Scraper for LinkedIn

## Overview

This repository contains a Python script that uses **Selenium WebDriver** to scrape job listings from LinkedIn for specific companies. The script collects job titles, locations, and the corresponding companies, storing the data in both CSV and JSON formats. This tool is helpful for job market analysis, recruitment, or researching specific companies' hiring trends.

## Key Features

- **Scrape Job Listings**: Collect job titles and their respective locations from LinkedIn.
- **Search Multiple Companies**: Easily scrape job listings from any set of companies (e.g., Google, Microsoft, Amazon).
- **Export Data**: Save the scraped data in CSV and JSON formats.
- **Headless Browser**: Uses Selenium's headless mode, which allows the script to run without opening the browser window.
- **Limit Results**: Collect only the first 10 job listings for each company to optimize performance.

## Prerequisites

Before running the script, make sure you have the following installed:

- **Python 3.x**
- **Selenium**: Web scraping library used to interact with LinkedIn.
- **ChromeDriver**: Web driver for Google Chrome browser. Make sure the version matches your Chrome browser version.
- **Pandas**: For handling data and saving it in CSV and JSON formats.

You can install the required Python libraries using `pip`:

```bash
pip install selenium pandas
```

## Usage

### 1. Clone the repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/NoorMahammad-S/LinkedIn_Jobs_WebScraping_Selenium.git
cd LinkedIn_Jobs_WebScraping_Selenium
```

### 2. Update the Script (Optional)

You can modify the `companies` list in the script to include the companies you want to scrape job listings for:

```python
companies = ['Google', 'Microsoft', 'Amazon']
```

### 3. Run the Script

Execute the script to start scraping job listings from LinkedIn:

```bash
python main.py
```

### 4. View the Results

Once the script finishes running, you will find the following files generated:

- `job_listings.csv`: A CSV file containing job titles, company names, and locations.
- `job_listings.json`: A JSON file containing the same data in a different format.

You can open these files using any text editor, spreadsheet software like Microsoft Excel, or use them in data analysis tools.

## Script Details

This Python script performs the following steps:

1. **Set Up Selenium WebDriver**: Configures the headless mode of Chrome using Selenium WebDriver.
2. **Company Search**: Loops through a list of companies and searches for job listings on LinkedIn.
3. **Extract Job Information**: For each job listing, it extracts the job title and location.
4. **Data Storage**: Stores the scraped data in both CSV and JSON formats for easy accessibility and further analysis.

### Example Job Data:

| Company   | Job Title               | Location      |
|-----------|-------------------------|---------------|
| Google    | Software Engineer       | Mountain View, CA |
| Microsoft | Data Scientist          | Redmond, WA   |
| Amazon    | Cloud Solutions Architect | Seattle, WA  |

## Limitations

- **Captcha Handling**: LinkedIn may display a CAPTCHA during automated scraping attempts. You may need to handle it manually or consider integrating CAPTCHA-solving services.
- **LinkedIn API**: This script does not use LinkedIn’s official API. It scrapes the job listings directly from the webpage, which could be against LinkedIn’s terms of service.
- **Rate Limiting**: LinkedIn might block your IP if too many requests are sent in a short period. It's recommended to use rate-limiting techniques or avoid scraping too frequently.

## Contributing

Contributions are welcome! If you'd like to improve the functionality of this script or add new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or need assistance, feel free to open an issue on GitHub.

---
