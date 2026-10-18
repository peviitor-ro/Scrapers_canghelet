# company: Vitamin Software
# API: https://vitaminsoftware.com/jobs


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
from bs4 import BeautifulSoup
import requests
import uuid


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from Vitamin Software jobs page.
    """

    response = requests.get('https://vitaminsoftware.com/jobs',
                            headers=DEFAULT_HEADERS).text

    soup = BeautifulSoup(response, 'html.parser')

    list_of_jobs = []
    for anchor in soup.select('a[href*="vitaminsoftware.bamboohr.com/careers/"]'):
        link = anchor['href'].strip()
        title = anchor.get_text(strip=True).split(' - ')[0].strip()

        if not title or not link:
            continue

        list_of_jobs.append({"id": str(uuid.uuid4()),
                             "job_title": title,
                             "job_link": link,
                             "company": "VitaminSoftware",
                             "country": "Romania",
                             "city": "Bucuresti",
                             "county": "Bucuresti",
                             "remote": "remote"})

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
print(update_logo("VitaminSoftware",
      "https://vitaminsoftware.bamboohr.com/manage/logo/?v=31"))
