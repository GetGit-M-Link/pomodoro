## Pomodoro Timer written in python with a tkinter GUI

inspired by the course 100 days of python on udemy

This timer sents a messages via gotify if the time is up. The Gotify server was already part of my homeautomation setup, that I setup at another time on my Rasberry Pi.
To get your own gotify-server follow these instructions: https://gotify.net/docs/install

To send the message a second .py-file named credentials.py is needed containing a dictionary named gotify in the following format:
```
gotify = {
    'url': "GOTIFY-SERVER-URL",
    'token': 'GOTIFY_TOKEN',
    }

```
![Screenshot_20240412_102009](https://github.com/user-attachments/assets/b4eb41eb-707e-470e-85f5-9e8eece47740)

![Screenshot_20240412_101620](https://github.com/user-attachments/assets/b7ab2cbf-61aa-413d-8b04-de5611efbecb)

