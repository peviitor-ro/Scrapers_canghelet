# company OPIS
# API: https://dowjones.jobs/jobs/feeds/rss/?q=OPIS&location=Romania


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from xml.etree import ElementTree


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from OPIS API.
    """

    response = requests.get(
        'https://dowjones.jobs/jobs/feeds/rss/', params={'q': 'OPIS', 'location': 'Romania'},
        headers=DEFAULT_HEADERS)

    root = ElementTree.fromstring(response.content)

    list_of_jobs = []
    for job in root.iter('item'):
        title = job.findtext('title', default='').strip()
        link = job.findtext('link', default='').strip()
        if not link:
            continue
        list_of_jobs.append({
            "job_title": title,
            "job_link": link,
            "company": "OPIS",
            "country": "Romania",
            "city": 'Bucuresti',
            "county": 'Bucuresti'
        })
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "OPIS"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("OPIS", "https://www.opisnet.com/wp-content/uploads/2022/02/OPIS_ADJC_Stacked_White-1.png"))
