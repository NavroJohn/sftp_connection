import os
import paramiko
from dotenv import load_dotenv

load_dotenv() 

'''
This script uses the paramiko module to make a connection to an sftp server. 

You need to set the path for the id_rsa file and the keypass for that file.

If you want to upload any files in the server you must define the local and remote paths.

TODO:
- Make a function to upload the files and check if the defined remote path exists or not and create the appropriate path 
if needed
- Make a log of the connections and any changes made to the server 
- Add the POST request to the server to notify that the data has been uploaded

Credits: 
-   Dimitris Kasabalis
    email: dkasampa@agro.auth.gr
'''

def create_client(host, port, username, keypath, keypass):
    '''

    :param host: The server address
    :param port: The port
    :param username: Specify the name of the user
    :param keypath: Specify the location of the id_rsa file in your machine
    :param keypass: Specify the password for the id_rsa key

    '''
    global transport
    transport = paramiko.Transport((host, port))
    mykey = paramiko.RSAKey.from_private_key_file(keypath, keypass)
    print("Connecting...")
    transport.connect(username=username, pkey=mykey)
    global sftp
    sftp = paramiko.SFTPClient.from_transport(transport)
    print("Connected.")
    print(sftp.listdir())


host = os.getenv("host")
port = int(os.getenv("port"))
username = os.getenv("username")
keypath = os.getenv("keypath")
keypass = os.getenv("keypass")

create_client(host=host, port=port, username=username, keypath=keypath, keypass=keypass)

# Uncomment of you want to upload files
# localPath = ""
# remotePath = ""

# sftp.put(localpath=localPath, remotepath=remotePath)

sftp.close()
transport.close()
print("Closed connection.")