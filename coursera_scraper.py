from bs4 import BeautifulSoup
import requests
import csv

def get_soup(site):
    source = requests.get(site).text
    return BeautifulSoup(source, 'lxml')

def get_title(soup):    
    try:
        return soup.find('h1').text
    except:
        return 'Null'


def get_rating_val(soup):
    try:
        rating_val = soup.find('span', attrs={'data-test' : 'number-star-rating'}).text[:-5]    
        return float(rating_val)
    except:
        return 'Null'

def get_enroll_count(soup):
    try:
        enroll_count = soup.find('div',class_='rc-ProductMetrics').div.span.span.text
        return int(enroll_count.replace(',',''))
    except:
        return 'Null'

def get_main_category(soup):
    try: 
        return soup.find_all('div',class_='_1ruggxy')[1].a.text
    except:
        return 'Null'

# def get_sub_category(soup):
#     try: 
#         return soup.find_all('div',class_='_1ruggxy')[2].a.text
#     except:
#         return 'Null'



source = requests.get('https://www.coursera.org/sitemap~www~courses.xml').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('coursera_dataset.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Rating Value', 'Enrollment Count', 'Main Category'])

for site in soup.find_all('loc')[:10]:
    site_soup = get_soup(site.text)
    title = get_title(site_soup)
    rating_val = get_rating_val(site_soup)
    enroll_count =    get_enroll_count(site_soup)
    main_category = get_main_category(site_soup)
    csv_writer.writerow([title, rating_val, enroll_count, main_category])


csv_file.close()




