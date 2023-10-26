# company: SugarCRM
# API: https://jobs.lever.co/sugarcrm


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup
import uuid


def get_all_jobs():
        """
        ... this func() makes a simple requests
        and collects data from SugarCRM API.
        """

        response = requests.get('https://jobs.lever.co/sugarcrm', headers=DEFAULT_HEADERS)
        soup = BeautifulSoup(response.text, 'lxml')

        list_of_jobs = []
        jobs = soup.find_all('div', class_='posting')
        for job in jobs:
            link = (job.find('a', class_ = 'posting-title')['href'])
            title = job.find('h5').text.strip()
            location = job.find('span', class_ = 'sort-by-location posting-category small-category-label location').text.split(',')[0].strip()
            if 'Romania' in location or 'Craiova' in location:
                list_of_jobs.append({
                    "id": str(uuid.uuid4()),
                    "job_title": title,
                    "job_link": link,
                    "company": "SugarCRM",
                    "country": "Romania",
                    "city": location})

        return list_of_jobs

@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = 'SugarCRM'
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo('SugarCRM', 'https://www.sugarcrm.com/uk/wp-content/themes/sugarcrm/dist/images/sugarcrm-logo-blk.svg'))