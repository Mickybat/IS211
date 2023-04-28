import requests
from bs4 import BeautifulSoup


def scrape_page(url):

    page = requests.get(url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, features='lxml')
    # Pull the table
    result_table = soup.find_all('table', class_="TableBase-table")
    # Get all the rows "tr"s
    rows = result_table[0].find_all('tr')[:21]

    # Parse the headers
    headers = rows[0].find_all("th")
    # print the header
    print(
        f"{headers[0].text.strip():>0} - {headers[12].text.strip():>55} ")

    for row in rows:
        player_name = row.find_all('span', class_="CellPlayerName--long")
        cells = row.find_all('td', class_="TableBase-bodyTd")
        if not player_name:
            continue
        print(f"{player_name[0].text.strip():>60}")
        if not cells:
            continue
        print(f"{cells[12].text.strip():>60}")


if __name__ == "__main__":
    """Main entry point"""
    URL = 'https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/'
    scrape_page(URL)

