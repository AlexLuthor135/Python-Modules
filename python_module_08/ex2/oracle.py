import os
from dotenv import load_dotenv

load_dotenv()
mode = os.getenv("MATRIX_MODE", "development")
database = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL", "INFO")
zion_endpoint = os.getenv("ZION_ENDPOINT")

if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print("Mode:", mode)
    print("Database:", "Configured" if database else "Not configured")
    print("API Access:", "Authenticated" if api_key else "Not configured")
    print("Log Level:", log_level)
    print("Zion Network:", "Online" if zion_endpoint else "Offline")
    if mode == "development":
        print("Development environment active")
    elif mode == "production":
        print("Production environment active")
    else:
        print("WARNING: Invalid MATRIX_MODE")
    if mode == "production" and not all(
        (database, api_key, zion_endpoint)
    ):
        print("WARNING: Missing production configuration")
