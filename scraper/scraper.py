from bs4 import BeautifulSoup
import requests


def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    citation_needed_arr = soup.find_all(title="Wikipedia: Citation needed")
    print(citation_needed_arr)
    return len(citation_needed_arr)


def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # TODO


if __name__ == "__main__":
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    print(get_citations_needed_count(URL))
