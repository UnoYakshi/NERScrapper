from bs4 import BeautifulSoup


NAVBAR_KWS = []
FOOTER_KWS = []


def filter_js(soup: BeautifulSoup) -> BeautifulSoup:
    """Removes all the JS code from the given BS4 object..."""
    for script in soup(['script']):
        script.extract()
    return soup


def filter_css(soup: BeautifulSoup) -> BeautifulSoup:
    """Removes all the CSS from the given BS4 object..."""
    for script in soup(['style']):
        script.extract()
    return soup


def filter_navbar(soup: BeautifulSoup) -> BeautifulSoup:
    """Tries to remove all the navigation bar sections from the given BS4 object..."""
    for script in soup(NAVBAR_KWS):
        script.extract()
    return soup


def filter_footer(soup: BeautifulSoup) -> BeautifulSoup:
    """Tries to remove all the footer-related sections from the given BS4 object..."""
    for script in soup(FOOTER_KWS):
        script.extract()
    return soup
