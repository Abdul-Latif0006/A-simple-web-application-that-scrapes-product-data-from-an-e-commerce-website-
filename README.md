# E-commerce Product Scraper

## Project Overview
A simple web application that scrapes product data from an e-commerce website
(<https://books.toscrape.com/>, a site built for scraping practice). The user
picks a product category from a dropdown, and the scraped products are shown in
a readable HTML table (title, price, rating, availability and a link).

Built with:
- **Flask**: web framework (routing and templates)
- **BeautifulSoup (bs4)**: HTML parsing for the scraping component
- **requests**: fetching pages

## Project Structure
```
.
├── app.py            # Flask app and routes
├── scraper.py        # Web scraping functions
├── requirements.txt  # Python dependencies
├── README.md
└── templates/
    └── index.html    # Category dropdown and results table
```
`index.html` lives in `templates/`, the folder Flask searches by default, so
no extra configuration is needed.

## Setup
Requires Python 3.8+.

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 2. Install dependencies
pip install -r requirements.txt
```

## How to Run
```bash
python app.py
```
Open <http://127.0.0.1:5000> in your browser, choose a category, and click
**Scrape**.

## Scraper Functions (`scraper.py`)

### `get_categories()`
Fetches the site's home page and reads the sidebar category links. Returns a
list of dictionaries, each with the category `name` and its absolute `url`.
Flask uses this list to build the dropdown.

### `scrape_category(category_url)`
Takes a category URL, scrapes every product on that page, and follows the
"next" link until all pages are covered. Returns a list of dictionaries with
the keys `title`, `price`, `rating`, `availability` and `url`. Flask passes
this list to the template to render the table.

## Notes
- Requests use a 10-second timeout; network errors appear as a message on the
  page instead of crashing the app.
- Only category URLs returned by `get_categories()` are accepted by the app.
- Please scrape responsibly and respect a site's terms of use.
