from typing import List
import requests

from goose3 import Goose
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request

from filters.core import filter_css, filter_js, filter_footer, filter_navbar
from recognition.phones.ner import recognize_phones
from recognition.phones.regex import extract_phone_numbers

app = FastAPI()


@app.get("/phones")
async def get_phones(request: Request) -> List[str]:
    """

    :param request: We only need to put {'urls': List[str]} in JSON; remember to have the full URL (with http[s])...
    :return:
    """
    request_data = await request.json()
    urls = request_data['urls']

    results = []

    content_extractor = Goose()
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        soup = filter_js(soup)
        soup = filter_css(soup)
        content = soup.text
        #
        # content = content_extractor.extract(url).cleaned_text

        phones = extract_phone_numbers(content)
        # phones = recognize_phones(content)
        results.append(phones)
    return results
