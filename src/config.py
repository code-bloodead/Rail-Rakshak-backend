from decouple import config

USERNAME = config("USER")
PASSWORD = config("PASSWORD")
DB_URL = config("DB_URL")
SMS_WEBHOOK = "https://www.fast2sms.com/dev/bulkV2"
API_KEY = config("API_KEY")