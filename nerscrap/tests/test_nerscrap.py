from typing import List

import pytest
from fastapi.testclient import TestClient
from nerscrap.main import app


client = TestClient(app)

URLS_DATA = {
    'https://www.regextester.com/94215': ['79855310868',
                                          '79855310868',
                                          '880084545454',
                                          '880084545454',
                                          '784545487878',
                                          '7889213554654',
                                          '84456464641',
                                          '89855310868'],
    'http://yakshi.uno': [],
    'https://hands.ru/company/about': [],
    'https://repetitors.info': ['880050572838'],
    'https://rosreestr.gov.ru/site/': []
}


@pytest.mark.parametrize('url,expected', [(item[0], item[1]) for item in URLS_DATA.items()])
def test_phones(url: str, expected: List[str]):
    response = client.get("/phones", json={'urls': [url]})
    assert response.status_code == 200
    assert response.json() == expected
