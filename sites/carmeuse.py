#company: Carmeuse
# API: https://ekiz.fa.em2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/requisitions?location=Romania&locationId=300000000306206&locationLevel=country&mode=job-location



from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests


def get_all_jobs():
    """
    this func() makes requests
    and collects data from Carmeuse API.
    """

    response = requests.get('https://ekiz.fa.em2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions?onlyData=true&expand=requisitionList.secondaryLocations,flexFieldsFacet.values&finder=findReqs;siteNumber=CX,facetsList=LOCATIONS%3BWORK_LOCATIONS%3BWORKPLACE_TYPES%3BTITLES%3BCATEGORIES%3BORGANIZATIONS%3BPOSTING_DATES%3BFLEX_FIELDS,limit=25,locationId=300000000306206,sortBy=POSTING_DATES_DESC',
                            headers=DEFAULT_HEADERS).json()['items'][0]['requisitionList']


    list_of_jobs = []
    for job in response:

        title = job['Title']
        location = job['PrimaryLocation']
        id = job['Id']
        link = f'https://ekiz.fa.em2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/requisitions/preview/{id}/?location=Romania&locationId=300000000306206&locationLevel=country&mode=job-location'

        if 'Brașov' in location:
            location = 'Brasov'
        elif 'Chişcădaga' in location:
            location = 'Chiscadaga'
        elif 'Valea Mare-Pravăţ' in location:
            location = 'Valea Mare-Pravat'

        list_of_jobs.append({
                    "job_title": title,
                    "company": "carmeuse",
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


company_name = "carmeuse"
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo("carmeuse", "https://www.carmeuse.com/themes/custom/carmeuse_theme/images/logo.svg"))
