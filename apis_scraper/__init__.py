import json as _json
import os as _os
import time as _time
from time import sleep as _sleep

import requests as _requests
from bs4 import BeautifulSoup as _BeautifulSoup


def _get_site():
    for a in range(5):
        try:
            res = _requests.get('http://ewybory.eu/sondaze')
            if res.ok:
                return res
        except Exception as e:
            print(e)
            print('Couldnt get site...')
            _sleep(a)
            print('Trying again...')

    print('Couldnt get site!')
    return None


def _get_name(th):
    return th.find('div').text


def _get_sup(th):
    parts = th.find('strong').text.split(' ')
    if len(parts) != 2:
        # Something is not yes
        return [-1, 0]
    growth = 0
    if parts[1] == '▲':
        growth = 1
    elif parts[1] == '▼':
        growth = -1
    return [float(parts[0]), growth]


def scrape(no_cache=False, cache_file_name='vote-results.json', cache_expire_time=24 * 60 * 60):
    result = {
        'success': False,
        'support': {
            'pis': -1,
            'ko': -1,
            'lewica': -1,
            'konfederacja': -1,
            'psl': -1,
            'polska2050': -1
        },
        'growth': {
            'pis': 0,
            'ko': 0,
            'lewica': 0,
            'konfederacja': 0,
            'psl': 0,
            'polska2050': 0
        }
    }

    get_site = False
    try:
        if no_cache:
            raise ValueError
        modify = _os.path.getmtime(cache_file_name)
        if modify < _time.time() - cache_expire_time:  # If cache file is older than 24h
            raise IOError
        with open(cache_file_name, 'rb') as f:
            print('Got results from cache')
            return _json.load(f)
    except FileNotFoundError:
        print('Cache file not found!')
        get_site = True
    except IOError:
        print('Cache file toot old!')
        get_site = True
    except ValueError:
        print('No-cache set to true, not touching cache files!')
        get_site = True

    if get_site:
        print('Getting the site from internet...')
        res = _get_site()
        if res is None:
            print("Can't get the site! Most probably no internet :/")
            return result
        soup = _BeautifulSoup(res.content, 'html.parser')

    print('Parsing with soup...')

    div = soup.find('div', class_='entry-content clearfix')
    table = div.find('table')
    tr = table.find('tr')
    ths = tr.find_all('th', class_='name_party_poll')

    name_party = {
        'pis': 'pis',
        'ko': 'ko',
        'lewica': 'lewica',
        'konfederacja': 'konfederacja',
        'psl': 'psl',
        'polska 2050': 'polska2050',
        'n.solidarność': 'nowasolidarnosc'
    }

    for i in range(len(name_party)):
        party = name_party.get(_get_name(ths[i]).lower(), None)
        if party is None:
            print("Looks like some unknown party is on graph? "
                  "It's possible that this means that this repo needs update - "
                  "feel free to make an Issue on GitHub about that :)")
            continue
        sup = _get_sup(ths[i])
        result['support'][party] = sup[0]
        result['growth'][party] = sup[1]

    result['success'] = True

    if not no_cache:
        with open(cache_file_name, 'w') as f:
            _json.dump(result, f)

    return result
