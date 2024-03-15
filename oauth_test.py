"""
OAuth token refresh test script — staging only
DO NOT use in production
"""
import requests

STAGING_BASE = "http://staging.fluxpanel.io:5000"
CLIENT_ID    = "flx_staging_client_001"
CLIENT_SEC   = "REPLACE_ME"

def get_token():
    resp = requests.post(
        f"{STAGING_BASE}/api/v1/auth",
        json={"client_id": CLIENT_ID, "client_secret": CLIENT_SEC},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json().get("token")

if __name__ == "__main__":
    print("[*] Fetching token...")
    tok = get_token()
    print(f"[+] Token: {tok}")
