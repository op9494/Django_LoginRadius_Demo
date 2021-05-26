# Django_LoginRadius_Demo
Demo project implemented login radiius Djangod.

 ```
 As This project has been done by the support of Loginradius developer free plan
```

## INSTALLATION
1. Install [django](https://www.djangoproject.com/download/) and then install 'pip'
2. Use the below code to install the needed packages used in the application
### To install
```
$ pip install
```
```
 $ pip update
```
```
python manage.py makemigrations
```
``` 
python manage.py migrate
```
3.How to run the application. from the current directory run the code from bash
```
python manage.py runserver
```
## Link to Visit
To visit [MAIN RESOURCE PAGE](http://127.0.0.1:8000/)

## For Testing
 -Move on to test folder and run as below
 ```
 python test.py
 ```
 -Install the selenium before it
 '''
 Pip install selinium
 '''
 It shows the result as below
 ```
 $ python test.py

DevTools listening on ws://127.0.0.1:64276/devtools/browser/14833c42-fe29-4edf-8130-319394306deb
---Visted----http://127.0.0.1:8000/-------Mainpage----- 
---Visted----http://127.0.0.1:8000/dashboard-------Mainpage-----case studey In this it will load mainpage beacause of no login is done and directly requesting dashboard URL
Test1 success
.
DevTools listening on ws://127.0.0.1:64298/devtools/browser/4fd08e89-468f-4dbf-a0be-b187db740c3c
[18160:5464:0526/234349.032:ERROR:device_event_log_impl.cc(214)] [23:43:49.032] USB: usb_device_handle_win.cc:1054 Failed to read descriptor from node connection: A device attached to the system is not functioning. 
(0x1F)
[18160:5464:0526/234349.034:ERROR:device_event_log_impl.cc(214)] [23:43:49.034] USB: usb_device_handle_win.cc:1054 Failed to read descriptor from node connection: A device attached to the system is not functioning. 
(0x1F)
Test2 success
.
DevTools listening on ws://127.0.0.1:64346/devtools/browser/d7f12ef7-9ef8-4286-ad69-e435f710c6e6
[15548:12180:0526/234404.490:ERROR:device_event_log_impl.cc(214)] [23:44:04.490] USB: usb_device_handle_win.cc:1054 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
Test3 success
.
DevTools listening on ws://127.0.0.1:64395/devtools/browser/bbe7d2fa-eeb7-433d-a600-806b0ccb9a63
This is the current dashboarhttps://opdemo.hub.loginradius.com/auth.aspx?action=login&return_url=http://127.0.0.1:8000/login/auth
[11380:11808:0526/234439.291:ERROR:device_event_log_impl.cc(214)] [23:44:39.290] USB: usb_device_handle_win.cc:1054 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
[11380:11808:0526/234439.295:ERROR:device_event_log_impl.cc(214)] [23:44:39.295] USB: usb_device_handle_win.cc:1054 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
Stored:None
Test4 success
.
DevTools listening on ws://127.0.0.1:64448/devtools/browser/d8537f90-f69e-460b-b4ce-20140e134eb0
[7012:2108:0526/234503.449:ERROR:device_event_log_impl.cc(214)] [23:45:03.449] USB: usb_device_handle_win.cc:1054 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
[7012:2108:0526/234503.455:ERROR:device_event_log_impl.cc(214)] [23:45:03.455] USB: usb_device_handle_win.cc:1054 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
For resetting password mail has been sent to Your mail id
Test5 success
.
----------------------------------------------------------------------
Ran 5 tests in 99.655s

OK
 ```

