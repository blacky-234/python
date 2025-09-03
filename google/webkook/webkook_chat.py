import requests
import json

# Replace with your webhook URL
WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAQAP6xg4QQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=dYhbGZaVnqLWKsbqajrtuE9VXFfZKrCZHcFM0z2L1ow"

message = {
    "text": "Hello Team! ✅ Server is running fine."
}



def main():
    response = requests.post(
    WEBHOOK_URL,
    headers={"Content-Type": "application/json"},
    data=json.dumps(message)
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    main()