# company: Tain
# API: https://tain.teamtailor.com/jobs?query=


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
import uuid
from bs4 import BeautifulSoup


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from Tain API.
    """

    list_of_jobs = []
    response = requests.get('https://tain.teamtailor.com/jobs?query=', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    jobs = soup.find_all('li', class_='w-full')

    for job in jobs:
        try:
            link = job.find('a').get('href')
        except:
            link = None

        if link is not None and 'jobs/' in link:
            title = job.find('span', class_='text-block-base-link sm:min-w-[25%] sm:truncate company-link-style').text.strip()
            location = job.find('div', class_='mt-1 text-md').text.split('·')[0].split(',')[0]

            if 'București' in location:
                location = 'Bucuresti'

            if 'Bucuresti' in location:
                list_of_jobs.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "Tain",
                "country": "Romania",
                "city": location,
                })
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "Tain"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("Tain", "https://images.teamtailor-cdn.com/images/s3/teamtailor-production/logotype-v3/image_uploads/b9065d15-97d1-4540-8350-012fe28ca460/original.png"))
