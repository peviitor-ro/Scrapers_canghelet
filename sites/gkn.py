# company Gkn Aerospace
# API: https://joinus.gknaerospace.com/api/jobs


from A_OO_get_post_soup_update_dec import update_peviitor_api
from L_00_logo import update_logo
import requests


def get_jobs():
    """
    ... this func() makes requests
    and collects data from Gkn Aerospace API.
    """

    url = "https://joinus.gknaerospace.com/api/jobs"

    payload = {
        "searchQuery": "",
        "location": "Bucharest, RO",
        "team": "",
        "startDate": None,
        "endDate": None,
        "pageNumber": 1,
        "pageSize": 10
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    response = requests.request("POST", url, json=payload, headers=headers).json()['items']

    list_of_jobs = []
    for job in response:


        title = job['title']
        location = job['location'].split(',')[0]
        id = job['id']
        link = f'https://joinus.gknaerospace.com/job/{id}'
        list_of_jobs.append({
            "job_title": title,
            "company": "GknAerospace",
            "job_link": link,
            "country": "Romania",
            "city": location
        })
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "GknAerospace"
data_list = get_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("GknAerospace", "https://www.gknaerospace.com/globalassets/global-images/logos/key-facts-logo.png"))