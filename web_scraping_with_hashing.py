from bs4 import BeautifulSoup
import requests
import re
import docx
from hash_function import hashing


url = 'https://aws.amazon.com/new/?whats-new-content-all'

response = requests.get(url)
# print(response)



soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h5", {"class": "lb-txt-bold lb-txt-uppercase lb-txt-white lb-none-v-margin lb-h5 lb-title"})
info = soup.find_all("div", {"class": "lb-txt-normal lb-txt-white lb-rtxt"})
dates = soup.find_all("div", {"class": "lb-tiny-align-right lb-txt-bold lb-txt-none lb-txt-white lb-txt"})

titles_string_list = [str(title) for title in titles]
info_string_list = [str(inf) for inf in info]
dates_string_list = [str(date) for date in dates]

regex_title = ">\s.*<"

filtered_titles_list = []

for text in titles_string_list:
    match = re.findall(regex_title, text)
    match = match[0]
    # match = match[2:-1]
    match = match.strip('>')
    match = match.strip('<')
    match = match.strip(' ')
    filtered_titles_list.append(match)



regex_info = ">.*\."

filtered_info_list = []

for text in info_string_list:
    match = re.findall(regex_info, text)
    match = match[0]
    # match = match[1:-1]
    match = match.strip('>')
    match = match.strip('<')
    filtered_info_list.append(match)



regex_date = "\s[A-Z].*\\n"

filtered_dates_list = []


for text in dates_string_list:
    match = re.findall(regex_date, text)
    match = match[0]
    match = match.strip('\n')
    match = match.strip(' ')
    # match = match[1:-2]
    filtered_dates_list.append(match)


all_in_one = [(filtered_titles_list[i],filtered_info_list[i],filtered_dates_list[i]) for i in range(len(filtered_dates_list))]
hashed_objects = []


for el in all_in_one:
    title = el[0]
    text = el[1]
    date = el[2]

    hash_value = hashing(title,text,date)
    hashed_objects.append(hash_value)


filtered_hashed_objects = []

for i in range(len(hashed_objects)):
    if hashed_objects[i] not in filtered_hashed_objects:
        filtered_hashed_objects.append(hashed_objects[i])
    else:
        filtered_titles_list.pop(i)
        filtered_info_list.pop(i)
        filtered_dates_list.pop(i)

mydoc = docx.Document()

for i in range(len(filtered_dates_list)):
    print(f"Title: {filtered_titles_list[i]}")
    mydoc.add_heading(filtered_titles_list[i])
    print(f"Text: {filtered_info_list[i]}")
    mydoc.add_paragraph(filtered_info_list[i])
    print(f"Date: {filtered_dates_list[i]}")
    mydoc.add_paragraph(filtered_dates_list[i])
    print(f"Hash value: {filtered_hashed_objects[i]}")
    print()
    mydoc.add_paragraph(f"")

try:
    mydoc.save("D:/my_written_file.docx")
except:
    print('!!!Затвори word файла за да може да бъде ъпдейтнат'.upper())