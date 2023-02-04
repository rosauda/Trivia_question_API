import requests

# ---------------------------- CONSTANTS ------------------------------- #

parameters = {
    "amount": 10,
    "type": "boolean"
}

# ---------------------------- GETTING TRIVIA QUESTIONS USING API ------------------------------- #

# Requesting data
response = requests.get(url="https://opentdb.com/api.php", params=parameters)

# Raising errors and exceptions
response.raise_for_status()

# Data to json
data = response.json()
question_data = data["results"]