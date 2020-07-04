# APiS-Scraper
## PL
### Web scraper w Pythonie do pozyskiwania poparcia Polskich partii politycznych!
Oto prosta biblioteka która pobiera strone http://ewybory.eu/sondaze (mam nadzieje że właściciele stronki nie mają nic przeciwko ;), i wyciąga z niej procenty poparcia poszczególnych partii

Możesz je wykorzystać do jakiegoś kreatywnego fajnego projektu :)

#### Jak korzystać?
 - Zainstaluj potrzebne bilbioteki przez pip - `pip install -r requirements.txt`
   Lub `pip install beautifulsoup4 requests`
 - Dodaj plik `apis_scraper.py` do tego samego folderu co reszta projektu
 - Zaimportuj go: `import apis_scraper`
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

## EN
### Python web scraper for getting Polish political parties support percentage!
This is a simple library which downloads site http://ewybory.eu/sondaze (I hope that administators don't mind ;) and scrapes support percentage of each party from it

You can then use it for some fun creative project ;)

#### How to use?
 - Install required libararies with pip - `pip install -r requirements.txt`
   Or `pip install beautifulsoup4 requests`
 - Add file `apis_scraper.py` to the same folder as your project
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
