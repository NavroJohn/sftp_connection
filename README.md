# sftp_client

This script uses the paramiko module to make a connection to Draxis sftp server
where the Africultures services are stored.
You need to set the path for the id_rsa file, the keypass for that file 
If you want to upload any files in the server you must define the local and remote paths.
TODO:
- Make a function to upload the files and check if the defined remote path exists or not and create the appropriate path
 if needed
- Make a log of the connections and any changes made to the server 
- Add the POST request to the server to notify that the data has been uploaded
Credits: 
-   Dimitris Kasabalis
    email: dimitriskasabalis@gmail.com
