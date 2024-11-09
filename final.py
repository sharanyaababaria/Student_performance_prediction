from flask import Flask,render_template,request
import joblib
app=Flask("_name_")

@app.route("/")
def return_home_page():
    return render_template("tem.html")

@app.route("/predict/gets",methods=["POST","GET"])
def return_submissions():
    Gender = request.form['Gender']
    last_to_last_percentage_last_percentage=request.form['last_to_last_percentage_last_percentage']
    average_study_hours=request.form['average_study_hours']
    average_screen_time=request.form['average_screen_time']
    attendance=request.form['attendance']
    participation_out_of_five=request.form['participation_out_of_five']
    extra_curriculur_participation=request.form['extra_curriculur_participation']
    timely_submission_out_of_five=request.form['timely_submission_out_of_five']
    parents_involvment=request.form['parents_involvment']
    time_management_out_of_five=request.form['time_management_out_of_five']
    interest_out_of_five=request.form['interest_out_of_five']

    Gender = float(Gender)
    last_to_last_percentage_last_percentage=float(last_to_last_percentage_last_percentage)
    average_study_hours=float(average_study_hours)
    average_screen_time=float(average_screen_time)
    attendance=float(attendance)
    participation_out_of_five=float(participation_out_of_five)
    extra_curriculur_participation=float(extra_curriculur_participation)
    timely_submission_out_of_five=float(timely_submission_out_of_five)
    parents_involvment=float(parents_involvment)
    time_management_out_of_five=float(time_management_out_of_five)
    interest_out_of_five=float(interest_out_of_five)
    model = joblib.load("mark_prediction_final.model")
    prediction=model.predict([[Gender,last_to_last_percentage_last_percentage,average_study_hours,average_screen_time,attendance,participation_out_of_five,extra_curriculur_participation,timely_submission_out_of_five,parents_involvment,time_management_out_of_five,interest_out_of_five]])
    text1="Prediction is {}".format(prediction[0])
    return render_template("tem.html",text=text1)
    
    



app.run(debug=True)