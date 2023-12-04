# company: stripe
# API: https://stripe.com/jobs/search?office_locations=Europe--Bucharest


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from stripe API.
    """

    list_of_jobs = []
    response = requests.get('https://stripe.com/jobs/search?office_locations=Europe--Bucharest', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    jobs = soup.find_all('tr', class_='TableRow')

    for job in jobs:
        try:
            link = 'https://stripe.com'+job.find('a').get('href')
        except:
            link = None

        if link is not None and 'jobs/' in link:
            title = job.find('a').text.strip()
            location = job.find('span', class_='JobsListings__locationDisplayName').text.split(',')[0]
            list_of_jobs.append({
                "job_title": title,
                "job_link": link,
                "company": "stripe",
                "country": "Romania",
                "city": location})
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list

company_name = "stripe"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("stripe","https://b.stripecdn.com/site-srv/assets/img/v3/jobs_v2/thumbnails/stripe-c7f91cf715df9fb9d2198e47de6fc3016a82795e.jpg"))