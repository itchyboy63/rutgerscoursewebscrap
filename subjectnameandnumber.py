from bs4 import BeautifulSoup
from urllib.request import urlopen
html=urlopen("https://sis.rutgers.edu/soc/#courses?subject=010&semester=72019&campus=NB&level=U").read().decode("utf-8")
soup = BeautifulSoup(html, features='lxml')
subjectname=soup.find_all('div', {"id": "initJsonData"})
print(subjectname)
