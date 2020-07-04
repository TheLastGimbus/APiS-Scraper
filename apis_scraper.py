import requests
from bs4 import BeautifulSoup
from time import sleep

def _get_site():
    for a in range(5):
        try:
            res = requests.get('http://ewybory.eu/sondaze')
            if res.ok:
                return res
        except Exception as e:
            print(e)
            print('Couldnt get site...')
            sleep(a)
            print('Trying again...')

    print('Couldnt get site!')
    return None

def _get_name(th):
    return th.find('div').text


def _get_sup(th):
    parts = th.find('strong').text.split(' ')
    growth = 0
    if parts[1] == '➚':
        growth = 1
    elif parts[1] == '➘':
        growth = -1
    return [float(parts[0]), growth]


def scrape():
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

    print('Getting the site...')
    res = _get_site()
    if res is None:
        print("Can't get the site! Most probably no internet :/")
        return result

    print('Parsing with soup...')
    soup = BeautifulSoup(res.content, 'html.parser')

    div = soup.find('div', class_='entry-content clearfix')
    table = div.find('table')
    tr = table.find('tr')
    ths = tr.find_all('th', class_='name_party_poll')

    # PiS
    print('Getting PiS data...')
    if _get_name(ths[0]).lower() != 'pis':
        print("pis is not on it's place on site! Probably site has changed!")
        return result
    pis_sup = _get_sup(ths[0])
    result['support']['pis'] = pis_sup[0]
    result['growth']['pis'] = pis_sup[1]

    # KO
    print('Getting KO data...')
    if _get_name(ths[1]).lower() != 'ko':
        print("ko is not on it's place on site! Probably site has changed!")
        return result
    ko_sup = _get_sup(ths[1])
    result['support']['ko'] = ko_sup[0]
    result['growth']['ko'] = ko_sup[1]

    # Lewica
    print('Getting Lewica data...')
    if _get_name(ths[2]).lower() != 'lewica':
        print("lewica is not on it's place on site! Probably site has changed!")
        return result
    lewica_sup = _get_sup(ths[2])
    result['support']['lewica'] = lewica_sup[0]
    result['growth']['lewica'] = lewica_sup[1]

    # Konfederacja
    print('Getting Konfederacja data...')
    if _get_name(ths[3]).lower() != 'konfederacja':
        print("konfederacja is not on it's place on site! Probably site has changed!")
        return result
    konfederacja_sup = _get_sup(ths[3])
    result['support']['konfederacja'] = konfederacja_sup[0]
    result['growth']['konfederacja'] = konfederacja_sup[1]

    # PSL
    print('Getting PSL data...')
    if _get_name(ths[4]).lower() != 'psl':
        print("psl is not on it's place on site! Probably site has changed!")
        return result
    psl_sup = _get_sup(ths[4])
    result['support']['psl'] = psl_sup[0]
    result['growth']['psl'] = psl_sup[1]

    # Polska 2050
    print('Getting Polska 2050 data...')
    if _get_name(ths[5]).lower() != 'polska 2050':
        print("polska 2050 is not on it's place on site! Probably site has changed!")
        return result
    polska2050_sup = _get_sup(ths[5])
    result['support']['polska2050'] = polska2050_sup[0]
    result['growth']['polska2050'] = polska2050_sup[1]

    result['success'] = True

    return result
