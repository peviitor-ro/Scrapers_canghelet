# company Able
# API: https://ableapp.com/careers#open-positions


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from Able API.
    """

    response = requests.get('https://api.ashbyhq.com/posting-api/job-board/able',
        headers=DEFAULT_HEADERS).json()['jobs']


    list_of_jobs = []
    for job in response:
        title = job['title']
        id = job['id']
        link = f'https://jobs.ashbyhq.com/able/{id}'


        list_of_jobs.append({
            "job_title": title,
            "company": "able",
            "job_link": link,
            "country": "Romania",
            "city": "Bucuresti"

        })

    return list_of_jobs

@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API
    """
    return data_list


company_name="able"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("able", "https://assets-global.website-files.com/6120e54bcdb381b9924f700c/649037cd4935bc23531b4800_logo-able.svg"))