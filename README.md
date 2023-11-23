[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oB7VDeFN)

# ExplorationActivity2

## 1. Package/Library

This sample program demonstrates the usage of the following Python libraries:

- `BeautifulSoup` (from `bs4`) for parsing and navigating HTML content.
- `sqlite3` for storing data scraped inside internal database.

## 2. How to Run

To run this program, follow these steps:

### Prerequisites

- Python 3 installed on your computer.
- Install required libraries by running:

`pip install requests beautifulsoup4`

### Execution

1. Clone this repository or download the Python script.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using Python:

`python scrap_news.py`

## 3. Purpose

The purpose of this program is to demonstrate web scraping techniques using BeautifulSoup library from python. It scrapes news articles from CBC Canada for specified provinces.
Furthermore, it utilizes sqlite3 to store scrapted data inside local SQLite database. This database ensures that the scraped data remains accessible even when user exits and reconnects to the program.

## 4. Sample Input/Output

### EX 1) When selecting option '1' to scrape data:

- The program will scrape news articles from CBC's Canada section for provinces like New Brunswick, Prince Edward Island, Nova Scotia, and Newfoundland and Labrador.
- It will extract the title, summary, and location of each article and insert the data into the internal database.
- Upon completion, it prints following message:
<pre>
<code>
Data successfully scraped and inserted into the database
</code>
</pre>

### EX 2) When selecting option '2' to view data:

- The program will retrieve and display all the scraped data in order of title, summary, location, and scraped time:

<pre>
<code>
(1, 'Moncton teen walks out of court with time served for 2022 shooting death', 'The Moncton teen who pleaded guilty to manslaughter in the shooting death of Joedin Leger last year will not have to return to jail.', 'new-brunswick', '2023-11-23 17:01:11')
(... and other news article in identical format)
</code>
</pre>

Note: The actual news content will vary based on the data available on the CBC Canada website.

### EX 3) When selecting option '3' to delete every record:

- The program will prompt for confirmation.
- If confirmed, it will delete all records from the database.

<pre>
<code>
Are you sure you want to delete all records? (yes/no): yes
All records deleted from the database.
</code>
</pre>
