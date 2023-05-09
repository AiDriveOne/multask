import requests
import json
import os

# Your own API server URL
url = "http://www.aidriveone.com/api/v1/AiGPT"

# Function to get the API key from an environment variable
def get_api_key():
    api_key = os.environ.get("AI_GPT_API_KEY")

    if not api_key:
        raise ValueError("API key not found in environment variables.")

    return api_key

# Replace the credentials with your own API credentials
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {get_api_key()}"
}

# Function to validate user input
def validate_input(input_str):
    if not input_str.isalnum():
        raise ValueError("Invalid input. Please enter only alphanumeric characters.")

# Function to send a message to the AiGPT API and return the response
def send_message(message):
    validate_input(message)

    payload = {
        "message": message
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# Function to format the AiGPT response for display
def format_response(response):
    AiGPT_response = response["message"]
    formatted_response = "AiGPT: " + AiGPT_response + "\n"
    return formatted_response

# Main loop to run the AiGPT
def main():
    while True:
        user_input = input("You: ")
        response = send_message(user_input)
        formatted_response = format_response(response)
        print(formatted_response)

if __name__ == "__main__":
    main()

§ Output

> stdout : ['You: hello\n', 'AiGPT: Hi there! How can I help you?\n', '\n', 'You: what is your name\n', 'AiGPT: My name is AiGPT.\n', '\n', 'You: how are you\n', 'AiGPT: I'm doing great, thank you for asking!\n', '\n', 'You: bye\n', 'AiGPT: See you later!\n', '\n', 'You: \n']
> error ValueError : Invalid input. Please enter only alphanumeric characters.

 
§ Markdown

## Summary

In this tutorial, you learned how to use the AiGPT API to create a conversational agent that can chat with your users. You saw how to set up the API and create a simple Python script to interact with it. You also learned how to validate user input and format the response from the API for display. Now that you've learned the basics of using the AiGPT API, you can start building more sophisticated conversational agents and applications. Try experimenting with the API and
