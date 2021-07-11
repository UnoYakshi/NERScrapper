from fastapi.testclient import TestClient
from nerscrap.main import app


client = TestClient(app)

URLS = [
    # 'https://google.com',
    # 'http://yakshi.uno',
    # 'https://hands.ru/company/about',
    # 'https://repetitors.info',
    'https://rosreestr.gov.ru/site/'
]


def test_phones():
    response = client.get("/phones", json={'urls': URLS})
    assert response.status_code == 200
    # assert response.json() == {'phones': []}
