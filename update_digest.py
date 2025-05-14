import feedparser
from datetime import datetime, timedelta, timezone
import os
from googletrans import Translator

# Inizializza il traduttore
translator = Translator()


def translate_to_italian(text):
    try:
        translated = translator.translate(text, src='en', dest='it')
        return translated.text if translated else text
    except Exception as e:
        print(f"Errore nella traduzione: {e}")
        return text


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "data", "articoli_blog.md")

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

sources = {
    "Krebs on Security": "https://krebsonsecurity.com/feed/ ",
    "Graham Cluley": "https://www.grahamcluley.com/feed/ ",
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews ",
    "BleepingComputer": "https://www.bleepingcomputer.com/feed/ ",

    "Troy Hunt": "https://www.troyhunt.com/rss ",
    "Schneier on Security": "https://www.schneier.com/feed/atom/ ",
    "Threatpost": "https://threatpost.com/feed/ ",
    "Cloudflare Blog - Security": "https://blog.cloudflare.com/tag/security/rss/"
}

today = datetime.now(timezone.utc)
limit_days = 7
cutoff = today - timedelta(days=limit_days)

all_articles = []  

# === Recupera articoli dai feed RSS ===
for name, url in sources.items():
    print(f"Fetching from {name}...")

    try:
        feed = feedparser.parse(url.strip(), sanitize_html=False)

        if feed.get('bozo', 0):
            exception = feed.get('bozo_exception', None)
            if exception:
                print(f"Malformed feed ({name}): {exception}")

            if not feed.entries:
                print(f"Nessun articolo trovato per {name}.")
                continue
            else:
                print(f"Feed parzialmente valido, proseguo con {len(feed.entries)} articoli.")

        for entry in feed.entries:
            try:
                pub_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            except AttributeError:
                print(f"Articolo senza data valida su {name}")
                continue

            if pub_date > cutoff:
                try:
                    title = entry.get("title", "Titolo non disponibile")
                    link = entry.get("link", "#")
                except Exception as e:
                    print(f"Errore nei dati dell'articolo su {name}: {e}")
                    continue

                title_it = translate_to_italian(title)

                all_articles.append({
                    "title": title,
                    "title_it": title_it,
                    "name": name,
                    "pub_date": pub_date,
                    "link": link
                })

    except Exception as e:
        print(f"Impossibile scaricare feed da {name}: {e}")


all_articles.sort(key=lambda x: x["pub_date"], reverse=True)


with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write("# Articoli e Blog Cybersec\n\n")
    f.write(f"## Ultimi {limit_days} giorni\n\n")

    for article in all_articles:
        f.write(f"- **{article['title_it']}**  \n")
        f.write(f"  Fonte: {article['name']}, {article['pub_date'].strftime('%d %b %Y, %H:%M:%S %Z')}  \n")
        f.write(f"  [Leggi](<{article['link']}>)\n\n")
