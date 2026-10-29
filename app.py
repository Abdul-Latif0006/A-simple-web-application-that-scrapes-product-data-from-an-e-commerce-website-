"""Flask application: lets the user pick a category and displays the scraped products."""
import requests
from flask import Flask, render_template, request
from scraper import get_categories, scrape_category

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    products, selected, error = [], None, None
    try:
        categories = get_categories()
        if request.method == "POST":
            selected = request.form.get("category")
            # only accept URLs that came from our own category list
            if selected in {c["url"] for c in categories}:
                products = scrape_category(selected)
            else:
                error = "Please choose a valid category."
    except requests.RequestException as exc:
        categories, error = [], f"Could not reach the website: {exc}"
    return render_template("index.html", categories=categories,
                           products=products, selected=selected, error=error)


if __name__ == "__main__":
    app.run(debug=True)
