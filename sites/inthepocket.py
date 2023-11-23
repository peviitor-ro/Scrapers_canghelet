# company in the Pocket
# API: https://www.inthepocket.com/careers

from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from in the Pocket API.
    """


    response = requests.get('https://www.inthepocket.com/careers', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    list_of_jobs = []
    jobs = soup.find_all('div', class_='do_not_remove_career__item w-dyn-item')
    for job in jobs:
        try:
            link = ('https://www.inthepocket.com'+job.find('a').get('href'))
        except:
            link = None

        if link is not None and 'jobs/' in link:

            title = job.find('a').text.strip()


            if '89200' in job.find('div', class_='do_not_remove_careers__div').text:

                list_of_jobs.append({
                     "job_title": title,
                     "company": "inthePocket",
                     "job_link": link,
                     "country": "Romania",
                     "city": 'Bucuresti'
                })

    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "inthePocket"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("inthePocket", "https://media.licdn.com/dms/image/C4E0BAQEEf_0PuRSBQg/company-logo_200_200/0/1636019709603/in_the_pocket_logo?e=1708560000&v=beta&t=Pq7AD1__VKnMwad2fPXEXpdcq3DEHGsmXCIt-We495A"))