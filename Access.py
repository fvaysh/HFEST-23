# a basic skeleton of a code that fetches data from a github link and displays it here
# some extra fields are also added to create groups and do other stuff too

import requests
import json

# Constants
GITHUB_API_URL = "https://github.com/ossamamehmood/Hacktoberfest2023/tree/main/content/participant/graphql"
ACCESS_TOKEN = "YOUR_GITHUB_ACCESS_TOKEN"
INTERESTS = ["ML", "App dev", "Software Dev", "DevOps"]
MAX_USERS_PER_GROUP = 5

# Data structures
users = {}
groups = {}

def get_user_data(username):
    query = """
    {
        user(login: "%s") {
            name
            login
            joinedAt
            # Fetch other user details here
        }
    }
    """ % username
    headers = {
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    response = requests.post(GITHUB_API_URL, json={"query": query}, headers=headers)
    data = response.json()
    return data["data"]["user"]

def collect_user_data():
    username = input("Enter your GitHub username: ")
    user_data = get_user_data(username)
    if user_data:
        interests = input("Enter your interests (comma-separated): ").split(',')
        users[username] = {
            "name": user_data["name"],
            "joinedAt": user_data["joinedAt"],
            "interests": interests,
            # Add other user details here
        }

def create_groups():
    for interest in INTERESTS:
        group = []
        for username, data in users.items():
            if interest in data["interests"] and len(group) < MAX_USERS_PER_GROUP:
                group.append(username)
        if group:
            groups[interest] = group

def display_data():
    for username, data in users.items():
        print(f"Username: {username}")
        print(f"Name: {data['name']}")
        print(f"Joined at: {data['joinedAt']}")
        # Display other user details here

    for interest, group in groups.items():
        print(f"\nGroup with interest: {interest}")
        for member in group:
            print(f"Member: {member}")

if __name__ == "__main__":
    while True:
        collect_user_data()
        create_groups()
        display_data()
