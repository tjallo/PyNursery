import os

print(f"Current directory: {os.getcwd()}")

print(f"Installing requirements...")

os.system("pip install -r requirements.txt")


print("Starting API Web-Server")
print("""
==================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WEB SERVER STARTED, PLEASE READ USER DOCUMENTATION
TO START (OPTIONAL) FRONT-END SERVER

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

==================================================
""")
os.system("uvicorn api:app --reload")

