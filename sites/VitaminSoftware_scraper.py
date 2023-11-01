# company: Vitamin Software
# API: https://vitaminsoftware.bamboohr.com/careers/


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
import uuid


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from Vitamin Software API.
    """

    response = requests.get('https://vitaminsoftware.bamboohr.com/careers/list', headers=DEFAULT_HEADERS).json()['result']

    list_of_jobs = []
    for job in response:
        title = job['jobOpeningName']
        id = job['id']
        link = f'https://vitaminsoftware.bamboohr.com/careers/{id}/detail'

        list_of_jobs.append({"id": str(uuid.uuid4()),
                             "job_title": title,
                             "job_link": link,
                             "company": "VitaminSoftware",
                             "country": "Romania",
                             "city": "Bucuresti",
                             "job_type": "Remote"})

    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "VitaminSoftware"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("VitaminSoftware", "https://vitaminsoftware.bamboohr.com/manage/logo/?v=31"))






