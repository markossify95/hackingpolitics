import bs4 as bs
import urllib.request
from parliament.models import Member


def get_links():
    sauce = urllib.request.urlopen('http://www.otvoreniparlament.rs/poslanici/').read()
    soup = bs.BeautifulSoup(sauce, 'html.parser')
    linkovi = []

    links = soup.find_all('ul', class_='clanovi-kluba clearfix')

    for ul in links:
        for li in ul.findAll('li'):
            ahref = li.a['href']
            linkovi.append(ahref)
    return linkovi


class MemberPerson:
    def __init__(self, ime, stranka, bio):
        self.ime = ime
        self.stranka = stranka
        self.bio = bio

    def __repr__(self):
        return self.ime


def get_member_data(path):
    sauce = urllib.request.urlopen(path).read()
    soup = bs.BeautifulSoup(sauce, 'html.parser')
    header = soup.h1.text
    name = ''
    party = ''
    if 'Poslanička grupa ' in header:
        s = header.split('Poslanička grupa ')
        name = s[0]
        party = s[1]
    else:
        name = header.split('Samostalni poslanici')[0]
    biography = ''
    for hit in soup.findAll(attrs={'dir': 'ltr'}):
        biography += hit.text

    mp = MemberPerson(name, party, biography)
    return mp


def get_members_list():
    members = []
    links = get_links()
    for member in links:
        m = get_member_data(member)
        members.append(m)
    return members


print(get_links())
# print(get_member_data('http://www.otvoreniparlament.rs/politicari/aleksandar-cotric/'))
# print(get_members_list())
print()
x = get_members_list()

for obj in x:
    mem = Member(name=obj.name, party=obj.party, bio=obj.bio)
    mem.save()
