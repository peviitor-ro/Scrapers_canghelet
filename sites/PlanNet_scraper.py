# company: Plan.Net
# API: https://www.plan-net.ro/ro/cariera.html#joburi-disponibile


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
import uuid
from bs4 import BeautifulSoup


def get_all_jobs():
    """
        ... this func() makes a simple requests
        and collects data from Plan.Net API.
    """

    response = requests.get('https://www.plan-net.ro/ro/cariera.html#joburi-disponibile', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    list_of_jobs = []
    jobs = soup.find_all('li', class_='latest-jobs-article')
    for job in jobs:
        link = ('https://www.plan-net.ro' + job.find('a')['href'])
        title = job.find('a').text.strip()
        location = job.find('p').text.split(' ')[-1].strip()
        list_of_jobs.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Plan.Net",
            "country": "Romania",
            "city": location})
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = 'Plan.Net'
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo('Plan.Net','https://www.plan-net.be/en/_jcr_content/root/header-iparsys/header/logo_with_link/image.coreimg.svg/1578492492470.svg'))

