# company MAGNA
# API: https://magnaelectronicsromania.teamtailor.com/jobs/


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup
import uuid

def get_all_jobs():

    response = requests.get('https://magnaelectronicsromania.teamtailor.com/jobs/', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')
    print(response.status_code)

    list_of_jobs = []
    jobs = soup.find_all('li', class_ = 'transition-opacity duration-150 border rounded block-grid-item border-block-base-text border-opacity-15')
    for job in jobs:
        link = (job.find('a', class_ = 'min-h-[180px] h-full w-full p-4 flex flex-col justify-center text-center hover:bg-block-base-text hover:bg-opacity-3')['href'])
        title = job.find('span', class_ = 'text-block-base-link company-link-style').text.strip()
        # location = job.find('div', class_ = 'mt-1 text-md').text.split(',')[0].strip()
        location = job.find('div', class_='mt-1 text-md').text.split('·')[1].split(',')[0]

        print(link)
        print(title)
        print(location)

        list_of_jobs.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "MAGNA",
            "country": "Romania",
            "city": location})
    return list_of_jobs

print(get_all_jobs())

@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list

company_name = 'MAGNA'
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo('MAGNA', 'https://images.teamtailor-cdn.com/images/s3/teamtailor-production/logotype-v3/image_uploads/6901fc63-3786-4d8b-8230-aa1bcd971324/original.png'))