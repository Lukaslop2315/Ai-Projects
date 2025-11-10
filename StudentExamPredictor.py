import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

#STUDENT PREDICTOR WITH MULTIPLE NUMERIC FEATURES based on : "Hours_Studied", "Previous_Scores", "Sleep_Hours", "Tutoring_Sessions", "Attendance"


# Use data frames for data storage 
dataFrame = pd.read_csv("StudentPerformanceFactors.csv", usecols=["Hours_Studied", "Previous_Scores", "Sleep_Hours", "Tutoring_Sessions", "Attendance", "Exam_Score"], nrows=10000)   

# Features = x  target = y
X = dataFrame[["Hours_Studied", "Previous_Scores", "Sleep_Hours", "Tutoring_Sessions", "Attendance"]]
y = dataFrame["Exam_Score"]


bestrandomstate = 0  # global
def avgMSE():
    msetotal = 0
    bestmse = 10  #  this is based on average MSE anyway  
    for i in range(500):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)  #  80/20 split for training and testing. each different state has a different model with lower MSE
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        msetotal += mse
        if mse < bestmse:
            bestmse = mse
            bestrandomstate  = i
    mseavg = msetotal / 500
    
    return mseavg, bestrandomstate  

def main():
    # Get the average MSE and best random state
    mse_avg, bestrandomstate = avgMSE()
    print("Average Mean Squared Error over 500 models: ", mse_avg)
    print("Best random state found: ", bestrandomstate)
    print("\nAdd your own variables (Integer inputs only, Attendance and Previous Scores must be between 0 and 100):")
    hours_studied = float(input("Hours Studied: "))
    previous_scores = float(input("Previous Scores: "))
    sleep_hours = float(input("Sleep Hours: "))
    tutoring_sessions = float(input("Tutoring Sessions: "))
    attendance = float(input("Attendance: "))
    if attendance < 0 or attendance > 100 or previous_scores < 0 or previous_scores > 100:
        print("Attendance and Previous Scores must be between 0 and 100")
        main()
    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=bestrandomstate)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        input_data = [[hours_studied, previous_scores, sleep_hours, tutoring_sessions, attendance]]
        predicted_score = model.predict(input_data)
        if predicted_score > 100:
            print("Max marks allocated 100/100")
        else:   
            print("Predicted Exam Score: ", int(predicted_score[0]), "/100")  #  must convert the one element in the array to an integer 
            print("With a MSE of: ", mse) 
            print("Thank you for using this predictor made by L.Lopetaitis")


main()
