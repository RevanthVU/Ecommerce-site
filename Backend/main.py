from flask import Flask,redirect,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import login_required,logout_user,login_user,LoginManager,login_manager,current_user
from flask.globals import request 
from werkzeug.security import generate_password_hash,check_password_hash
import MySQLdb
import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     username="root",
#     password="********"
# )
# mycursor=mydb.cursor()

# mydatabase connection
local_server=True
app=Flask(__name__)
app.secret_key="*******"


# This is for getting the unique user access

login_manager=LoginManager(app)
login_manager.login_view='login'




# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databasename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/online_retail'
db=SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return adminregister.query.get(int(user_id))

# class Test(db.Model):
#     admin_id=db.Column(db.Integer,primary_key=True)
#     username=db.Column(db.String(50))
#     password=db.Column(db.String(50))

class adminregister(UserMixin,db.Model):
    admin_id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(40))
    password=db.Column(db.String(1000))

class distributorregister(UserMixin,db.Model):
    Distributor_name=db.Column(db.String(40))
    Distributor_Type=db.Column(db.String(40))
    Distributor_Location=db.Column(db.String(20))
    Distributor_id=db.Column(db.Integer,primary_key=True)

class storeregister(UserMixin,db.Model):
    Branch_name=db.Column(db.String(40))
    City=db.Column(db.String(40))
    Region=db.Column(db.String(20))
    State=db.Column(db.String(20))
    Pincode=db.Column(db.String(10))
    Branch_id=db.Column(db.Integer,primary_key=True)

class user_register(UserMixin,db.Model):
    UserID=db.Column(db.Integer,primary_key=True)
    Email_id=db.Column(db.String(50))
    Username=db.Column(db.String(50))
    Password=db.Column(db.String(1000))
    Contact=db.Column(db.String(20))

@app.route("/")
def home():
    return render_template("index.html")



# @app.route("/AdminLogin")
# def AdminLogin():
#     return render_template("AdminLogin.html")



@app.route("/Allthingstobuy")
def Allthingstobuy():
    return render_template("Allthingstobuy.html")





@app.route("/AdminDetails")
def ADetails():
    return render_template("AdminDetails.html")

@app.route("/StoreDetails")
def SDetails():
    return render_template("StoreDetails.html")

@app.route("/DistributorDetails")
def DDetails():
    return render_template("DistributorDetails.html")

@app.route("/Products")
def Products():
    return render_template("products.html")

@app.route("/ProductDetails")
def Pdetails():




    return render_template("Productdetails.html",page_heading='Men faviorate wear')

@app.route("/Cart")
def Cart():
    return render_template("Cart.html")

@app.route("/Account")
def Account():
    return render_template("Account.html")

@app.route("/CheckingWebsite")
def CheckingWeb():
    return render_template("CheckingWebsites.html")


@app.route('/AdminLogin',methods=['POST', 'GET'])
def Alogin():
    if request.method=="POST":
        admin_id=request.form.get('admin_id')
        username=request.form.get('username')
        password=request.form.get('password')
        print(admin_id,username,password)
        user=adminregister.query.filter_by(admin_id=admin_id).first()
        if user and check_password_hash(user.password,password):
            
            return 'Login success'
        else:
            flash("Invalid Credentials","danger")
            return render_template("AdminLogin.html")

    return render_template("AdminLogin.html")

@app.route('/Adminsignup',methods=['POST', 'GET'])
def Asignup():
    if request.method=="POST":
        admin_id=request.form.get('admin_id')
        username=request.form.get('username')
        password=request.form.get('password')
        # print(admin_id,username,password)
        encpassword=generate_password_hash(password)
        new_user=db.engine.execute(f"INSERT INTO `adminregister` (`admin_id`,`username`,`password`) VALUES ({admin_id},'{username}','{encpassword}') ")
        if new_user:
            return 'USER ADDED'

    return render_template("Adminsignup.html")


