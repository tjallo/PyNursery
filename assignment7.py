import os
from src.utils import set_db_path


def main():
    """
    Main Function

    Does initial setup, and runs webserver
    """

    # Setting database DB path in the settings.json file
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


if __name__ == '__main__':
    main()