# company OPIS
# API: https://dowjones.jobs/jobs/?q=OPIS&location=Romania



from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
import uuid
from bs4 import BeautifulSoup



def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from OPIS API.
    """

    response = requests.get('https://dowjones.jobs/jobs/?q=OPIS&location=Romania', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    list_of_jobs = []
    jobs = soup.find_all('li', class_='direct_joblisting with_description')

    for job in jobs:
        link = ('https://dowjones.jobs'+ job.find('a',)['href'])
        title = job.find('span', class_ = 'resultHeader').text.strip()
        list_of_jobs.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "OPIS",
            "country": "Romania",
            "city": 'Bucuresti'})
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "OPIS"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("OPIS", "https://www.opisnet.com/wp-content/uploads/2022/02/OPIS_ADJC_Stacked_White-1.png"))
