# company: stripe
# API: https://stripe.com/careers/search


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
import json
from bs4 import BeautifulSoup
from _county import translate_city, get_county

SEARCH_URL = 'https://stripe.com/careers/search'
LISTING_URL = 'https://stripe.com/careers/listing/{slug}/{job_id}'
FALLBACK_CITY = 'Bucharest'


def get_locations(soup):
    """
    Locations live in the __NEXT_DATA__ blob of the search page, as a flat list
    that every listing points into through its locationIndices.
    """
    data_tag = soup.find('script', id='__NEXT_DATA__')
    if data_tag is None:
        return {}, []

    job_index = json.loads(data_tag.string)['props']['pageProps']['jobIndexData']

    return job_index['filters']['locations'], job_index['listings']


def get_romanian_city(locations, listing):
    """
    Picks the Romanian city of a listing.
    Stripe groups locations in a tree (Romania -> Bucharest / Remote in Romania)
    and remote entries such as 'Remote in Romania' carry no city of their own,
    so the capital is used for them.
    """
    cities = []
    for index in listing.get('locationIndices') or []:
        location = locations.get(index)
        if not location or location.get('countryCode') != 'RO':
            continue
        name = location['name']
        if location.get('remote') or name.startswith('Remote in '):
            cities.append(FALLBACK_CITY)
        else:
            cities.append(name)

    if not cities:
        return None

    return translate_city(cities[0])


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from stripe API.
    """

    list_of_jobs = []
    response = requests.get(SEARCH_URL, headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    locations, listings = get_locations(soup)
    locations = {index: location for index, location in enumerate(locations)}

    for listing in listings:
        link = LISTING_URL.format(
            slug=listing['slug'], job_id=listing['greenhouseId'])

        city = get_romanian_city(locations, listing)
        if city is None:
            continue

        list_of_jobs.append({
            "job_title": listing['title'],
            "job_link": link,
            "company": "stripe",
            "country": "Romania",
            "city": city,
            "county": get_county(city)
        })
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
print(update_logo("stripe", "https://b.stripecdn.com/site-srv/assets/img/v3/jobs_v2/thumbnails/stripe-c7f91cf715df9fb9d2198e47de6fc3016a82795e.jpg"))
