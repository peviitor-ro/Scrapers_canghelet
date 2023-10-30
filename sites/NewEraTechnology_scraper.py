# company New Era Technology
# API: https://boards.greenhouse.io/neweratech?t=9455d2142us

from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup
import uuid

def get_all_jobs():

    response = requests.get('https://boards.greenhouse.io/neweratech?t=9455d2142us', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')


    list_of_jobs = []
    jobs = soup.find_all('div', class_ = 'opening')
    for job in jobs:
        link = ('https://boards.greenhouse.io' + job.find('a')['href'])
        title = job.find('a').text.strip()
        city = job.find('span', class_ = 'location').text.split(',')[0].strip()
        location = job.find('span', class_='location').text
        if "Romania" in location:
            list_of_jobs.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "NewEraTechnology",
                "country": "Romania",
                "city": location})
    return list_of_jobs



@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
company_name = 'NewEraTechnology'
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo('NewEraTechnology', 'https://cdn.neweratech.com/us/wp-content/uploads/sites/5/2021/04/newera-tech-logo-200x200-1.png'))