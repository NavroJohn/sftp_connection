import paramiko

'''
This script uses the paramiko module to make a connection to Draxis sftp server
where the Africultures servises are storeddatetime A combination of a date and a time. Attributes: ()
You need to set the path for the id_rsa file, the keypass for that file 
If you want to upload any files in the server you must define the loacl and remote paths.
TODO:
- Make a function to upload the files and check if the defined remote path exists or not and create the appropriate path if needed
- Make a log of the connections and any changes made to the server 
- Add the POST request to the server to nottify that the data has been uploaded

Credits: 
-   Dimitris Kasabalis
    email: dkasampa@agro.auth.gr
'''

def create_client(host, port, username, keypath, keypass):
    global transport
    transport = paramiko.Transport((host, port))
    mykey = paramiko.RSAKey.from_private_key_file(keypath, keypass)
    print("Connecting...")
    transport.connect(username=username, pkey=mykey)
    global sftp
    sftp = paramiko.SFTPClient.from_transport(transport)
    print("Connected.")
    print(sftp.listdir())


host = "18.196.31.48"
port = 2310
keypath = "" # Insert the path of the id_rsa file.
keypass = "" # Insert the keypas for your ssh key 
username = "user1"

create_client(host= host, port=port, username=username, keypath=keypath, keypass=keypass)

## Uncomment of you want to upload files
# localPath = ""
# remotePath = ""

# sftp.put(localpath=localPath, remotepath=remotePath)

sftp.close()
transport.close()
print("Closed connection.")