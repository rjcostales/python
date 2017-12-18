import sys

import dropbox
from dropbox.exceptions import AuthError

from keys import TOKEN

if __name__ == '__main__':
    # Check for an access token
    if len(TOKEN) == 0:
        sys.exit("ERROR: Looks like you didn't add your access token. "
                 "Open up backup-and-restore-dropbox-api-examples.py.py in a text editor and "
                 "paste in your token in line 14.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()

        print("\nFiles List Folder...")
        for entry in dbx.files_list_folder("/Apps/O'Reilly Media").entries:
            print(entry.name)

        print("\nFiles List Revisions...")
        for entry in dbx.files_list_revisions("/Apps/O'Reilly Media/Web Scraping with Python/Web Scraping with Python.pdf").entries:
            print(entry)

        print("\nFiles Search...")
        for result in dbx.files_search("/Apps", "Python").matches:
            print(result.metadata.name)

    except AuthError as err:
        sys.exit("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
