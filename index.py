import requests
import json

# Replace 'YOUR_ACCESS_TOKEN' with your actual Webex access token
access_token = 'PUT YOUR ACCESS TOKEN HERE'
base_url = 'https://api.ciscospark.com/v1/'

def test_connection():
    url = base_url + 'people/me'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Connection to Webex server successful.")
    else:
        print("Failed to connect to Webex server.")
    input("Press Enter to return to the main menu...")

def display_user_information():
    url = base_url + 'people/me'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_info = response.json()
        print(f"Displayed Name: {user_info['displayName']}")
        print(f"Nickname: {user_info['nickName']}")
        print(f"Emails: {', '.join(user_info['emails'])}")
    else:
        print("Failed to fetch user information.")
    input("Press Enter to return to the main menu...")

def list_rooms():
    url = base_url + 'rooms'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'max': 5
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        rooms = response.json()['items']
        for room in rooms:
            print(f"Room ID: {room['id']}")
            print(f"Room Title: {room['title']}")
            print(f"Date Created: {room['created']}")
            print(f"Last Activity: {room['lastActivity']}")
            print()
    else:
        print("Failed to retrieve room list.")
    input("Press Enter to return to the main menu...")

def create_room():
    title = input("Enter the title for the new room: ")
    url = base_url + 'rooms'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'title': title
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("Room created successfully.")
    else:
        print("Failed to create the room.")
    input("Press Enter to return to the main menu...")

def send_message_to_room():
    url = base_url + 'rooms'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'max': 5
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        rooms = response.json()['items']
        for i, room in enumerate(rooms):
            print(f"{i + 1}. Room Title: {room['title']}")
        room_choice = int(input("Enter the room number to send a message to: ")) - 1
        if 0 <= room_choice < len(rooms):
            room_id = rooms[room_choice]['id']
            message = input("Enter the message to send: ")
            message_url = base_url + 'messages'
            message_headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'  # Specify the Content-Type
            }
            message_data = {
                'roomId': room_id,
                'text': message
            }
            message_response = requests.post(message_url, headers=message_headers, data=json.dumps(message_data))
            if message_response.status_code == 200:
                print("Message sent successfully.")
            else:
                print(f"Failed to send the message. Error code: {message_response.status_code}")
                print(f"Error message: {message_response.text}")
        else:
            print("Invalid room choice.")
    else:
        print("Failed to retrieve room list.")
    input("Press Enter to return to the main menu...")


# Main Menu
while True:
    print("Webex Troubleshooting Tool Menu:")
    print("0. Test Connection")
    print("1. Display User Information")
    print("2. List Rooms")
    print("3. Create a Room")
    print("4. Send Message to a Room")
    print("5. Exit")

    choice = input("Enter your choice (0-5): ")

    if choice == '0':
        test_connection()
    elif choice == '1':
        display_user_information()
    elif choice == '2':
        list_rooms()
    elif choice == '3':
        create_room()
    elif choice == '4':
        send_message_to_room()
    elif choice == '5':
        print("Exiting the Webex Troubleshooting Tool. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (0-5).")
