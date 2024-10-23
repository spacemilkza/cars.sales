from flask import Flask, render_template, request #import the Flask class

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/") #we create an instance of the class

com_name = "Ntsakos Boutique"
com_type = "Pty Ltd"
com_reg_no = "2017/257825/07"
com_addr = "Danume str, Pretea Glen, JHB, Gauteng, 1818"
com_email = "bvumantsako249@gmail.com"
com_slogan = "is a locally established trendy boutique clothing store located in Tibane."

data={ com_name:com_name, com_addr: com_addr, com_email: com_email, com_reg_no: com_reg_no, com_slogan: com_slogan, com_type: com_type}

@app.route("/")
def index():
    body_type = 'cabriolet', 'coupe', 'crew bus', 'double cab', 'extended cab', 'fast back', 'hatchback', 'king cab', 'LCV', 'minibus', 'MPV', 'sportback', 'station wagon', 'supercab', 'SUV'
    car_inventory = sorted([
        {"title": "Volkswagen Polo Hatch 1.0TSI",
         "power_max": 85,
         "year": 2024,
         "mileage": 3,
         "price": 520400,
         "new": True, 
         "fuel_type": "petrol",
         "transmission": "automatic",
         "banner": "polotsi.jpeg"},
        {"title": "Volkswagen Polo GTi",
         "power_max": 147,
         "year": 2024,
         "mileage": 3,
         "price": 589950,
         "new": True, 
         "fuel_type": "petrol",
         "transmission": "automatic",
         "banner": "pologti.jpeg"},
        {"title": "Toyota Corolla Quest 1.8 Plus",
         "power_max": 103,
         "year": 2024,
         "mileage": 3,
         "price": 335500,
         "new": True, 
         "fuel_type": "petrol",
         "transmission": "automatic",
         "banner": "corollaquest.jpeg"},
        {"title": "Nissan NP200 1.5dCi Safety Pack",
         "power_max": 63,
         "year": 2019,
         "mileage": 127000,
         "price": 199950,
         "new": False, 
         "fuel_type": "diesel",
         "transmission": "manual",
         "banner": "np200.jpeg"},
        {"title": "Renault Kwid 1.0 Dynamique",
         "power_max": 50,
         "year": 2022,
         "mileage": 40000,
         "price": 149950,
         "new": False, 
         "fuel_type": "petrol",
         "transmission": "manual",
         "banner": "kwid.jpeg"}
    ], key= lambda d: d["price"], reverse=False)
    return render_template("index.html", data=data, body_type=body_type, car_inventory=car_inventory)

@app.get("/notifications")
def notifications():
    return render_template("notifications.html", data=data)

@app.get("/signin")
def signin():
    return render_template("signin.html")

@app.route("/account", methods=["GET", "POST"]) #we tie the response function a url
def user_account():
    if request.method == "GET":
        return render_template("signin.html", data=data)
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        return render_template("user_account.html")

@app.route("/apply")
def com_reg():
    return render_template("/apply.html")

@app.route("/create_item")
def create_item():
    return render_template("/create_item.html")

@app.route("/web_development")
def web_dev():
    return render_template("/services/web_dev.html")