from bs4 import BeautifulSoup
import requests

class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        self.title = soup.title.string if soup.title else "No title found"
        for script in soup(["script", "style", "img"]):
            script.decompose()
        self.text = soup.get_text()
    def __str__(self) -> str:
       return self.text 
