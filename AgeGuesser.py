import pip._vendor.requests
import requests

# Store URL
myURL = "https://api.agify.io/"

# Store the Query String Parameters
person = input("Input a name:")
queryString = { "name": person }

# Get Request
responseData = requests.get(myURL, params=queryString)

# Display the result as JSON
resultDictionary = responseData.json()
print(resultDictionary)
print(f"The predicted age based on the name {person} is {resultDictionary['age']}.")

input_age = resultDictionary['age']

# Import the Matplotlib Module
import matplotlib.pyplot as plt

# Setup example Names and Predicted Ages
names = ["Brandon", "Leah", "Peter", "Skylar", person]
ages = [25, 40, 58, 40, input_age]

# Plot them on a basic graph
plt.bar(names, ages, color="green")

#Set the text
plt.title('Predicted Age by Name')
plt.xlabel('Names')
plt.ylabel('Predicted Age')

# Display the Graph
plt.show()