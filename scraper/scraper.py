from bs4 import BeautifulSoup
import requests


def get_citations_needed_count(URL):
    """
    this function will return the number of citations needed in the wiki
    """
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    citation_needed_arr = soup.find_all(title="Wikipedia:Citation needed")
    return len(citation_needed_arr)


def get_citations_needed_report(URL):
    """
    this function will return the information that needs citations in the wiki
    """

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    citation_needed_arr = soup.find_all(title="Wikipedia:Citation needed")
    counter = 0
    obj_citations = {}
    for citation in citation_needed_arr:
        counter += 1
        report = citation.parent.parent.parent.text.strip()
        obj_citations[f"citation needed {counter}"] = report
    return obj_citations


if __name__ == "__main__":
    URL = "https://en.wikipedia.org/wiki/Chicken"
    print(get_citations_needed_count(URL))
