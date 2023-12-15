# Application using Vonage API Python Server SDK - JWT auto renewal

## Set up

Copy or rename .env-example to .env<br>
Update parameters in .env file<br>
Have Python version 3.9 or later installed on your system, this application has been tested with Python version 3.9.7<br>
Install modules with the command "pip install --upgrade -r requirements.txt". You may need to manually install additional necessary modules<br>

## How these applications work

### Show Auth failure

When creating a new instance of the SDK, the corresponding JWT has a default expiration time of 15 minutes, meaning after that time, new API calls will fail with "Authentication failed" error.

Execute following commands:

```
python -u script-auth-expires.py > log.txt &
tail -f log.txt
```

The application will make an outbound phone call every 4 minutes.
After 15 minutes since application launch, new API calls will fail with "Authentication failed" error.


To stop the application:

first exit log.txt continuous refresh display with Ctrl+C

then

```
ps aux | grep script
kill -9 <process_id>
```

### Show Auth auto-renewal

In this sample code, the JWT is always automatically renewed before it expires

Execute following commands:

```
python -u script-auth-renews.py > log.txt &
tail -f log.txt
```

The application will make an outbound phone call every 4 minutes.
After 16 minutes since application launch, new API calls will always work as expected


To stop the application:

first exit log.txt continuous refresh display with Ctrl+C

then

```
ps aux | grep script
kill -9 <process_id>
```

## Update your own application

To update your own Python application using Vonage Python Server SDK (version 3.12.0 or later) to handle JWT (Auth) auto-renewal,

copy/paste from script-auth-renews.py file the code in both sections marked between following lines

#===== Add this section to your actual Python code =====
...
...
#================== End add section =====================





