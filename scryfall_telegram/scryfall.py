import requests


BASE_URL = "https://api.scryfall.com/"


def cards_search(query: str, order: str = None, page: int = 1):
    response = requests.get(BASE_URL + 'cards/search',
                            params={
                                'q': query,
                                'order': order or 'name',
                                'page': page
                            })
    content = response.json()

    return content

