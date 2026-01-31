

# from sklearn.linear_model import LinearRegression
# model = LinearRegression()

# X = [[1], [2], [3], [4], [5]]
# y = [40, 50, 65, 75, 90]

# model.fit(X, y)
# hours = float(input("Enter the value: "))
# predicted_marks = model.predict([[hours]])
# print(f"Predicted marks for {hours} hours of study is: {predicted_marks}")

# from sklearn.linear_model import LogisticRegression

# X = [ [1], [2], [3], [4], [5]] # Hours Studied input
# y = [ 0, 0, 1, 1, 1] # Pass/Fail output

# model = LogisticRegression()
# model.fit(X, y)
# hours = float(input("Enter the value: "))
# predicted_result = model.predict([[hours]])
# if predicted_result == 1:
#     print(f"Predicted result for {hours} hours of study is: Pass")
# else:
#     print(f"Predicted result for {hours} hours of study is: Fail")


# from sklearn.neighbors import KNeighborsClassifier

# X = [
#     [180, 7],
#     [200,7.5],
#     [250,8],
#     [300,8.5],
#     [330,9],
#     [360,9.5]
# ]
# # 0 = Apple , 1 = Orange
# y = [0,0,0,1,1,1]

# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X, y)
# weight = float(input("Enter the weight of fruit in grams: "))
# size = float(input("Enter the size of the fruit in cm: "))
# predicted_fruit = model.predict([[weight, size]])
# if predicted_fruit == 0:
#     print("The fruit is an Apple")
# else:
#     print("The fruit is an Orange")
# # --- IGNORE ---

from sklearn.tree import DecisionTreeClassifier
X = [
    [7, 2],
    [8,3],
    [9,8],
    [10,9]
]
y = [0,0,1,1]  # 0 = No , 1 = Yes
model = DecisionTreeClassifier()
model.fit(X, y)
age = int(input("Enter the Fruit size in cm : "))
shade = int(input("Enter the Fruit color shade (1-10) : "))
predicted_edibility = model.predict([[age, shade]]) 
if predicted_edibility == 0:
    print("The fruit Apple")
else:
    print("The fruit is Orange")

