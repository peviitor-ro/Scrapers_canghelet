# company: Meteo Control
# API: https://meteocontrol.jobs.personio.de/search.json


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from Meteo Control API.
    """

    response = requests.get('https://meteocontrol.jobs.personio.de/search.json', headers=DEFAULT_HEADERS).json()

    list_of_jobs = []
    for job in response:


        title = job['name']
        location = job['office']
        id = job['id']
        link = f'https://meteocontrol.jobs.personio.de/job/{id}?language=en%3Flanguage%3D&display=en'
        if "Cluj-Napoca" in location:
            list_of_jobs.append({
                "job_title": title,
                 "job_link":link ,
                "company": "meteocontrol",
                "country": "Romania",
                "city": location})

    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "meteocontrol"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("meteocontrol", "https://assets.cdn.personio.de/logos/87288/social/9b6147d6e2e5464861dfca6a104e3eb6.png"))