import requests
from bs4 import BeautifulSoup
import sqlite3


conn = sqlite3.connect('jobs.db')
c = conn.cursor()
c.execute('''CREATE TABLE jobs (title text, link text)''')

for page in range(1, 5):
    url = "https://github.com/awesome-jobs/vietnam/issues?page={}&q=is%3Aissue+is%3Aopen".format(
        page)
    ses = requests.session()
    resp = ses.get(url).text
    soup = BeautifulSoup(resp, 'html.parser')

    gdp_title = soup.find_all("a", attrs={"data-hovercard-type": "issue"})

    titles_job = [title.text for title in gdp_title]

    links_job = []

    for title in gdp_title:
        links = "https://github.com/"+title.get('href')
        links_job.append(links)

    jobs_if = list(zip(titles_job, links_job))

    for job in jobs_if:
        conn.execute("INSERT INTO jobs VALUES (? , ?)", job)
    conn.commit()



