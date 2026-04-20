# company: ENEA
# API: https://careers.enea.com/jobs?country=Romania&query=


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup
from _county import get_county, translate_city


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from ENEA API.
    """

    list_of_jobs = []
    response = requests.get(
        'https://careers.enea.com/jobs?country=Romania&query=', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    jobs = soup.find('ul', id='jobs_list_container').find_all('li', recursive=False)

    for job in jobs:
        link_tag = job.find('a', href=True)
        if not link_tag or 'jobs/' not in link_tag['href']:
            continue

        title = link_tag.get_text(strip=True)
        details = job.find('div', class_='mt-1 text-md')
        if not details:
            continue

        details_text = ' '.join(details.stripped_strings)
        if 'Bucharest, Romania' not in details_text:
            continue

        city = translate_city('Bucharest')
        county = get_county(city)
        list_of_jobs.append({
            "job_title": title,
            "job_link": link_tag['href'],
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
