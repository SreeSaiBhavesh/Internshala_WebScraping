from unicodedata import category
from bs4 import BeautifulSoup
import requests

print('Select the filter methods: ')
print('Enter 1 for Category: ')
print('Enter 2 for location to work: ')
print('Enter 3 for type of job: ')

print('Enter the filter you want to apply: ')
n = int(input())

if n==1:

    print('Enter the category/domain you want to search for: ')
    cat = input()
    html_text = requests.get('https://internshala.com/jobs/internships').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('div', class_= {'container-fluid individual_internship visibilityTrackerItem'})
    a = 0
    for job in jobs:
        
        category = job.find('h3', class_={'heading_4_5 profile'}).a.text
        if cat in category:
            a = 1
            #company = job.find('div', class_='heading_6 company_name')
            company_name = job.find('h4',class_='heading_6 company_name').a.text
            location_work = job.find('a', class_='location_link view_detail_button').text
            position = job.find('h3', class_='heading_4_5 profile').a.text
            du = job.find_all('div', class_='other_detail_item_row')
            
            
                    
            #job_type = job.find('div', class_='label_container label_container_mobile').text
            job_type = job.find('div', class_ = 'status status-small status-inactive').text

            if job_type=='                    Fresher Job                ':
                #pay_scale = job.find('div', class_='item_body').i.text
                print(f"Company Name: {company_name.strip()}")
                print(f"Position: {position.strip()}")
                print(f"Work Location: {location_work.strip()}")
                print(f"Type of Job: {job_type.strip()}")
                #print(f"Salary Details: {pay_scale}")
                #print(f"Application Deadline: {deadline}")
                print('')

            else:
                #pay_scale = job.find('span', class_='stipend').text
               
                        
            
                print(f"Company Name: {company_name.strip()}")
                print(f"Position: {position.strip()}")
                print(f"Work Location: {location_work.strip()}")
                print(f"Type of Job: {job_type.strip()}")
                #print(f"Stipend Details: {pay_scale}")
                #print(f"Duration of Internship: {duration}")
                #print(f"Application Deadline: {deadline.strip()}")
                print('')
        
    if a==0:
        print("No results Found")

elif n==2:

    print('Enter the location from where you want to work: ')
    loc = input()
    html_text = requests.get('https://internshala.com/jobs/internships').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('div', class_= {'container-fluid individual_internship visibilityTrackerItem'})
    
    a = 0
    for job in jobs:
        location_work = job.find('a', class_='location_link view_detail_button').text
        if loc in location_work:
            a = 1
            #company = job.find('div', class_='heading_6 company_name')
            company_name = job.find('h4',class_='heading_6 company_name').a.text
            position = job.find('h3', class_='heading_4_5 profile').a.text
            #deadline = job.find('div', class_='item_body').text
            location_work = job.find('a', class_='location_link view_detail_button').text
            #job_type = job.find('div', class_='label_container label_container_mobile').text
            job_type = job.find('div', class_ = 'status status-small status-inactive').text

            print(f"Company Name: {company_name.strip()}")
            print(f"Position: {position.strip()}")
            print(f"Work Location: {location_work.strip()}")
            print(f"Type of Job: {job_type.strip()}")
            print('')

            # if job_type== '                    Fresher Job                ':
             #   print('yes')
                #pay_scale = job.find('div', class_='item_body').text
              #  print(f"Company Name: {company_name.strip()}")
               # print(f"Position: {position.strip()}")
                #print(f"Work Location: {location_work.strip()}")
               # print(f"Type of Job: {job_type.strip()}")
               #print(f"Salary Details: {pay_scale}")
                #print(f"Application Deadline: {deadline}")
                #print('')

            #else:
             #   print('no')
                #pay_scale = job.find('span', class_='stipend').text
                #duration = job.find('div', class_='item-body').text
              #  print(f"Company Name: {company_name.strip()}")
               # print(f"Position: {position.strip()}")
               # print(f"Work Location: {location_work.strip()}")
               # print(f"Type of Job: {job_type.strip()}")
                #print(f"Stipend Details: {pay_scale}")
                #print(f"Duration of Internship: {duration}")
                #print(f"Application Deadline: {deadline}")
                #print('') 

    if a==0:
        print("No Results Found")

elif n==3:
    
    print('Select one from both (Internship or Fresher Job): ')
    print('Enter 1 for Fresher Jobs')
    print('Enter 2 for Internships')

    n = int(input())

    if n==1:

        html_text = requests.get('https://internshala.com/fresher-jobs/').text
        soup = BeautifulSoup(html_text,'lxml')
        jobs = soup.find_all('div', class_= {'container-fluid individual_internship visibilityTrackerItem'})

        for job in jobs:
            #company = job.find('div', class_='heading_6 company_name')
            company_name = job.find('div',class_='company_and_premium').a.text
            position = job.find('h3', class_='heading_4_5 profile').a.text
            #deadline = job.find('div', class_='item_body').text
            location_work = job.find('a', class_='location_link view_detail_button').text
            #job_type = job.find('div', class_='label_container label_container_mobile').text
            job_type = job.find('div', class_ = 'status status-small status-inactive').text
            #pay_scale = job.find('div', class_='item_body').i.text

            print(f"Company Name: {company_name.strip()}")
            print(f"Position: {position.strip()}")
            print(f"Work Location: {location_work.strip()}")
            print(f"Type of Job: {job_type.strip()}")
            #print(f"Stipend Details: {pay_scale}")
            #print(f"Application Deadline: {deadline}")
            print('')
    else:

        
        html_text = requests.get('https://internshala.com/internships/').text
        soup = BeautifulSoup(html_text,'lxml')
        jobs = soup.find_all('div', class_= {'container-fluid individual_internship visibilityTrackerItem'})

        for job in jobs:

            #company = job.find('div', class_='heading_6 company_name')
            company_name = job.find('div',class_='company_and_premium').a.text
            position = job.find('h3', class_='heading_4_5 profile').a.text
            #deadline = job.find('div', class_='item_body').text
            location_work = job.find('a', class_='location_link view_detail_button').text
            #job_type = job.find('div', class_='label_container label_container_mobile').text
            job_type = job.find('div', class_ = 'status status-small status-inactive').text
            pay_scale = job.find('span', class_='stipend').text
            #duration = job.find('div', class_='item_body').text

            print(f"Company Name: {company_name.strip()}")
            print(f"Position: {position.strip()}")
            print(f"Work Location: {location_work.strip()}")
            print(f"Type of Job: {job_type.strip()}")
            print(f"Stipend Details: {pay_scale}")
            #print(f"Duration of Internship: {duration}")
            #print(f"Application Deadline: {deadline}")
            print('')    

else:
    print("Enter number 1 or 2 or 3")    