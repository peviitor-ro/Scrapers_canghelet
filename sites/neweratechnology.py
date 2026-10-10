# company New Era Technology
# API: https://boards-api.greenhouse.io/v1/boards/neweratech/jobs

from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from _county import translate_city, get_county

API_URL = 'https://boards-api.greenhouse.io/v1/boards/neweratech/jobs'


def get_all_jobs():

    response = requests.get(API_URL, headers=DEFAULT_HEADERS)
    response.raise_for_status()

    list_of_jobs = []
    for job in response.json().get('jobs', []):
        location = (job.get('location') or {}).get('name', '').strip()

        if 'Romania' not in location and 'Bucharest' not in location and 'Bucuresti' not in location:
            continue

        city = location.split(',')[0].split('/')[0].strip()
        if not city or 'Romania' in city:
            city = 'Bucuresti'

        city = translate_city(city)
        list_of_jobs.append({
            "job_title": job.get('title', '').strip(),
            "job_link": job.get('absolute_url'),
            "company": "NewEraTechnology",
            "country": "Romania",
            "city": city,
            "county": get_county(city)
        })
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
