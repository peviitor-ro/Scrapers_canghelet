# company: ENEA
# API: https://careers.enea.com/jobs?country=Romania&query=


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from ENEA API.
    """

    list_of_jobs = []
    response = requests.get('https://careers.enea.com/jobs?country=Romania&query=', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    jobs = soup.find_all('li', class_ = 'w-full')

    for job in jobs:
        try:
            link = job.find('a').get('href')
        except:
            link = None

        if link is not None and 'jobs/' in link:
            title = job.find('span',class_='text-block-base-link sm:min-w-[25%] sm:truncate company-link-style').text.strip()
            location = job.find('div', class_='mt-1 text-md').text.split('·')[1].split(',')[-2].strip()
            list_of_jobs.append({
                "job_title": title,
                "job_link": link,
                "company": "ENEA",
                "country": "Romania",
                "city": location})
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