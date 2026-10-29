"""Scraping component: fetches categories and product data from books.toscrape.com."""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
HEADERS = {"User-Agent": "Mozilla/5.0 (educational scraper project)"}


def _get_soup(url):
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    response.encoding = "utf-8"  # avoids 'Â£' in prices
    return BeautifulSoup(response.text, "html.parser")


def get_categories():
    """Return a list of {'name', 'url'} dicts for every product category."""
    soup = _get_soup(BASE_URL)
    links = soup.select("div.side_categories ul li ul li a")
    return [
        {"name": a.get_text(strip=True), "url": urljoin(BASE_URL, a["href"])}
        for a in links
    ]


def scrape_category(category_url):
    """Scrape every product (following pagination) in one category."""
    products = []
    url = category_url
    while url:
        soup = _get_soup(url)
        for item in soup.select("article.product_pod"):
            link = item.h3.a
            products.append({
                "title": link["title"],
                "price": item.select_one("p.price_color").get_text(strip=True),
                "rating": item.select_one("p.star-rating")["class"][1],
                "availability": item.select_one("p.availability").get_text(strip=True),
                "url": urljoin(url, link["href"]),
            })
        next_link = soup.select_one("li.next a")
        url = urljoin(url, next_link["href"]) if next_link else None
    return products
