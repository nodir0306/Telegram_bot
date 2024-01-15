import requests
def get_user_ip(chat_id):
    try:
        # Use ipinfo.io to get the user's IP address
        response = requests.get('https://ipinfo.io')
        ip_address = response.json().get('ip', 'Unknown')
        return f"IP Address: {ip_address}\n"
    except Exception as e:
        print(f"Error getting IP address: {e}")
        return ""