{\rtf1\ansi\ansicpg936\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, render_template, request, redirect\
from flask_sqlalchemy import SQLAlchemy\
from datetime import datetime\
\
app = Flask(__name__)\
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///greenhill.db'\
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False\
db = SQLAlchemy(app)\
\
# \uc0\u25968 \u25454 \u24211 \u27169 \u22411 \
class Member(db.Model):\
    id = db.Column(db.Integer, primary_key=True)\
    member_no = db.Column(db.String(20), unique=True, nullable=False)\
    name = db.Column(db.String(100), nullable=False)\
    phone = db.Column(db.String(20))\
    is_active = db.Column(db.Boolean, default=True)\
\
class Product(db.Model):\
    id = db.Column(db.Integer, primary_key=True)\
    name = db.Column(db.String(100), nullable=False)\
    price = db.Column(db.Float, nullable=False)\
    sales_mode = db.Column(db.String(10), nullable=False)\
    bay_location = db.Column(db.String(10))\
    is_active = db.Column(db.Boolean, default=True)\
\
class Round(db.Model):\
    id = db.Column(db.Integer, primary_key=True)\
    round_no = db.Column(db.Integer, unique=True)\
    status = db.Column(db.String(20), default='open')\
\
class Order(db.Model):\
    id = db.Column(db.Integer, primary_key=True)\
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))\
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'))\
    crate_no = db.Column(db.Integer)\
    total = db.Column(db.Float, default=0)\
\
# \uc0\u39318 \u39029 -\u21327 \u35843 \u21592 \u20202 \u34920 \u26495 \
@app.route('/')\
def dashboard():\
    rounds = Round.query.all()\
    members = Member.query.filter_by(is_active=True).all()\
    products = Product.query.filter_by(is_active=True).all()\
    return render_template('dashboard.html', rounds=rounds, members=members, products=products)\
\
# \uc0\u20250 \u21592 \u31649 \u29702 \
@app.route('/members')\
def members():\
    member_list = Member.query.all()\
    return render_template('members.html', members=member_list)\
\
@app.route('/members/add', methods=['POST'])\
def add_member():\
    m = Member(\
        member_no=request.form['member_no'],\
        name=request.form['name'],\
        phone=request.form['phone']\
    )\
    db.session.add(m)\
    db.session.commit()\
    return redirect('/members')\
\
# \uc0\u20135 \u21697 \u31649 \u29702 \
@app.route('/products')\
def products():\
    product_list = Product.query.all()\
    return render_template('products.html', products=product_list)\
\
@app.route('/products/add', methods=['POST'])\
def add_product():\
    p = Product(\
        name=request.form['name'],\
        price=float(request.form['price']),\
        sales_mode=request.form['sales_mode'],\
        bay_location=request.form['bay_location']\
    )\
    db.session.add(p)\
    db.session.commit()\
    return redirect('/products')\
\
if __name__ == '__main__':\
    with app.app_context():\
        db.create_all()\
    app.run(debug=True)\
}