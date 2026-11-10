# company: SugarCRM
# API: https://api.ashbyhq.com/posting-api/job-board/sugarai


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests


def get_all_jobs():
    """
    ... this func() makes a simple requests
    and collects data from SugarCRM API.
    """

    response = requests.get(
        'https://api.ashbyhq.com/posting-api/job-board/sugarai',
        headers=DEFAULT_HEADERS).json()['jobs']

    list_of_jobs = []
    for job in response:
        title = job['title']
        link = job['jobUrl']
        location = job['location']

        if 'Romania' in location or 'Craiova' in location:
            list_of_jobs.append({
                "job_title": title,
                "job_link": link,
                "company": "SugarCRM",
                "country": "Romania",
                "city": "Craiova",
                "county": "Dolj"
            })

    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = 'SugarCRM'
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo('SugarCRM',
      'https://app.ashbyhq.com/api/images/org-theme-wordmark/6ef21256-985f-4ba7-8d4e-d162fda43cbb/feb254c0-97ee-4490-abd0-d6e0d38e870b/52df7f25-d470-4b03-9c0f-c221e3a6c701.png'))
