What is Systemd?
It is basically an innit system which is the most important process when we start our LINUX  system.They are also referred to as PID1 since its the first to start.
It manages all the services thst runs in the background.

Working with Units:-
Units are basically resources that are able to mange the services,timers,mounts,automounts.Units are what systemd can mange for us and services are a type of unit.

Installing apache:-
We use the command sudo apt install apache2
![image](https://github.com/user-attachments/assets/d0b71edd-1d76-4db6-8342-9eab7074b52b)

We then checked the status to make sure weather it installs apache2 or not by using the command systemctl status apache2
![image](https://github.com/user-attachments/assets/c58178ac-a89b-4051-9397-6629196e37a9)

![image](https://github.com/user-attachments/assets/cbd955d9-38b7-4427-b857-819e5dec6100)


There are some important commands:-
1).sudo systemctl start apache2-which basically starts the server.
2).sudo systemctl stop apache2-which stops the server.
3).sudo systemctl restart apache2-which resarts the server, it is too fast we won't even notice.
4).sudo systemctl enable apache2-which enables the server and make sure it dosen't start as soon as the computer starts running.
5).sudo systemctl disable apache2-which disables the server.
6).sudo systemctl reload apache2-which instructs systemd to reload its configuration files that means unit files as well.

![image](https://github.com/user-attachments/assets/f5f97a5f-05fe-44ea-8873-65d1e31a4f7b)

![image](https://github.com/user-attachments/assets/e71c6cdc-220b-47cf-826a-409c5850c1bb)

![image](https://github.com/user-attachments/assets/92620dd8-cb46-41b5-8a55-7d43d3ac60da)


Service Files:-service  files are just text files that contain instructions that tell systemd what needs to be done to manage that  particular service.
These files specify how a service should be started, stopped, and managed. 
Systemd unit directories
1./etc/systemd/system
2./run/systemd/system
3./lib/systemd/system
where 1st is the most prioritized and 3rd the least.


/lib/systemd/system is the directory that installed service files to go into so when we install a package it basically includes a service file which is going to be found inside that directory
![image](https://github.com/user-attachments/assets/5b32c8b2-8576-4b0d-b5ce-d0735bf728b8)
We have more than service files we have mount as well as target files as well.


![image](https://github.com/user-attachments/assets/2f736dd3-058d-40e6-9956-dc731ab00ef5)
We also have apache service files that we installed


/run/systemd/system store runtime systemd units
![image](https://github.com/user-attachments/assets/4869fa45-2bbd-451a-bd01-03159505a915)


![image](https://github.com/user-attachments/assets/ddbb5345-2d2f-416c-964a-efcefd38f905)

![image](https://github.com/user-attachments/assets/a2b5c3e9-c2c3-4976-8fdf-c308d8c717ec)
The error was there because we didn't use sudo because we dont want to modify this file yet we can ignore it.


Editing part of the systemd:-
1st method:-sudo systemctl edit apache2.service

![image](https://github.com/user-attachments/assets/ef459c45-0b21-47e1-a8ce-2300ee4d50d2)

![image](https://github.com/user-attachments/assets/de10a63b-fcc5-4754-aab7-c1b7113fb9ef)

We made some changes:-
![image](https://github.com/user-attachments/assets/63010702-1666-4dd5-9a2f-ff2fbc8252d1)

![image](https://github.com/user-attachments/assets/752715f2-9bf9-4f2c-ae9e-86adc8f071e5)
We deleted the file using sudo rm command which removes files or directories.


2nd method:-
![image](https://github.com/user-attachments/assets/a8dd7668-6129-4ad8-9477-c0d532545d3a)

It is not an override file.
![image](https://github.com/user-attachments/assets/1dd5c676-4ec0-4047-b53d-0018ccc36951)

In 1st method we are creating an overide file that gives us the option tot add the sections settings that we want to ovveride and having it stored in an override file rather than having entirety of the systemd all over againn.(To override something is to cause something else to operate instead of it without harming or changing the thing overridden)
whereas ,
--full option is telling systemd that we want to start with an entire configuartion file an entire service file and use that as a base.

![image](https://github.com/user-attachments/assets/c72b199a-8cd7-4578-960d-b12d1e279a61)
basically creates a copy of original method.


This command takes into account about all the changes that we made.
![image](https://github.com/user-attachments/assets/d3e0c8e0-fce2-4457-9bbf-64270477ad71)

