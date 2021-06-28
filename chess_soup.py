"""
Parse the html pages containing the Top 100 FIDE rated players for various dates.

The only function that should typically be called from outside the module
is get_full_player_list. It returns a dictionary that can be converted
to a Pandas dataframe.
"""

import datetime
from bs4 import BeautifulSoup

month_numbers = {'January': 1,
                 'February': 2,
                 'March': 3,
                 'April': 4,
                 'May': 5,
                 'June': 6,
                 'July': 7,
                 'August' : 8,
                 'September' : 9,
                 'October': 10,
                 'November': 11,
                 'December': 12}

def get_top100(page):
    """ Get month, year and player list from top 100 FIDE rating page | obj -> tuple(int, int, list(obj))"""
    top100 = page.find("table", {"width":"450"})
    date_text = page.find('td', {'class':'contentheading', 'width':'100%'}).text
    month_start = date_text.rfind(' ', 0, -16) + 1
    month_text = date_text[month_start:-16]
    month = month_numbers[month_text.title()]
    year = int(page.find('td', {'class':'contentheading', 'width':'100%'}).text[-15:-11])
    return (month, year, list(top100.children)[1:])

def get_player(player):
    """ Extract relevant info from a player entry | obj -> dict(str, str, int, int, int)"""
    entry = list(player)
    name = entry[1].text[1:]
    country = entry[3].text[1:]
    rating = entry[4].text[1:]
    games = entry[5].text[1:]
    year = entry[6].text[1:]
    return {
        'name': name,
        'country': country,
        'rating': int(rating),
        'games': int(games),
        'birth_year': int(year)
    }

def get_player_list(top100):
    """ Parses all player entries from a top 100 list | list(obj) -> list(dict) """
    player_list = []
    for number, player in enumerate(top100):
        player = get_player(player)
        player['rank'] = number + 1
        player_list.append(player)
    return player_list

def get_page_items(filename):
    """ Open and parse top 100 html page | string -> tuple(int, int, list(dict)) """
    with open(filename, 'r') as page:
        soup = BeautifulSoup(page, 'html.parser')
    top100 = get_top100(soup)
    month = top100[0]
    year = top100[1]
    player_list = get_player_list(top100[2])
    return (month, year, player_list)

def get_full_player_list(pages=157):
    """ Open and parse all top 100 html pages | None -> list(dict)
    
    The pages keyword argument was set at a default 157 as a quick
    and dirty way to avoid downloading non-existent pages, but it will need to be
    increased to get the latest rating lists.
    """
    full_player_list = []
    for page in range(pages):
        month, year, player_list = get_page_items('pages/chess' + str(page + 1) + '.html')
        for player in player_list:
            player['age'] = year - player['birth_year']
            player['rating_list'] = datetime.date(year, month, 1)
            full_player_list.append(player)
    print('Done')
    return full_player_list
