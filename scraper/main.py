import requests
import os
import hashlib

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

offer = {
    "source": "TEST",
    "title": "Test Offer",
    "route": "Mediterranean",
    "price": 123
}

offer["offer_hash"] = hashlib.md5(
    f"{offer['source']}-{offer['title']}-{offer['price']}".encode()
).hexdigest()

requests.post(
    f"{SUPABASE_URL}/rest/v1/offers",
    headers={
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "resolution=ignore-duplicates"
    },
    json=offer
)

print("Done")
