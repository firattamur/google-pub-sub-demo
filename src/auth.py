from google.oauth2 import service_account
from config import credentials_path

credentials = service_account.Credentials.from_service_account_file(credentials_path)
