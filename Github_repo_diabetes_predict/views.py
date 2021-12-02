from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from models import User
from index import db
import pickle
import numpy as np
from mail import send_mail


views = Blueprint("views", __name__)



#my url starts
filename = 'diabetes-prediction-model5.pkl'
classifier = pickle.load(open(filename, 'rb'))

@views.route("/",methods=['GET', 'POST'])
@views.route("/index",methods=['GET', 'POST'])
@views.route("/home/")
@login_required
def home():
    return render_template('index.html')

@views.route("/exercise/")
@login_required
def exercise():
    return render_template('exercise.html',title='exercise')#exercise_bmi_doctor


@views.route("/contact/",methods=['GET','POST'])
@login_required
def contact():
    if request.method=="POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        flag=send_mail(email,message,name,phone)
        return  render_template('contact.html',success=flag)
    return render_template('contact.html')
    
@views.route("/input")
@login_required
def input():
    return render_template('input.html')

@views.route("/bmi")
@login_required
def bmi():
    return render_template('bmi.html')

@views.route('/predict', methods=['POST','GET'])
@login_required
def predict():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    my_prediction = classifier.predict(final_features)
    return render_template('predict.html', prediction = my_prediction)

#my url ends