@app.route("/DistributorLogin", methods=['POST','GET'])
def DistributorLogin():
    if request.method=="POST":
        Distributor_name=request.form.get('Distributor_name')
        Distributor_Type=request.form.get('Distributor_Type')
        Distributor_Location=request.form.get('Distributor_Location')
        user=distributorregister.query.filter_by(Distributor_name=Distributor_name).first()
        if user:
            return 'Login success'
        else:
            flash("Invalid Credentials","danger")
            return render_template("DistributorLogin.html")
    return render_template("DistributorLogin.html")

@app.route("/Distributorsignup",methods=['POST', 'GET'])
def Distributorsignup():
    if request.method=="POST":
        Distributor_name=str(request.form.get('Distributor_name'))
        Distributor_Type=str(request.form.get('Distributor_Type'))
        Distributor_Location=str(request.form.get('Distributor_Location'))
        new_user=db.engine.execute(f"INSERT INTO `distributorregister` (`Distributor_name`,`Distributor_Type`,`Distributor_Location`) VALUES ('{str(Distributor_name)}','{str(Distributor_Type)}','{str(Distributor_Location)}') ")
       
        if new_user:
            return 'USER ADDED'
    return render_template("Distributorsignup.html")


@app.route("/StoreLogin",methods=['POST', 'GET'])
def StoreLogin():
    if request.method=="POST":
        Branch_name=request.form.get('Branch_name')
        City=request.form.get('City')
        Region=request.form.get('Region')
        State=request.form.get('State')
        Pincode=request.form.get('Pincode')
        user=storeregister.query.filter_by(Branch_name=Branch_name).first()
        if user:
            return 'Login success'
        else:
            flash("Invalid Credentials","danger")
            return render_template("StoreLogin.html")
    return render_template("StoreLogin.html")


@app.route("/Storesignup", methods=['POST', 'GET'])
def Ssignup():
    if request.method=="POST":
        Branch_name=str(request.form.get('Branch_name'))
        City=str(request.form.get('City'))
        Region=str(request.form.get('Region'))
        State=str(request.form.get('State'))
        Pincode=str(request.form.get('Pincode'))
        new_user=db.engine.execute(f"INSERT INTO `storeregister` (`Branch_name`,`City`,`Region`,`State`,`Pincode`) VALUES ('{str(Branch_name)}','{str(City)}','{str(Region)}','{str(State)}','{str(Pincode)}') ")
        if new_user:
            return 'USER ADDED'
    return render_template("Storesignup.html")


@app.route("/FreeuserLogin" , methods=['POST','GET'])
def FLogin():
    if request.method=="POST":
        Email_id=str(request.form.get('Email_id'))
        Username=str(request.form.get("Username"))
        Password=str(request.form.get("Password"))
        user=user_register.query.filter_by(Email_id=Email_id).first()
        if user and check_password_hash(user.Password,Password):
            return render_template('Allthingstobuy.html')
        else:
            flash("Invalid Credentials","danger")
            return render_template("FreeuserLogin.html")
    
    return render_template("FreeuserLogin.html")


@app.route("/FreeuserSignup",methods=['POST','GET'])
def FSignup():
    if request.method=="POST":
        Email_id=str(request.form.get('Email_id'))
        Username=str(request.form.get("Username"))
        Password=str(request.form.get("Password"))
        Contact=str(request.form.get("Contact"))
        encpassword=generate_password_hash(Password)
        new_user=db.engine.execute(f"INSERT INTO `user_register` (`Email_id`,`Username`,`Password`,`Contact`) VALUES ('{str(Email_id)}','{str(Username)}','{encpassword}','{str(Contact)}') ")
        if new_user:
            return 'USER ADDED'
    return render_template("FreeuserSignup.html")







@app.route("/testwhetheritisconnectedornot")
def test():
    try:
        a=adminregister.query.all()
        print(a)
        return f'MY DATABASE IS CONNECTED'
    except Exception as e:
        print(e)
        return f"NOT CONNECTED {e}"


app.run(debug=True)
