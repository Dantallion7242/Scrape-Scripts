import os
import csv
import datetime
import requests
from bs4 import BeautifulSoup

def scrape_reviews(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all review div elements on the page
    reviews = soup.find_all('div', class_='review')
    
    # Extract review data and return as a list of dictionaries
    review_data = []
    for review in reviews:
        title_element = review.find("h2", class_="review-title")
        content_element = review.find("p", class_="review-content")
        if title_element and content_element:
            title = title_element.text.strip()
            content = content_element.text.strip()
            review_data.append({"title": title, "content": content})
    
    return review_data

def scrape_all_pages(base_url, total_pages):
    all_divs = []

    for page_number in range(1, total_pages + 1):
        url = f"{base_url}{page_number}/"
        print(f"Scraping page {page_number}")
        soup = scrape_reviews(url)
        divs = soup.find_all('div')
        all_divs.extend(divs)

    return all_divs
def save_reviews_to_csv(reviews, file_path):
    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "content"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reviews)
    print(f"Data has been saved to {file_path}")
def scrape_all_pages(base_url, total_pages):
    all_divs = []
    for page_number in range(1, total_pages + 1):
        url = f"{base_url}{page_number}/"
        print(f"Scraping page {page_number}")
        soup = scrape_reviews(url)
        divs = soup.find_all('div')
        all_divs.extend(divs)
    return all_divs

def save_divs_to_file(divs, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        for div in divs:
            file.write(str(div))
            file.write("\n")
def main():
    base_url = "https://www.airlinequality.com/airline-reviews/british-airways/page/"
    total_pages = 375
    folder_path = r"C:\Users\Leopo\work\reviews"
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Scrape reviews from all pages
    all_reviews = scrape_all_pages(base_url, total_pages)
    
    # Get the current date for the file name
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
       # Scrape all div elements from all pages
    all_divs = scrape_all_pages(base_url, total_pages)
    
    # Define the file path
    file_path = os.path.join(folder_path, "all_divs.txt")
    
    # Save all divs to a file
    save_divs_to_file(all_divs, file_path)
    print(f"All <div> elements have been saved to {file_path}")


if __name__ == "__main__":
    main()