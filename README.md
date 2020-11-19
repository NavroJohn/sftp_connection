# sftp_client

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
    email: dimitriskasabalis@gmail.com
