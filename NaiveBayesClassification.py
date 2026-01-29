
import numpy as np
import pandas as pd 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score # only really needed for testing data and seeing how well the model performs
from sklearn.metrics import confusion_matrix #correct / incorrect matrix of model. , How many false positives 




df = pd.read_csv("fake_bills.csv", sep = ";")
repline = "-" * 60
smallerrepline = "-" * 21
print(repline)
print(smallerrepline + "FAKE MONEY CHECKER" + smallerrepline)
print(repline)



df = df.dropna(subset=["margin_low"]) # drop th NaN

features = ["diagonal","height_left","height_right","margin_low","margin_up","length"]
X = df[features]
y = df["is_genuine"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=50                 # split from training data and testing data. / only if no user input is collected
)

NBmodel = GaussianNB()


NBmodel.fit(X_train,y_train)
predictedY = NBmodel.predict(X_test)
accuracyScore = accuracy_score(y_test, predictedY) * 100
print("Accuracy: ", accuracyScore)

print(repline)
print("You will require to measure your bill and input the values below:")
print("Diagonal length:")
print("Height of the left side:")
print("Height of the right side:")
print("Distance from the printed design to the Bottom edge")
print("Distance from the printed design to the Top edge")
print("Length of the banknote:")
print("All values to be rounded to 2 decimal places")
print(repline)

completed = False
while completed == False: 
    try:
        diagonal = float(input("Enter the diagonal of the banknote: "))
        height_left = float(input("Enter the height of the left side: "))
        height_right = float(input("Enter the height of the right side: "))
        margin_low = float(input("Enter the distance from the printed design to the Bottom edge: "))
        margin_up = float(input("Enter the distance from the printed design to the Top edge: "))
        length = float(input("Enter the length of the banknote: "))
        completed = True
    except ValueError:
        print("Please enter a valid number")
        continue
print(repline)

user_input = [[diagonal, height_left, height_right, margin_low, margin_up, length]]
prediction = NBmodel.predict(user_input)

print("The bill is: ", prediction)
print(repline)
print("thanks for using.. made by Lukas.L")