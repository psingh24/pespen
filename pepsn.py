from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
    'author': 'X-factor', 
    'title': "How Westbrook's triple doubles are not meaningful.",
    'content': "Coming soon...",
    'date': "04/20/2019"
    },
    {
    'author': 'Jassi A. Smith', 
    'title': "THIS MAN IS A BONAFIDE SCRUB!",
    'content': "Coming soon...",
    'date': "04/22/2019"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/login")
def login():
    return render_template('login.html', title='Login')

@app.route("/register")
def register():
    return render_template('register.html', title='Register')

@app.route("/picks")
def picks():
    return render_template('picks.html', title='Picks')

@app.route("/standings")
def standings():
    return render_template('standings.html', title='Standings')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/discussion")
def discussion():
    return render_template('discussion.html', title='Discussion', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
