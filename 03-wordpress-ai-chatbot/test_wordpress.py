import requests
import os
import sys

# Try to get from environment or use placeholders
WORDPRESS_URL = os.getenv("WORDPRESS_URL", "https://your-wordpress-site.com")
USERNAME = os.getenv("WORDPRESS_USERNAME", "admin")
APP_PASSWORD = os.getenv("WORDPRESS_APP_PASSWORD", "")

def test_wordpress():
    print(f"Testing WordPress connectivity to: {WORDPRESS_URL}")
    endpoint = f"{WORDPRESS_URL.rstrip('/')}/wp-json/wp/v2/posts"
    
    try:
        response = requests.get(endpoint, params={"per_page": 1})
        if response.status_code == 200:
            print("✅ Successfully connected to WordPress REST API!")
            print(f"Total posts found: {response.headers.get('X-WP-Total')}")
            return True
        else:
            print(f"❌ Failed to connect. Status code: {response.status_code}")
            print(f"Response: {response.text[:200]}")
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    if not test_wordpress():
        sys.exit(1)
