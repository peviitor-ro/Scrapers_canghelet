# company: ONAPSIS
# API: https://boards.greenhouse.io/embed/job_board?for=onapsis&b=https%3A%2F%2Fonapsis.com%2Fcompany%2Fcareers


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
import uuid
from bs4 import BeautifulSoup


def get_all_jobs():
    response = requests.get('https://boards.greenhouse.io/embed/job_board?for=onapsis&b=https%3A%2F%2Fonapsis.com%2Fcompany%2Fcareers', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    list_of_jobs = []
    jobs = soup.find_all('div', class_ = 'opening')

    for job in jobs:
        link = (job.find('a')['href'])
        title = job.find('a').text.strip()
        location = job.find('span', class_ = 'location').text.split(',')[0].strip()
        if 'Bucharest' in location:
            list_of_jobs.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "ONAPSIS",
                "country": "Romania",
                "city": location})
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