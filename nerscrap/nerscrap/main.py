from fastapi import FastAPI, Request
from bs4 import BeautifulSoup
import requests

app = FastAPI()


@app.get("/phones")
async def get_phones(request: Request):
    """

    :param request: We only need to put {'urls': List[str]} in JSON; remember to have the full URL (with http[s])...
    :return:
    """
    request_data = await request.json()
    urls = request_data['urls']
    results = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        results.append(soup.prettify())
    return results
