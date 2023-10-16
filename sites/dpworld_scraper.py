# company DP WORLD
# API: https://ehpv.fa.em2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions?onlyData=true&expand=requisitionList.secondaryLocations,flexFieldsFacet.values&finder=findReqs;siteNumber=CX_1,facetsList=LOCATIONS%3BWORK_LOCATIONS%3BWORKPLACE_TYPES%3BTITLES%3BCATEGORIES%3BORGANIZATIONS%3BPOSTING_DATES%3BFLEX_FIELDS,limit=25,locationId=300000000275207,sortBy=POSTING_DATES_DESC

from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
import uuid

def get_jobs():
    response = requests.get('https://ehpv.fa.em2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions?onlyData=true&expand=requisitionList.secondaryLocations,flexFieldsFacet.values&finder=findReqs;siteNumber=CX_1,facetsList=LOCATIONS%3BWORK_LOCATIONS%3BWORKPLACE_TYPES%3BTITLES%3BCATEGORIES%3BORGANIZATIONS%3BPOSTING_DATES%3BFLEX_FIELDS,limit=25,locationId=300000000275207,sortBy=POSTING_DATES_DESC'
                        , headers = DEFAULT_HEADERS).json()['items'][0]['requisitionList']

    list_of_jobs = []
    for job in response:


        title = job['Title']
        location = job['PrimaryLocation']
        id = job['Id']
        link = f'https://ehpv.fa.em2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/requisitions/preview/{id}/?location=Romania&locationId=300000000275207&locationLevel=country&mode=location'
        list_of_jobs.append({"id": str(uuid.uuid4()),
                        "job_title": title,
                        "job_link":link ,
                        "company": "DPWORLD",
                        "country": "Romania",
                        "city": location})
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """"
    Update data on peviitor API!
    """
    return data_list

company_name = "DPWORLD"
data_list = get_jobs()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('DPWORLD', 'https://strgdpworldweb.z1.web.core.windows.net/DPW%20Logo.png'))









