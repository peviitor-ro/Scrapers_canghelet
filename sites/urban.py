# company: Urban Socializing
# API: https://www.urbansocializing.ro/jobs/


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
import uuid
from bs4 import BeautifulSoup


def get_jobs():

    list_jobs = []

    page = 1
    flag = True

    while flag:

        response = requests.get(f'https://www.urbansocializing.ro/jobs/page/{page}/', headers=DEFAULT_HEADERS)
        soup = BeautifulSoup(response.text, 'lxml')
        jobs = soup.find_all('div', class_='hp-listing__content')


        if len(jobs) > 0:
            for job in jobs:
                link = job.find('a')['href']
                title = job.find('a').text.strip()
                list_city = ['Timisoara', 'Bucuresti']
                try:
                    location = job.find('div', class_='hp-listing__attribute hp-listing__attribute--location').text.split(',')[0].strip().split('/')
                except:
                    location = 'Timisoara'
                    job_type = 'remote'

                if 'Bucuresti' in location:
                   location = list_city

                if 'Remote' in location:
                    location = 'Timisoara'
                    job_type = 'remote'
                else:
                    job_type = 'on-site'

                if 'Cluj' in location:
                    location = 'Cluj-Napoca'

                list_jobs.append({
                    "id": str(uuid.uuid4()),
                    "job_title": title,
                    "job_link": link,
                    "company": "UrbanSocializing",
                    "country": "Romania",
                    "city": location,
                    "remote": job_type})
        else:
            flag = False
        page += 1

    return list_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "UrbanSocializing"
data_list = get_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("UrbanSocializing", 'https://www.urbansocializing.ro/wp-content/uploads/2021/05/logo-red.png'))
