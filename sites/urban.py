# company: Urban Connect
# API: https://urbanconnect.ro/find-a-job/


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup
from _county import get_county, translate_city


def get_jobs():
    """
     ... this func() makes requests
      and collects data from Urban API.
      """

    list_jobs = []
    url = 'https://urbanconnect.ro/find-a-job/'

    try:
        response = requests.get(url, headers=DEFAULT_HEADERS, timeout=20)
        response.raise_for_status()
        html = response.text
    except requests.exceptions.RequestException:
        try:
            response = requests.get(
                f'https://r.jina.ai/{url}',
                headers={**DEFAULT_HEADERS, 'X-Return-Format': 'html'},
                timeout=60,
            )
            response.raise_for_status()
            html = response.text
        except requests.exceptions.RequestException:
            return list_jobs

    soup = BeautifulSoup(html, 'lxml')
    seen_links = set()

    for link_tag in soup.find_all('a', href=True):
        if '/jobsid/' not in link_tag['href']:
            continue

        title_tag = link_tag.find('h2')
        if not title_tag:
            continue

        link = link_tag['href']
        if link in seen_links:
            continue

        card = link_tag.find_parent('div', class_='ct-div-block')
        if not card:
            continue

        location_tag = card.find('div', class_='ct-code-block')
        if not location_tag:
            continue

        location_parts = [part.strip() for part in location_tag.get_text(strip=True).split(',')]
        if len(location_parts) < 2 or location_parts[1] != 'Romania':
            continue

        city = translate_city(location_parts[0])
        county = get_county(city)
        seen_links.add(link)
        list_jobs.append({
            "job_title": title_tag.get_text(strip=True),
            "job_link": link,
            "company": "UrbanSocializing",
            "country": "Romania",
            "city": city,
            "county": county,
        })

    return list_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "UrbanSocializing"
data_list = get_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("UrbanSocializing", 'https://urbanconnect.ro/wp-content/uploads/2024/07/logo_website.png'))
