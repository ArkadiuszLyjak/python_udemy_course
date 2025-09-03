import requests
from bs4 import BeautifulSoup
import time
import csv

BASE_URL = "https://movies.niwszone.com/category/movie/page/1/"
HEADERS = {'User-Agent': 'Mozilla/5.0'}
titles = []


def get_titles_from_page(url):
    res = requests.get(url, headers=HEADERS)
    if res.status_code != 200:
        print(f"Błąd ładowania strony: {url}")
        return []

    soup = BeautifulSoup(res.text, "html.parser")

    # Używamy selektora CSS, który działa
    links = soup.select("h2.entry-title a")

    page_titles = []
    for link in links:
        title = link.get_text(strip=True)
        page_titles.append(title)

    return page_titles


def scrape_all_pages(max_pages=150):
    page = 1
    while page <= max_pages:
        url = BASE_URL if page == 1 else f"{BASE_URL}page/{page}/"
        print(f"Przetwarzanie strony {page}: {url}")
        page_titles = get_titles_from_page(url)
        print(f"Znaleziono {len(page_titles)} filmów na stronie {url}")

        if not page_titles:
            print("Brak kolejnych tytułów lub koniec paginacji.")
            break

        titles.extend(page_titles)
        page += 1
        time.sleep(1)

    return titles


def save_to_txt(titles, filename="filmy_niwszone.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for title in titles:
            f.write(f"{title}\n")
    print(f"Zapisano do pliku TXT: {filename}")


def save_to_csv(titles, filename="filmy_niwszone.csv"):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Lp.", "Tytuł"])
        for i, title in enumerate(titles, 1):
            writer.writerow([i, title])
    print(f"Zapisano do pliku CSV: {filename}")


if __name__ == "__main__":
    all_titles = scrape_all_pages()
    print(f"\nZnaleziono {len(all_titles)} filmów.")

    save_to_txt(all_titles)
    save_to_csv(all_titles)
