# company: Evolution
# API: https://careers.evolution.com/all-vacancies/?location=Romania#jobWidget


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from Evolution API.
    """

    response = requests.get('https://careers.evolution.com/wp-json/wp/v2/vacancies',
        headers=DEFAULT_HEADERS).json()


    list_of_jobs = []
    for job in response:
        title = job['name']
        id = job['id']
        location = job['location']['city']
        link = f'https://careers.evolution.com/job/{id}/'

        if 'Bucharest' in location:
            list_of_jobs.append({
                "job_title": title,
                "company": "evolution",
                "job_link": link,
                "country": "Romania",
                "city": location

        })

    return list_of_jobs

@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API
    """
    return data_list

company_name = "evolution"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("evolution", "https://www.evolution.com/wp-content/themes/evolution-wp/assets/img/evolution_logo.svg"))

