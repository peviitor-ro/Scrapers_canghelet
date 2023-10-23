# company: HOGARTH
# API: https://www.hogarth.com/careers?key=&departments=All&location=413#jobs-list


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
import uuid
from bs4 import BeautifulSoup


def get_all_jobs():
    response = requests.post('https://www.hogarth.com/careers?key=&departments=All&location=413#jobs-list', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')


    list_of_jobs = []
    jobs = soup.find_all('div', class_ = 'views-row')

    for job in jobs:
        link = ('https://www.hogarth.com'+job.find('a')['href'])
        title = job.find('span', class_ = 'field-content').text.strip()
        location = job.find('div', class_ = 'field-content').text.split(',')[0].strip()
        if 'Bucharest' in location:
            list_of_jobs.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "HOGARTH",
                "country": "Romania",
                "city": location})
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API
    """
    return data_list

company_name = 'HOGARTH'
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo('HOGARTH', 'https://images.crunchbase.com/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/v1458646269/jwjdl0o2yhlivkiwsrai.png'))
