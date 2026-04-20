#company: EA Sports
# API: https://jobs.ea.com/en_US/careers/Home/?4538=8382&4538_format=3021&listFilterMode=1


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup
from _county import get_county, translate_city


def get_soup(url):
    response = requests.get(url, headers=DEFAULT_HEADERS)
    return BeautifulSoup(response.text, 'lxml')


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from EA Sports careers page.
    """

    list_of_jobs = []
    city = translate_city('Bucharest')
    county = get_county(city)
    seen_links = set()

    for offset in range(0, 1000, 20):
        if offset == 0:
            url = 'https://jobs.ea.com/en_US/careers/Home/?4538=8382&4538_format=3021&listFilterMode=1'
        else:
            url = f'https://jobs.ea.com/en_US/careers/Home/?4538=8382&4538_format=3021&listFilterMode=1&jobRecordsPerPage=20&jobOffset={offset}'

        soup = get_soup(url)
        jobs = soup.find_all('article', class_='article--result')
        if not jobs:
            break

        page_links = []
        for job in jobs:
            link_tag = job.find('a', href=True)
            if link_tag:
                page_links.append(link_tag['href'])

        if not page_links:
            break

        for job in jobs:
            title_tag = job.find('h3')
            link_tag = job.find('a', href=True)
            if not title_tag or not link_tag:
                continue

            title = title_tag.get_text(strip=True)
            link = link_tag['href']
            if link in seen_links:
                continue

            job_text = job.get_text(' | ', strip=True)
            if 'Bucharest, Romania' not in job_text:
                continue

            seen_links.add(link)
            list_of_jobs.append({
                "job_title": title,
                "company": "easports",
                "job_link": link,
                "country": "Romania",
                "city": city,
                "county": county,
            })

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
