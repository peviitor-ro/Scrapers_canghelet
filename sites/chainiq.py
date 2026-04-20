#company CHAIN IQ
# API: https://careers.chainiq.com/search/?q=&location=Bucharest&sortColumn=referencedate&sortDirection=desc&startrow={page}

from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup
from _county import get_county,translate_city

def get_soup_object(url: str):
    req = requests.get(url=url, headers= DEFAULT_HEADERS, verify=False)
    soup = BeautifulSoup(req.text, 'lxml')

    return soup

def get_number_jobs():
    soup_object = get_soup_object(url='https://careers.chainiq.com/search/?q=&q2=&alertId=&title=&location=Bucharest&date=')
    num_all_jobs = int(soup_object.find('span',class_='paginationLabel').text.split()[-1])

    return num_all_jobs
get_number_jobs()


def get_jobs():
    list_jobs = []
    for page in range(0, get_number_jobs(),25):
        response = get_soup_object(f'https://careers.chainiq.com/search/?q=&location=Bucharest&sortColumn=referencedate&sortDirection=desc&startrow={page}')

        jobs = response.find_all('tr', class_='data-row')
        for job in jobs:
            link = ('https://careers.chainiq.com'+job.find('a', class_ = 'jobTitle-link')['href'])
            title = (job.find('a', class_ = 'jobTitle-link').text)
            city = translate_city(job.find('span', class_ = 'jobLocation').text.split(',')[0].strip())
            county = get_county(city)
            list_jobs.append({
                        "job_title": title,
                        "job_link": link,
                        "company": "CHAINIQ",
                        "country": "Romania",
                        "city": city,
                        "county": county
                        })
    return list_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list

company_name = "CHAINIQ"
data_list = get_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo('CHAINIQ', 'https://chainiq.com/wp-content/themes/chain-iq/assets/svg/chain-iq-logo-black.svg'))


