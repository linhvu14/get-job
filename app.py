
# importing modules
from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect('jobs.db')
c = conn.cursor()


# declaring app name
app = Flask(__name__)


job_list = []
link_list = []
for row in c.execute('SELECT * FROM jobs'):
    job_list.append(row[0])
    link_list.append(row[1])

# defining home page


@app.route('/')
def homepage():

    # returning index.html and list
    # and length of list to html page
    return render_template("home.html", len=len(job_list), job_list=job_list, link_list=link_list)
    # if __name__ == '__main__':

    # running app
    app.run(use_reloader=True, debug=True)
