# company: Uni Systems
# API: https://apply.workable.com/uni-systems/#jobs


from A_OO_get_post_soup_update_dec import update_peviitor_api
from L_00_logo import update_logo
import requests
import re


def get_cookies():

    response = requests.head(url='https://apply.workable.com/uni-systems/#jobs').headers

    wmc = re.search(r"wmc=([^;]+);", str(response)).group(0)
    __cf_bm = re.search(r"__cf_bm=([^;]+);", str(response)).group(0)

    return wmc, __cf_bm


def get_all_jobs():
    """
    ... this func() makes requests
    and collects data from Uni Systems API.
    """
    url = "https://apply.workable.com/api/v3/accounts/uni-systems/jobs"

    cookies = get_cookies()

    payload = {
        "query": "",
        "location": [
            {
                "country": "Romania",
                "region": "Bucharest",
                "city": "Bucharest",
                "countryCode": "RO"
            }
        ],
        "department": [],
        "worktype": [],
        "remote": [],
        "workplace": []
    }
    headers = {
        "cookie": f"{cookies[0]}{cookies[1]}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    response = requests.request("POST", url, json=payload, headers=headers).json()['results']


    list_of_jobs = []
    for job in response:
        title = job['title']
        location = job['location']['city'].split(',')[0]
        id = job['shortcode']
        link = f'https://apply.workable.com/uni-systems/j/{id}'
        list_of_jobs.append({
            "job_title": title,
            "company": "uni.systems",
            "job_link": link,
            "country": "Romania",
            "city": location
            })
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


company_name = "uni.systems"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("uni.systems", "https://workablehr.s3.amazonaws.com/uploads/account/logo/492828/logo"))