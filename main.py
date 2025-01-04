from bs4 import BeautifulSoup
import requests
import time
#To filter out
print("Put some skill you are not familier with.")
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")
def find_jobs():
#Requests information from a specific website
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=%22Data+Science%22&txtKeywords=python%2C%22Data+Science%22%2C&txtLocation=').text
#Creating an instance of soup
    soup = BeautifulSoup(html_text, 'lxml')
#find the class name of the card(class, classname)
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'today' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills =  job.find('div', class_='more-skills-sections').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
               with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More info: {more_info}")

               print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes for next search...')
        time.sleep(time_wait*60)