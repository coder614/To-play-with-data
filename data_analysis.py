import json

def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def get_user_name_by_id(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user["name"]
    return "Unknown"

def get_page_name_by_id(pages, page_id):
    for page in pages:
        if page["id"] == page_id:
            return page["name"]
    return "Unknown"

def display_users(data):
    users = data["users"]
    pages = data["pages"]

    print("=== USERS ===\n")
    for user in users:
        friend_names = [get_user_name_by_id(users, fid) for fid in user["friends"]]
        liked_page_names = [get_page_name_by_id(pages, pid) for pid in user["liked_pages"]]

        print(f"{user['name'].title()} (ID: {user['id']})")
        print(f" Friends: {', '.join(friend_names)}")
        print(f" Liked Pages: {', '.join(liked_page_names)}\n")

# Load and display data
data = load_data("data.json")
display_users(data)