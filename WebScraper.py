import json
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# Pulls the url link and allows the html code to be viewed
url = "https://en.wikipedia.org/wiki/Family_tree_of_Swedish_monarchs"
page = urllib.request.urlopen(url)

# Shows the html
soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())

# Shows the html tags 'tbody' and everything that resides in it.
sort_table = soup.find_all('tbody')
# print(sort_table)

name = []

# Scours on these elements and appends anything that are inside of them.
for row in sort_table[1].find_all('td'):
    cells = row.find_all('a')
    missing = row.find_all('td')
    if len(cells) == 1:
        name.append(cells[0].find(text=True))

    elif len(cells) == 2:
        name.append(cells[0].find(text=True))
        name.append(cells[1].find(text=True))

    elif len(cells) == 3:
        name.append(cells[0].find(text=True))
        name.append(cells[1].find(text=True))
        name.append(cells[2].find(text=True))

# List of the monarchs that are int the wikipage.
monarchs = ['Eric the Victorious', 'Olof Skötkonung', 'Estrid of the Obotrites', 'Emund the Old', 'Anund Jacob',
            'Unknown name', 'Stenkil', 'Eric and Eric', 'Anund Gårdske', 'Halsten Stenkilsson', 'Inge the Elder',
            'Helena', 'Blot-Sweyn', 'Håkan the Red', 'Philip Halstensson', 'Inge the Younger', 'Ulvhild Håkansdotter',
            'Niels, King of Denmark', 'Margaret Fredkulla', 'Ragnvald Ingesson', 'Katarina Ingesdotter',
            'Björn Haraldsen Ironside', 'Ragnvald Knaphövde', 'Sverker I', 'Richeza of Poland', 'Magnus I',
            'Ingrid Ragnvaldsdotter', 'Henrik Skadelår', 'Christina of Denmark', 'Eric IX', 'Charles VII', 'Boleslaw',
            'Sophia of Minsk', 'Valdemar I of Denmark', 'Magnus II', 'Canute I', 'Sverker II', 'Richeza of Denmark',
            'Eric X', 'Canute II', 'John I', 'Birger Jarl', 'Ingeborg Eriksdotter of Sweden', 'Eric XI', 'Magnus III',
            'Valdemar', 'Eric, Duke of Södermanland', 'Birger', 'Albert II, Duke of Mecklenburg', 'Euphemia of Sweden',
            'Valdemar IV of Denmark', 'Magnus IV', 'Albert', 'Ingeborg of Mecklenburg',
            'Henry III, Duke of Mecklenburg', 'Ingeborg of Denmark', 'Margaret I', 'Haakon', 'Eric XII',
            'Wartislaw VII, Duke of Pomerania', 'Wartislaw VII, Duke of Pomerania', 'Maria of Mecklenburg',
            'Gerhard VI, Count of Holstein-Rendsburg', 'John, Count Palatine of Neumarkt', 'Catherine of Pomerania',
            'Eric XIII', 'Helvig of Schauenburg', 'Christopher', 'Dorothea of Brandenburg', 'Christian I',
            'Charles VIII', 'John II', 'King Frederick I of Denmark', 'Christian II', 'Gustav I',
            'King Christian III of Denmark', 'Adolf, Duke of Holstein-Gottorp', 'Eric XIV', 'John III', 'Charles IX',
            'John Adolf, Duke of Holstein-Gottorp', 'Sigismund', 'Gustav II Adolph', 'Princess Catherine',
            'John Casimir, Count Palatine of Kleeburg', 'Frederick III, Duke of Holstein-Gottorp', 'Christina',
            'Charles X Gustav', 'Christina Magdalena of the Palatinate-Zweibrücken',
            'Frederick VI, Margrave of Baden-Durlach', 'Charles XI', 'John Frederick, Margrave of Brandenburg-Ansbach',
            'Johanna Elisabeth of Baden-Durlach', 'Frederick VII, Margrave of Baden-Durlach',
            'Christian Albert, Duke of Holstein-Gottorp', 'Frederick I', 'Ulrika Eleonora', 'Charles XII',
            'Dorothea Friederike of Brandenburg-Ansbach', 'Johann Reinhard III, Count of Hanau-Lichtenberg',
            'Margravine Albertina Frederica of Baden-Durlach', 'Christian August of Holstein-Gottorp, Prince of Eutin',
            'Louis VIII, Landgrave of Hesse-Darmstadt', 'Countess Charlotte of Hanau-Lichtenberg', 'Adolf Frederick',
            'Prince George William of Hesse-Darmstadt', 'Maximilian I Joseph of Bavaria',
            'Princess Augusta Wilhelmine of Hesse-Darmstadt', 'Gustav III', 'Charles XIII', 'Charles XIV John',
            'Eugène de Beauharnais', 'Princess Augusta of Bavaria', 'Gustav IV Adolf', 'Oscar I',
            'Josephine of Leuchtenberg', 'Leopold, Grand Duke of Baden', 'Princess Sophie', 'Crown Prince Gustav',
            'Charles XV', 'Prince Gustaf', 'Oscar II', 'Frederick I, Grand Duke of Baden',
            'King Frederick VIII of Denmark', 'Princess Louise', 'Prince Carl Oscar', 'Gustaf V', 'Victoria of Baden',
            'Gustaf VI Adolf', 'Prince Gustaf Adolf', 'Carl XVI Gustaf', 'Crown Princess Victoria',
            'Prince Carl Philip', 'Princess Estelle']

# Removes anything unnecessary besides the monarchs.
for i in name:
    if i not in monarchs:
        name.remove(i)

# Removes any none element values that are put into the list.
filtered_Name = [i for i in name if i]

# Checks if there's any missing monarchs that aren't in the list
for x in monarchs:
    if x not in filtered_Name:
        print(x)

# Checks the amount of monarchs that have been listed down: The total should be 133.
print(len(filtered_Name))
print(filtered_Name)

# Turns the list into a dataframe
df = pd.DataFrame(filtered_Name, columns=["Name"])

# Converts the dataframe into a JSON
data = df.to_json(orient='index')
with open('monarchs', 'w') as json_file:
    json.dump(data, json_file)
