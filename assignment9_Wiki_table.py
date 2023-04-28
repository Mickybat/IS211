import requests
from bs4 import BeautifulSoup


def scrape_page(url):

    page = requests.get(url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, features='lxml')
    # Pull the table
    result_table = soup.find_all('table', class_="wikitable sortable")
    # Get all the rows "tr"s
    rows = result_table[0].find_all('tr')
    # Parse the headers
    headers = rows[0].find_all("th")
    # print the header
    print(
        f"{headers[0].text.strip():<15} - {headers[1].text.strip():<40}"
        f"{headers[2].text.strip():<45} - {headers[3].text.strip():<25}"
        f"{headers[4].text.strip():<35} - {headers[5].text.strip():<40}"
        f"{headers[6].text.strip():<40} - {headers[7].text.strip():<20}"
        f"{headers[8].text.strip():<25} - {headers[9].text.strip():<20}"
    )
    # Get all the cells
    for row in rows:
        cells = row.find_all("td")
        if not cells:
            continue
        print(
            f"{cells[0].text.strip():<15} - {cells[1].text.strip():<40} - "
            f"{cells[2].text.strip():<45} - {cells[3].text.strip():<25}"
            f"{cells[4].text.strip():<35} - {cells[5].text.strip():<40}"
            f"{cells[6].text.strip():<40} - {cells[7].text.strip():<20}"
            f"{cells[8].text.strip():<25} - {cells[9].text.strip():<20}"
        )


if __name__ == "__main__":
    """Main entry point"""
    URL = 'https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions'
    scrape_page(URL)
