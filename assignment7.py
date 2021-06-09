import os
from src.utils import set_db_path

cwd = os.getcwd()
print(f"Current directory: {cwd}")
print(f"Setting db-path")
set_db_path(cwd)



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
