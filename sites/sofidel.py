# company SOFIDEL
# API: https://careers.sofidel.com/search/?createNewAlert=false&q=&locationsearch=&optionsFacetsDD_customfield2=Romania&optionsFacetsDD_city=&optionsFacetsDD_customfield1=


from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup
import uuid

def get_all_jobs():

    response = requests.get('https://careers.sofidel.com/search/?createNewAlert=false&q=&locationsearch=&optionsFacetsDD_customfield2=Romania&optionsFacetsDD_city=&optionsFacetsDD_customfield1=',
                            headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')


    list_of_jobs = []
    jobs = soup.find_all('tr', class_ = 'data-row')
    for job in jobs:
        link = ('https://careers.sofidel.com'+job.find('a', class_ = 'jobTitle-link')['href'])
        title = job.find('a', class_ = 'jobTitle-link').text.strip()
        location = job.find('span', class_ = 'jobLocation').text.split(',')[0].strip()
        list_of_jobs.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "SOFIDEL",
            "country": "Romania",
            "city": location})
    return list_of_jobs


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list

company_name ='SOFIDEL'
data_list = get_all_jobs()
scrape_and_update_peviitor(company_name, data_list)
print(update_logo('SOFIDEL', '//rmkcdn.successfactors.com/398b80ae/84fafa7f-bd2a-47b6-980f-e.jpg'))
