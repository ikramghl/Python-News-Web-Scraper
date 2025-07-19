# Python-News-Web-Scraper

This project features a simple yet efficient Python script that illustrates how to retrieve the latest news headlines from a website utilizing requests and BeautifulSoup. Web scraping is a valuable technique for extracting data from web pages, enabling applications such as data analysis, automation, and real-time content updates.

---

## Program Steps

1. **Import the necessary libraries**  
   The script uses `requests` to send HTTP requests and `BeautifulSoup` from `bs4` to parse and navigate HTML.

2. **Send an HTTP request to the website**  
   A GET request is made to the target news website URL to fetch the HTML content.

3. **Parse the HTML content**  
   The retrieved HTML content is parsed using `BeautifulSoup` for easy navigation and data extraction.

4. **Identify the HTML elements containing the desired information**  
   The page's structure is inspected to find the specific tags that contain the headlines.

5. **Extract and display the headlines**  
   Extracted headlines are cleaned and printed in a readable format, and saved to a `.txt` file.


---

##  Tools Used

- **Python 3.13** - language used to build the scraper
- **Requests** – For sending HTTP requests to fetch webpage content
- **BeautifulSoup (bs4)** – For parsing and navigating HTML
- **Visual Studio Code** – editor used for development and testing
