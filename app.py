import gspread
from flask import Flask, render_template,request
app = Flask(__name__)

gc = gspread.service_account(filename='flask-Udemy.json')
sh = gc.open("ML Team Daily Updates")
shDailyUpdates = sh.get_worksheet(0)
shAutomatedTest = sh.get_worksheet(1)
#shAutomatedTest.append_row(["31/5/23", "Test","SUBIN","Ongoing"])
@app.route('/')
def home():    
    return "Hello World"

@app.route('/index', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        shAutomatedTest.append_row([name, email, message])
        return "Updated Successfully"
    profile = {
        "about": shAutomatedTest.acell('B1').value,
        "interests": shAutomatedTest.acell('B2').value,
        "experience": shAutomatedTest.acell('B3').value,
        "education": shAutomatedTest.acell('B4').value,
    }
    return render_template('index.html', profile=profile)

@app.route('/contact')
def contact():
    return render_template('contact.html')