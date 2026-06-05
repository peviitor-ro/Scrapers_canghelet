# company: ENEA
# API: https://careers.enea.com/jobs.json


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from _county import get_county, translate_city


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from ENEA JSON feed.
    """

    list_of_jobs = []
    response = requests.get(
        'https://careers.enea.com/jobs.json', headers=DEFAULT_HEADERS)
    data = response.json()

    for item in data.get('items', []):
        job = item.get('_jobposting', {})
        locations = job.get('jobLocation', [])
        if not locations:
            continue

        address = locations[0].get('address', {})
        if address.get('addressCountry') != 'RO':
            continue

        city_raw = address.get('addressLocality', '')
        if not city_raw:
            continue

        city = translate_city(city_raw)
        county = get_county(city)
        list_of_jobs.append({
            "job_title": job.get('title', item.get('title', '')),
            "job_link": item.get('url', ''),
            "company": "ENEA",
            "country": "Romania",
            "city": city,
            "county": county})
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "ENEA"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("ENEA", "https://images.teamtailor-cdn.com/images/s3/teamtailor-production/logotype-v3/image_uploads/a5810fe7-ad47-451d-87d2-3e692b2ae5b1/original.png"))
