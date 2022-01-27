from flask import render_template, Blueprint, request, redirect, session, url_for
from joblib import dump, load
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from joblib import dump, load

global y_pred
page = Blueprint("page", __name__, template_folder = "templates", url_prefix="")
@page.route("/", methods=['GET','POST'])
def test1():
	if request.method == 'POST':
		EXT1=request.form.get("optradio1")
		session['EXT1'] = [int(EXT1)]
		print(session['EXT1'])

		EXT2=request.form.get("optradio2")
		session['EXT2'] = [int(EXT2)]
		print(session['EXT2'])

		EXT3=request.form.get("optradio3")
		session['EXT3'] = [int(EXT3)]
		print(session['EXT3'])

		EXT4=request.form.get("optradio4")
		session['EXT4'] = [int(EXT4)]
		print(session['EXT4'])

		EXT5=request.form.get("optradio5")
		session['EXT5'] = [int(EXT5)]
		print(session['EXT5'])

		EXT6=request.form.get("optradio6")
		session['EXT6'] = [int(EXT6)]
		print(session['EXT6'])

		EXT7=request.form.get("optradio7")
		session['EXT7'] = [int(EXT7)]
		print(session['EXT7'])

		EXT8=request.form.get("optradio8")
		session['EXT8'] = [int(EXT8)]
		print(session['EXT8'])

		EXT9=request.form.get("optradio9")
		session['EXT9'] = [int(EXT9)]
		print(session['EXT9'])

		EXT10=request.form.get("optradio10")
		session['EXT10'] = [int(EXT10)]
		print(session['EXT10'])
		return redirect(url_for('page.test2'))
	return render_template('page1.html')
	

@page.route("/test2",methods=['GET','POST'])
def test2():
	if request.method == 'POST':
		EST1=request.form.get("optradio11")
		session['EST1'] = [int(EST1)]
		print(session['EST1'])

		EST2=request.form.get("optradio12")
		session['EST2'] = [int(EST2)]
		print(session['EST2'])

		EST3=request.form.get("optradio13")
		session['EST3'] = [int(EST3)]
		print(session['EST3'])

		EST4=request.form.get("optradio14")
		session['EST4'] = [int(EST4)]
		print(session['EST4'])

		EST5=request.form.get("optradio15")
		session['EST5'] = [int(EST5)]
		print(session['EST5'])

		EST6=request.form.get("optradio16")
		session['EST6'] = [int(EST6)]
		print(session['EST6'])

		EST7=request.form.get("optradio17")
		session['EST7'] = [int(EST7)]
		print(session['EST7'])

		EST8=request.form.get("optradio18")
		session['EST8'] = [int(EST8)]
		print(session['EST8'])

		EST9=request.form.get("optradio19")
		session['EST9'] = [int(EST9)]
		print(session['EST9'])

		EST10=request.form.get("optradio20")
		session['EST10'] = [int(EST10)]
		print(session['EST10'])
		return redirect(url_for('page.test3'))
	return render_template('page2.html')

@page.route("test3",methods=['GET','POST'])
def test3():
	if request.method == 'POST':
		AGR1=request.form.get("optradio21")
		session['AGR1'] = [int(AGR1)]
		print(session['AGR1'])

		AGR2=request.form.get("optradio22")
		session['AGR2'] = [int(AGR2)]
		print(session['AGR2'])

		AGR3=request.form.get("optradio23")
		session['AGR3'] = [int(AGR3)]
		print(session['AGR3'])

		AGR4=request.form.get("optradio24")
		session['AGR4'] = [int(AGR4)]
		print(session['AGR4'])

		AGR5=request.form.get("optradio25")
		session['AGR5'] = [int(AGR5)]
		print(session['AGR5'])

		AGR6=request.form.get("optradio26")
		session['AGR6'] = [int(AGR6)]
		print(session['AGR6'])

		AGR7=request.form.get("optradio27")
		session['AGR7'] = [int(AGR7)]
		print(session['AGR7'])

		AGR8=request.form.get("optradio28")
		session['AGR8'] = [int(AGR8)]
		print(session['AGR8'])

		AGR9=request.form.get("optradio29")
		session['AGR9'] = [int(AGR9)]
		print(session['AGR9'])

		AGR10=request.form.get("optradio30")
		session['AGR10'] = [int(AGR10)]
		print(session['AGR10'])


		return redirect(url_for('page.test4'))
	return render_template('page3.html')

