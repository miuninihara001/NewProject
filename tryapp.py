# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import numpy as np 

# Utils
import os
import joblib 
import hashlib
# passlib,bcrypt

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')

import pickle
import warnings

# DB
#from managed_db import *

feature_names_best = ['CustomerID','gender', 'SeniorCitizen', 'partner', 'tenure', 'phoneService', 'multipleLine', 'InternetService','OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']

gender_dict = {"male":1,"female":2}
feature_dict = {"No":1,"Yes":2}


def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 

def get_key(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return key

def get_fvalue(val):
	feature_dict = {"No":1,"Yes":2}
	for key,value in feature_dict.items():
		if val == key:
			return value 
        
        # Load ML Models
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

# ML Interpretation
#import lime
#import lime.lime_tabular

def main():
	"""Churn Prediction App"""
	st.title("Hepatitis Mortality Prediction App")
	#st.markdown(html_temp.format('royalblue'),unsafe_allow_html=True)

	menu = ["Home","Classification","Clustering"]
	#sub_menu = ["Plot","Prediction","Metrics"]

	choice = st.sidebar.selectbox("Menu",menu)
	if choice == "Home":
		st.subheader("Home")
		st.text("What is Hepatitis?")
		#st.markdown(descriptive_message_temp,unsafe_allow_html=True)
		#st.image(load_image('images/hepimage.jpeg'))
        
	elif choice == "Prediction":
					st.subheader("Predictive Analytics")

					CustomerID = st.text_input("CustomerID",".")
					gender = st.radio("Gender",tuple(gender_dict.keys()))
					SeniorCitizen = st.radio("Senior Citizen",tuple(feature_dict.keys()))
					partner = st.radio("Does the Customer Have a Partner in the Network Registered? ",tuple(feature_dict.keys()))
					tenure = st.slider('Number of months the customer has stayed with the company', min_value=0, max_value=72, value=0)
					phoneService = st.radio("Phone Service",tuple(feature_dict.keys()))
					multipleLine = st.selectbox("Multiple Line",tuple(feature_dict.keys()))
					InternetService = st.selectbox("Internet Service",tuple(feature_dict.keys()))
					OnlineSecurity = st.radio("Online Security",tuple(feature_dict.keys()))
					OnlineBackup = st.radio("Online Backup",tuple(feature_dict.keys()))
					DeviceProtection = st.radio("DeviceProtection",tuple(feature_dict.keys()))
					TechSupport = st.radio("Tech Support",tuple(feature_dict.keys()))
					StreamingTV = st.radio("StreamingTV",tuple(feature_dict.keys()))
					StreamingMovies = st.radio("StreamingMovies",tuple(feature_dict.keys()))
					Contract = st.selectbox("Contract",tuple(feature_dict.keys()))
					PaperlessBilling= st.selectbox("Paperless Billing",tuple(feature_dict.keys()))
					PaymentMethod= st.selectbox("Payment Method",tuple(feature_dict.keys()))
					MonthlyCharges= st.selectbox("Monthly Charges",tuple(feature_dict.keys()))
					TotalCharges= st.selectbox("Total Charges",tuple(feature_dict.keys()))
                    
					feature_list = [CustomerID,get_value(gender,gender_dict),get_fvalue(SeniorCitizen),get_fvalue(partner),tenure,get_fvalue(phoneService),get_fvalue(multipleLine,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges)]
					st.write(len(feature_list))
					st.write(feature_list)
					pretty_result = {"CustomerID":CustomerID,'gender':gender, 'SeniorCitizen':SeniorCitizen, 'partner':partner, 'tenure':tenure, 'phoneService':phoneService, 'multipleLine':multipleLine, 'InternetService':InternetService,'OnlineSecurity':OnlineSecurity, 'OnlineBackup':OnlineBackup, 'DeviceProtection':DeviceProtection, 'TechSupport':TechSupport, 'StreamingTV':StreamingTV, 'StreamingMovies':StreamingMovies,'Contract':Contract,'PaperlessBilling':PaperlessBilling,'PaymentMethod':PaymentMethod,'MonthlyCharges':MonthlyCharges,'TotalCharges':TotalCharges}
                                    
                                
					st.json(pretty_result)
					single_sample = np.array(feature_list).reshape(1,-1)
                    
                   
if __name__ == '__main__':
	main()
