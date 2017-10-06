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

        for entry in dbx.files_list_folder("/Apps/O'Reilly Media").entries:
            print(entry.name)

        # for entry in dbx.files_list_revisions("/my-file-backup.txt").entries:
        #     print(entry)

        for result in dbx.files_search("/Apps", "Java").matches:
            print(result.metadata.name)

    except AuthError as err:
        sys.exit("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
