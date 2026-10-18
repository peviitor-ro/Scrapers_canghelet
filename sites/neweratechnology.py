# company New Era Technology
# API: https://boards-api.greenhouse.io/v1/boards/neweratech/jobs

from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from _county import translate_city, get_county

API_URL = 'https://boards-api.greenhouse.io/v1/boards/neweratech/jobs'

ROMANIA_LOCATION_MARKERS = (
    'romania',
    'bucharest',
    'bucuresti',
    'bucurești',
    'cluj',
    'timisoara',
    'timișoara',
    'iasi',
    'iași',
    'brasov',
    'brașov',
    'sibiu',
    'craiova',
    'constanta',
    'constanța',
    'oradea',
    'ploiesti',
    'ploiești',
    'pitesti',
    'pitești',
    'baia mare',
    'bacau',
    'bacău',
    'targu mures',
    'târgu mureș',
    'targu-mures',
)


def is_romania_location(location):
    location_lower = location.lower()
    return any(marker in location_lower for marker in ROMANIA_LOCATION_MARKERS)


def get_all_jobs():

    response = requests.get(API_URL, headers=DEFAULT_HEADERS)
    response.raise_for_status()

    list_of_jobs = []
    for job in response.json().get('jobs', []):
        location = (job.get('location') or {}).get('name', '').strip()

        if not is_romania_location(location):
            continue

        city = location.split(',')[0].split('/')[0].strip()
        if not city or 'romania' in city.lower():
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
