# company 3SS
# API: https://www.3ss.tv/careers#open-positions


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
import uuid
from bs4 import BeautifulSoup


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from 3SS API.
    """

    response = requests.get('https://www.3ss.tv/careers#open-positions')
    soup = BeautifulSoup(response.text, 'lxml')

    list_of_jobs = []
    jobs = soup.find_all('div', class_='list-jobs-item w-dyn-item')

    for job in jobs:
        link = 'https://www.3ss.tv' + job.find('a', class_='link-job-item w-inline-block')['href']
        title = job.find('h3', class_='h3 left').text.strip()
        locations = job.find_all('div', class_='caption')
        cities = []
        list_cities = ['BraÈ\x99ov', 'Targu MureÈ\x99', 'Cluj-Napoca']

        for city in locations:
            if city.text in list_cities:
                cities.append(city.text)

        list_of_jobs.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "company": "3SS",
            "job_link": link,
            "country": "Romania",
            "city": cities
        })
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """"
    Update data on pe viitor API!
    """
    return data_list

company_name = "3SS"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("3SS", "https://assets-global.website-files.com/5f2bf44086e9ed3d6fc6099d/637a13ae2913f938ce3ede58_3SS%20Logo.svg"))