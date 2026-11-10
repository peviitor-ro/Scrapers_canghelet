# company Gkn Aerospace
# API: https://joinus.gknaerospace.com/api/jobs


from A_OO_get_post_soup_update_dec import update_peviitor_api
from L_00_logo import update_logo
import requests
from _county import translate_city, get_county

def _is_romanian_job(job):
    country_code = (job.get('countryCode') or '').upper()
    country = (job.get('country') or '').lower()
    location = (job.get('location') or '').split(',')
    location_code = location[-1].strip().upper() if location else ''
    return country_code == 'RO' or 'romania' in country or location_code == 'RO'


def _get_all_jobs(url, headers):
    jobs = []
    page_number = 1
    while True:
        payload = {
            "searchQuery": "",
            "location": "",
            "team": "",
            "startDate": None,
            "endDate": None,
            "pageNumber": page_number,
            "pageSize": 100
        }
        data = requests.post(url, json=payload, headers=headers).json()
        jobs.extend(data.get('items', []))
        if page_number >= data.get('totalPages', 1):
            return jobs
        page_number += 1


def get_jobs():
    """
    ... this func() makes requests
    and collects data from Gkn Aerospace API.
    """

    url = "https://joinus.gknaerospace.com/api/jobs"

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    response = _get_all_jobs(url, headers)

    list_of_jobs = []
    for job in response:
        if not _is_romanian_job(job):
            continue

        title = job['title']
        city = translate_city(job['location'].split(',')[0].strip())
        county = get_county(city)
        id = job['id']
        link = f'https://joinus.gknaerospace.com/job/{id}'
        list_of_jobs.append({
            "job_title": title,
            "company": "GknAerospace",
            "job_link": link,
            "country": "Romania",
            "city": city,
            "county": county
        })
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "GknAerospace"
data_list = get_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("GknAerospace", "https://www.gknaerospace.com/globalassets/global-images/logos/key-facts-logo.png"))