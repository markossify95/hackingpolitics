"""import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen(
    'http://www.parlament.gov.rs/akti/doneti-zakoni/u-sazivu-od-16-%D0%B0prila-2014.3411.html').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

laws_doneti = []
konza = soup.find_all('td', class_='lawtitle')
for i in konza:
    law = i.find('strong').find('a').text
    laws_doneti.append(law)

print('DONETI\n\n')

sauce = urllib.request.urlopen(
    'http://www.parlament.gov.rs/akti/zakoni-u-proceduri/zakoni-u-proceduri.1037.html').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

print('\n\nU PROCESU\n\n')
laws_proces = []
konza = soup.find_all('td', class_='lawtitle')
for i in konza:
    law = i.find('strong').find('a').text
    laws_proces.append(law)


class Act:
    def __init__(self, name, status):
        # name, status = 1 usvojen 0 u proceduri
        self.name = name
        self.status = status

    def get_touple(self):
        return self.name, self.status


doneti_final = []
for obj in laws_doneti:
    x = Act(obj, 1)
    name, status = x.get_touple()
    doneti_final.append((name, status))

uprocesu_final = []
for obj in laws_proces:
    x = Act(obj, 0)
    name, status = x.get_touple()
    uprocesu_final.append((name, status))

print(doneti_final)
print('\n\n')
print(uprocesu_final)


def pucaj(lista):
    for obj in lista:
        topic = 1
        name = obj['name']
        status = obj['status']
        x = Zakon(topic=topic, name=name, status=status)
        x.save()


pucaj(doneti_final)
pucaj(uprocesu_final)"""
