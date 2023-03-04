from flask import Flask ,render_template

wep = Flask(__name__)
@wep.route("/")
def homepage():
    return render_template("homepage.html")

@wep.route("/about")
def aboutpage():
    return render_template("about.html")
@wep.route("/Categories")
def aboutpage():
    return render_template("Categories.html")
@wep.route("/Category")
def aboutpage():
    return render_template("Category.html")
@wep.route("/Item")
def aboutpage():
    return render_template("Item.html")

if __name__ =="__main__" :
    wep.run(debug=True,port=9000)
 