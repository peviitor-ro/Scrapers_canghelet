# company: ONAPSIS
# API: https://boards.greenhouse.io/embed/job_board?for=onapsis&b=https%3A%2F%2Fonapsis.com%2Fcompany%2Fcareers


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup
from _county import get_county, translate_city


def get_all_jobs():
    response = requests.get('https://boards.greenhouse.io/embed/job_board?for=onapsis&b=https%3A%2F%2Fonapsis.com%2Fcompany%2Fcareers', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    list_of_jobs = []
    jobs = soup.find_all('tr', class_='job-post')

    for job in jobs:
        link_tag = job.find('a', href=True)
        title_tag = job.find('p', class_='body body--medium')
        location_tag = job.find('p', class_='body body__secondary body--metadata')
        if not link_tag or not title_tag or not location_tag:
            continue

        location = location_tag.get_text(strip=True)
        if 'Bucharest' not in location or 'Romania' not in location:
            continue

        city = translate_city('Bucharest')
        county = get_county(city)
        list_of_jobs.append({
            "job_title": title_tag.get_text(strip=True),
            "job_link": link_tag['href'],
            "company": "ONAPSIS",
            "country": "Romania",
            "city": city,
            "county": county,
        })
    return list_of_jobs

@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API
    """
    return data_list

company_name = 'ONAPSIS'
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo('ONAPSIS', 'https://onapsis.com/sites/default/files/Onapsis_Logo_KO.png'))
