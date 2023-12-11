# company: HOGARTH
# API: https://www.hogarth.com/careers?key=&departments=All&location=413#jobs-list


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests



def get_all_jobs():

    jobs_list = []
    response = requests.get('https://www.hogarth.com/jobs_list/json', headers=DEFAULT_HEADERS).json()

    for job in response:
        location = job['field_gh_location']

        if 'Romania' in location:
            jobs_list.append({
                "job_title": job['title'],
                "job_link": f"https://www.hogarth.com/{job['view_node']}",
                "company": "HOGARTH",
                "country": "Romania",
                "city": location.split(',')[0],
            })
    return jobs_list

@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API
    """
    return data_list

company_name = 'HOGARTH'
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo('HOGARTH', 'https://images.crunchbase.com/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/v1458646269/jwjdl0o2yhlivkiwsrai.png'))
