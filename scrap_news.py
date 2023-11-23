from datetime import datetime
import requests
from bs4 import BeautifulSoup
import sqlite3


def scrap(conn, cursor):
    # Provinces of interest
    provinces = [
        "new-brunswick",
        "prince-edward-island",
        "nova-scotia",
        "newfoundland-labrador",
    ]

    news_data = []

    # loop through the provinces
    for i in provinces:
        page_url = "https://www.cbc.ca/news/canada/" + i
        response = requests.get(page_url)

        # Parse the html content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # locate where news contents are located
        news_contents = soup.find("div", class_="contentArea")

        # Find and extract informations
        news_elements = news_contents.find_all("a", class_="card")

        for news_element in news_elements:
            news = {}
            news["title"] = news_element.find("h3").text
            description_div = news_element.find("div", class_="description")
            if description_div:
                news["summary"] = description_div.text
            else:
                news["summary"] = "Description not available"
            news["location"] = i

            news_data.append(news)

    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for news in news_data:
        # Check if the title already exists in the database
        cursor.execute("SELECT id FROM scraped_data WHERE title = ?", (news["title"],))
        existing_record = cursor.fetchone()
        if not existing_record:
            cursor.execute(
                """
                INSERT INTO scraped_data(title, summary, location, scraped_datetime)
                VALUES (?, ?, ?, ?)""",
                (news["title"], news["summary"], news["location"], current_datetime),
            )
            conn.commit()
    print("Data successfully scraped and inserted into the database")


def view_data(conn, cursor):
    cursor.execute("SELECT * FROM scraped_data")
    rows = cursor.fetchall()

    if not rows:
        print("No data available in the database.")
    else:
        print("Scraped Data:")
        for row in rows:
            print(row)


def delete_all_records(conn, cursor):
    confirm = input("Are you sure you want to delete all records? (yes/no): ")
    if confirm.lower() == "yes":
        cursor.execute("DELETE FROM scraped_data")
        conn.commit()
        print("All records deleted from the database.")
    else:
        print("Deletion canceled.")


def main():
    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()

    # Create table for the scrapted data
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS scraped_data (
               id INTEGER PRIMARY KEY,
               title TEXT UNIQUE,
               summary TEXT,
               location TEXT,
               scraped_datetime TEXT)"""
    )
    # Menu options
    while True:
        print("Main Menu")
        print("1. Scrape data and Insert into Database")
        print("2. View Data from Database")
        print("3. Delete All Records")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            scrap(conn, cursor)
        elif choice == "2":
            view_data(conn, cursor)
        elif choice == "3":
            delete_all_records(conn, cursor)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
