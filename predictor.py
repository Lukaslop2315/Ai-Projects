import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.linear_model import LinearRegression

# Simple Linear regression with ONE feature input.

def load_data():
    try:
        data = pd.read_csv("StudentPerformanceFactors.csv")
        hours_studied = data["Hours_Studied"].tolist()
        exam_score = data["Exam_Score"].tolist()
        return hours_studied, exam_score
    except Exception as e:
        print(f"Error loading data: {e}")
        

def printHourscolumns():
    try:
        data = pd.read_csv("StudentPerformanceFactors.csv")
        columns = ["Hours_Studied"]
        print(data[columns].head(6500))
    except FileNotFoundError:
        print("StudentPerformanceFactors.csv not in directory")

def printExamScorecolumns():
    try:
        data = pd.read_csv("StudentPerformanceFactors.csv")
        columns = ["Exam_Score"]
        print(data[columns].head(6500))
    except FileNotFoundError:
        print("StudentPerformanceFactors.csv not in directory")

def printGraphWithoutLinearRegression(hours_studied, exam_score):
    plt.scatter(hours_studied, exam_score)
    plt.xlabel("Hours_Studied")
    plt.ylabel("Exam_Score")
    plt.show()

def printGraphWithLinearRegression(hours_studied, exam_score, x, y):
    plt.scatter(hours_studied, exam_score, color="blue", label="Data Points")
    plt.plot(x, y, color="red", label="Regression Line")
    plt.xlabel("Hours Studied")
    plt.ylabel("Exam Score")
    plt.title("Hours Studied vs Exam Score")
    plt.legend()
    plt.show()

def main():
    print("---Single Feature Linear Regression (Really Basic)---")
    print("Database used off Kaggle -https://www.kaggle.com/datasets/lainguyn123/student-performance-factors")
    print("Hours Studied vs Exam Score")
    print("1. See graph without linear regression")
    print("2. See graph with linear regression")
    print("3.See Line formula")
    print("4. See the Accuracy with MSE")
    print("5.Test the predictor")
    print("6 How many hours to score 100%?")
    print("7. Exit")
    hours_studied, exam_score = load_data()
    hours_studied_2D = np.array(hours_studied).reshape(-1, 1)
    exam_score_2D = np.array(exam_score).reshape(-1, 1)  
    predictor = LinearRegression()
    predictor.fit(hours_studied_2D, exam_score_2D)  
    m = predictor.coef_  #Use Gradient descent to prove
    b = predictor.intercept_  # Intercept //0 hours studeied  = 61 exam score which is unrealistic. 
    x = np.linspace(0, 45, 5000).reshape(-1, 1)  
    y = predictor.predict(x)
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            printGraphWithoutLinearRegression(hours_studied, exam_score)
        elif choice == "2":
            printGraphWithLinearRegression(hours_studied, exam_score, x, y) 
        elif choice == "3":
            print( "ŷ = " + str(m) + "x + " + str(b))    # ŷ = mx + b simple linear regression 
        elif choice == "4":
            sum_errors = 0
            for i in range(len(hours_studied)):
                actual = exam_score_2D[i][0]
                hours = np.array([[hours_studied[i]]])
                predicted = predictor.predict(hours)[0][0]  # must be 2D 
                sum_errors += (actual - predicted) ** 2
            
            mse = sum_errors / len(hours_studied)
            print("Mean Squared Error (MSE): ", mse)
            print("Meaning this is the Average difference between the actual and predicted values.")
        elif choice == "5":   
            hours_studied_input = int(input("Enter hours studied: "))
            print("Predicted exam score: ", predictor.predict([[hours_studied_input]]))  
        elif choice == "6":
            target_score = 100 # Target score
            required_hours = (target_score - b[0]) / m[0][0] 
            print(f"To score 100%, you would need to study approximately {required_hours:.2f} hours.")
        elif choice == "7":
            print("Thank you for using the predictor! - Made by Lukas.L")
            break
        else:
            print("Invalid choice")
     
main()