#company: EA Sports
# API: https://www.ea.com/jobs-feed/filter/studio=EA%20Studios%20-%20SPORTS,city=Bucharest


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from EA Sports API.
    """

    response = requests.get('https://www.ea.com/jobs-feed/filter/studio=EA%20Studios%20-%20SPORTS,city=Bucharest', headers=DEFAULT_HEADERS).json()['jobs']

    list_of_jobs = []
    for job in response:

        title = job['title']
        location = job['locations'][0]['city']

        if title =='Rendering Software Engineer':
            location = job['locations'][6]['city']

        if title =='Technical Interface Designer (1 year contract)':
            location = job['locations'][2]['city']

        id = job['reqId']
        link = f'https://ea.gr8people.com/jobs/{id}/rendering-software-engineer?locale=en'

        list_of_jobs.append({
            "job_title": title,
            "company": "easports",
            "job_link": link,
            "country": "Romania",
            "city": location})

    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API
    """
    return data_list


company_name = "easports"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("easports", "https://media.licdn.com/dms/image/C560BAQHgafvDKry3Yg/company-logo_200_200/0/1630656141341/easports_logo?e=1717027200&v=beta&t=jXSgA2To1eNaPCBnwDQD0ZQDgd07x57Sgj84uT85Zzc"))
