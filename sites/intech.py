# company: intech
# API: https://www.in-tech.com/en/career/jobs?country=all&location=bukarest&entryType=all&category=all&type=all&remote=all&search=


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup
from _county import get_county


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from intech API.
    """

    response = requests.get(
        'https://www.in-tech.com/en/career/jobs', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    list_of_jobs = []
    jobs = soup.find_all(
        'div', class_='mt-0.5 bg-white px-standard-s py-standard-xs sm:px-standard-m sm:py-standard-s')

    for job in jobs:
        try:
            link = 'https://www.in-tech.com' + job.find('a').get('href')
        except Exception:
            link = None

        if link is not None and ('jobs/' in link or 'carrers/jobs/' in link):
            try:
                title = job.find('a').text.strip()
            except Exception:
                title = None
            if not title:
                continue
            cities = []
            try:
                location = job.find(
                    'div', class_='m-1 flex flex-row items-center rounded bg-gray-100 p-1 px-2').text.strip().split(', ')
            except Exception:
                location = []

            for city in location:
                if city in ['Brasov', 'Bucuresti', 'Bucharest', 'Bukarest']:
                    cities.append('Bucuresti' if city in ['Bucuresti', 'Bucharest', 'Bukarest'] else city)

            if cities:
                list_of_jobs.append({
                    "job_title": title,
                    "company": "intech",
                    "job_link": link,
                    "country": "Romania",
                    "city": cities,
                    "county": [get_county(city) for city in cities]
                })

    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """"
        Update data on pe viitor API!
    """
    return data_list


company_name = "intech"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("intech",
      "https://imgcdn.bestjobs.eu/cdn/el/plain/employer_logo/58a5c5db02dee.png"))
