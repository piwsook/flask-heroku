from flask import Flask, render_template, request, jsonify
import smtplib

app = Flask(__name__)
data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]



subscribers = []

@app.route('/')
def index():
    title = "JuAm's Portfolio"
    return render_template('index.html', titel=title)

@app.route('/about')
def about():
    title = "About JuAm coffee cafe"
    names = ["Product and Service < Youtube Channel >",
             "Product and Service < Life Insurance >"
                , "Product and Service < Coffee and Tea >"]
    return render_template('about.html', names=names,
                           title=title)

@app.route('/youtube')
def youtube():
    title = ""
    names = [""]
    return render_template('youtube.html', names=names, title=title)

@app.route('/life')
def life():
    title = ""
    names = [""]
    return render_template('life.html', names=names, title=title)

@app.route('/coffee')
def coffee():
    title = ""
    names = [""]
    return render_template('coffee.html', names=names, title=title)

@app.route('/contact')
def contact():
    title = ""
    names = [""]
    return render_template('contact.html', names=names, title=title)

@app.route('/inbox')
def subscribe():
    title = "Inbox Message"
    return render_template('subscribe.html', title=title)

@app.route('/form', methods=["POST"])
def form():
    try :
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        message_box = request.form.get('message_box')

        message = (f"{first_name} | {last_name} | {email} | {message_box}")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("piwsook@gmail.com", "Khanchu69")
        server.sendmail("piwsook@gmail.com", email, message,)
    except :
        error_statement = "All Form Fields Required..."
        render_template("subscribe.html",
                           error_statement =error_statement,
                           first_name = first_name,
                           last_name = last_name,
                           email = email,
                           message_box = message_box, )

    if  first_name == '' or last_name == '' or email == '' or message_box == '':
        error_statement = "All Form Fields Required..."
        return render_template("subscribe.html",
            error_statement = error_statement,
            first_name = first_name,
            last_name = last_name,
            email = email,
            message_box = message_box,)


    #subscribers.append(f'{first_name} {last_name} | {email} | {message_box}')
    title = "Thank You!"
    return render_template('form.html', title=title, subscribers=subscribers)

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)








