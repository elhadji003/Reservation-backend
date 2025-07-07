import os
import tempfile
import json

def get_google_credentials_file():
    raw = os.getenv('GOOGLE_SERVICE_ACCOUNT_JSON')
    if not raw:
        return None

    try:
        data = json.loads(raw)
        data["private_key"] = data["private_key"].replace('\\n', '\n').strip()

        path = os.path.join(tempfile.gettempdir(), 'google-cred.json')
        with open(path, "w") as f:
            json.dump(data, f)
        return path
    except Exception as e:
        print("Erreur parsing clé Google:", e)
        return None
