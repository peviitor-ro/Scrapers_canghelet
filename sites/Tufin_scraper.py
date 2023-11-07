# company Tufin
# API: https://www.tufin.com/careers/rd


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
import uuid
from bs4 import BeautifulSoup


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from Tufin API.
    """

    response = requests.get('https://www.tufin.com/careers/rd', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')
    print(response.status_code)

    list_of_jobs = []
    jobs = soup.find_all('div', class_ = 'positions1')

    for job in jobs:
        link = job.find('a')['href']
        title = job.find('span', class_='name').text.strip()
        location = job.find('span', class_ = 'loc-dept').text.split(',')[0].strip()
        if 'Bucharest' in location:
            list_of_jobs.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "Tufin",
                "country": "Romania",
                "city": location})
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "Tufin"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("Tufin", "https://www.tufin.com/wp-content/themes/tufin/images/logo.svg"))