@page.route("test4",methods = ['GET','POST'])
def test4():
	if request.method == 'POST':
		CSN1=request.form.get("optradio31")
		session['CSN1'] = [int(CSN1)]
		print(session['CSN1'])

		CSN2=request.form.get("optradio32")
		session['CSN2'] = [int(CSN2)]

		CSN3=request.form.get("optradio33")
		session['CSN3'] = [int(CSN3)]

		CSN4=request.form.get("optradio34")
		session['CSN4'] = [int(CSN4)]

		CSN5=request.form.get("optradio35")
		session['CSN5'] = [int(CSN5)]

		CSN6=request.form.get("optradio36")
		session['CSN6'] = [int(CSN6)]

		CSN7=request.form.get("optradio37")
		session['CSN7'] = [int(CSN7)]

		CSN8=request.form.get("optradio38")
		session['CSN8'] = [int(CSN8)]

		CSN9=request.form.get("optradio39")
		session['CSN9'] = [int(CSN9)]

		CSN10=request.form.get("optradio40")
		session['CSN10'] = [int(CSN10)]
		print(session['CSN10'])
		
		return redirect(url_for('page.test5'))
	return render_template('page4.html')

@page.route("test5",methods = ['GET','POST'])
def test5():
	#global y_pred
	if request.method == 'POST':
		OPN1=request.form.get("optradio41")
		session['OPN1'] = [int(OPN1)]
		print(session['OPN1'])

		OPN2=request.form.get("optradio42")
		session['OPN2'] = [int(OPN2)]

		OPN3=request.form.get("optradio43")
		session['OPN3'] = [int(OPN3)]

		OPN4=request.form.get("optradio44")
		session['OPN4'] = [int(OPN4)]

		OPN5=request.form.get("optradio45")
		session['OPN5'] = [int(OPN5)]

		OPN6=request.form.get("optradio46")
		session['OPN6'] = [int(OPN6)]

		OPN7=request.form.get("optradio47")
		session['OPN7'] = [int(OPN7)]

		OPN8=request.form.get("optradio48")
		session['OPN8'] = [int(OPN8)]

		OPN9=request.form.get("optradio49")
		session['OPN9'] = [int(OPN9)]

		OPN10=request.form.get("optradio50")
		session['OPN10'] = [int(OPN10)]
		print(session['OPN10'])	
		print(session)
		pred_x = pd.DataFrame.from_dict(session, orient='columns')
		clf = load('xgboost_model1.joblib')
		y_pred = clf.predict(pred_x)
		print(y_pred)
		# print(type(y_pred))
		#session['pred_y'] = str(y_pred[0])
	#	y_pred=request.form.get(str(y_pred[0]))
		if int(y_pred)== 0:
			prediction = 'AGREEABLENESS'
		elif int(y_pred) == 1:
			prediction='CONSCIENTIOUSNESS'
		elif int(y_pred) == 2:
			prediction='NEUROTICISM'
		elif int(y_pred) ==3:
			prediction='EXTRAVERSION'
		else:
			prediction= 'OPENNESS'
		print(prediction)
		return redirect(url_for('page.result',prediction=prediction))
	return render_template('page5.html')



@page.route("result/<prediction>", methods=['GET', 'POST'])
def result(prediction):
	#return redirect(url_for('phome.landing'))
	return render_template('result.html',value =prediction)
