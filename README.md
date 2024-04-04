# Web Scraping Susamusa Website

This project aims to scrape the Susamusa website, a brand that sells trending female wears, to collect data about their clothes catalogue using Python's BeautifulSoup and Requests libraries. By automating the process of extracting data from the website, we can gather valuable information about the products they offer.

## Technologies Used
- Requests: Used to send HTTP requests to the Susamusa website and retrieve the HTML content of the web pages.
- BeautifulSoup: Utilized for parsing the HTML content obtained from the website, making it easier to navigate and extract the desired data.
- Pandas: Used for data manipulation and organization.
- User-Agent: Implemented to mimic real user behavior and avoid being detected as a bot by the website's security measures.

## Process Overview
1. Sending HTTP Requests: We start by sending HTTP requests to the Susamusa website to obtain the HTML content of the web pages containing the clothes catalogue.

2. Parsing HTML Content: Once we receive the HTML content, we use BeautifulSoup to parse it, allowing us to navigate through the structure of the web pages and locate the relevant information.

3. Scraping Data: We identify the specific HTML elements that contain the product information we want to extract, such as product names, prices, descriptions, and images. We use BeautifulSoup's methods to extract this data from the HTML.

4. Handling Pagination: Since the clothes catalogue may span multiple pages, we implement a loop to navigate through each page and scrape its content iteratively.

5. Organizing Data: We store the scraped data in a Python list, organizing it into structured format for further processing.

6. Converting to DataFrame: Once we have collected all the data, we convert the Python list into a Pandas DataFrame for easier manipulation and analysis.

7. Saving Data to CSV: Finally, we save the DataFrame containing the scraped data as a CSV file for future reference and analysis.

## Usage
To run the web scraping script:

1. Ensure you have Python installed on your system.
2. Install the necessary libraries using pip: pip install requests beautifulsoup4 pandas.
3. Run the Python script to initiate the scraping process: python scrape_susamusa.py

## Disclaimer
This project is intended for educational purposes only. Always adhere to the terms of service of the website you are scraping and respect their policies regarding data usage and scraping activities.

### website view

![image](https://github.com/FaeyO/websrcapping-clothing-brand-website/assets/118575325/b5f5caf0-d66a-4da5-b955-e9bb7cefa01b)
