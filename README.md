# APiS-Scraper
## PL
### Web scraper w Pythonie do pozyskiwania poparcia Polskich partii politycznych!
Oto prosta biblioteka która pobiera strone http://ewybory.eu/sondaze (mam nadzieje że właściciele stronki nie mają nic przeciwko ;), i wyciąga z niej procenty poparcia poszczególnych partii

Możesz je wykorzystać do jakiegoś kreatywnego fajnego projektu :)

#### Jak korzystać?
 - Zainstaluj: `pip3 install -U apis-scraper`
 - Zaimportuj: `import apis_scraper`
 - Użyj funkcji `apis_scraper.scrape()`. Zwraca ona słownik, wyglądający tak:
```python
{
    'success': True,  # Czy się udało, jeśli nie - False
    'support' : {  # Słownik z % poparcia - liczba z przecinkiem
        'pis': 10.0,
        'ko': 10.0,
        'lewica': 10.0,
        'konfederacja': 10.0,
        'psl': 10.0,
        'polska2050': 10.0
    },  # Jeśli coś pójdzie nie tak, wszysktkie poparcia będą -1 a 'success' = False
    'growth': {  # Czy poparcie rośnie/spada. -1=spada, 0=takie same, 1=rośnie
        'pis': 0,
        'ko': 0,
        'lewica': 0,
        'konfederacja': 0,
        'psl': 0,
        'polska2050': 0
    }
}
```
Przykładowy kod:
```python
import apis_scraper

wyniki = apis_scraper.scrape()
if wyniki['success'] == False:
    print('Nie dało rady - nie ma internetu czy coś :/')
    exit(-1)

if wyniki['support']['pis'] < wyniki['support']['ko']:
    print('Trzeba anulować, bo przegramy...')
```

Domyślnie, biblioteka zapisuje wyniki w pliku `vote-results.json`, żeby nie musiała zawsze pobierać strony z internetu - wyniki i tak zmieniają sie co ~tydzień.
Zapisane wyniki wyczerpują się po 24 godzinach.
Jeśli chcesz to zmienić, możesz:
```python
apis_scraper.scrape(
  no_cache=True,  # Kompletenie wyłącza zapisywanie w pliku - nie polecam
  cache_file_name='dupa12.json',  # Zmienia nazwe pliku
  cache_expire_time=1*60*60
  # Zmienia czas (w sekundach) po którym plik sie wyczerpuje,
  # i strona jest pobierana na nowo
)
```

## EN
### Python web scraper for getting Polish political parties support percentage!
This is a simple library which downloads site http://ewybory.eu/sondaze (I hope that administators don't mind ;) and scrapes support percentage of each party from it

You can then use it for some fun creative project ;)

#### How to use?
 - Install it: `pip3 install -U apis-scraper`
 - Import it: `import apis_scraper`
 - Use function `apis_scraper.scrape()`. It returns a dict, which looks like this:
```python
{
    'success': True,  # If it was succesfull, if not - False
    'support' : {  # Dict with % of support - in float
        'pis': 10.0,
        'ko': 10.0,
        'lewica': 10.0,
        'konfederacja': 10.0,
        'psl': 10.0,
        'polska2050': 10.0
    },  # If something goes wrong, all supports will be -1 and 'success' = False
    'growth': {  # Whether support is growing or falling. -1=falling, 0=stays same, 1=growing
        'pis': 0,
        'ko': 0,
        'lewica': 0,
        'konfederacja': 0,
        'psl': 0,
        'polska2050': 0
    }
}
```

Example code:
```python
import apis_scraper

wyniki = apis_scraper.scrape()
if wyniki['success'] == False:
    print("Can't do - no internet or something :/")
    exit(-1)

if wyniki['support']['pis'] < wyniki['support']['ko']:
    print('We need to cancel, or we will lose...')
```

By default, library saves results in `vote-results.json` file, so it doesn't need to download the site every time - results change ~once a week anyway.
Saved results expire after 24h
If you want to change this, you can:
```python
apis_scraper.scrape(
  no_cache=True,  # Completley disable cache - not recommended
  cache_file_name='dupa12.json',  # Change file name
  cache_expire_time=1*60*60
  # Change time (in seconds) after file expires, and site is downloaded again
)
```
