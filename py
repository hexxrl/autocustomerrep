import requests
import json

def get_auto_response(message):
  """Gets an auto response for a support message.

  Args:
    message: The support message.

  Returns:
    The auto response.
  """

  url = "https://api.example.com/support/auto_response"
  headers = {
    "Content-Type": "application/json",
  }
  data = {
    "message": message,
  }

  response = requests.post(url, headers=headers, data=data)
  if response.status_code == 200:
    return response.json()["response"]
  else:
    raise Exception("Failed to get auto response")

if __name__ == "__main__":
  message = "I'm having trouble logging in."
  response = get_auto_response(message)
  print(response)

def get_auto_response_with_categories(message):
  """Gets an auto response for a support message, along with the categories that the message belongs to.

  Args:
    message: The support message.

  Returns:
    A tuple of the auto response and the categories.
  """

  url = "https://api.example.com/support/auto_response_with_categories"
  headers = {
    "Content-Type": "application/json",
  }
  data = {
    "message": message,
  }

  response = requests.post(url, headers=headers, data=data)
  if response.status_code == 200:
    return response.json()["response"], response.json()["categories"]
  else:
    raise Exception("Failed to get auto response")

if __name__ == "__main__":
  message = "I'm having trouble logging in."
  response, categories = get_auto_response_with_categories(message)
  print(response)
  print(categories)
