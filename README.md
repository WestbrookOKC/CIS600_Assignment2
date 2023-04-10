# CIS600_Assignment2
This repository is used for education.

station_1.py and station_2.py is used to send virtual sensor data to MTQQ topic.

website.py is used to connect to DynamoDB and get the virtual sensor data, then display it on the website.

To realize the assignment, we should do the following step by step.

1. 
  Run the station_1.py and station_2.py and last it for 15 seconds, which may send sensor three times.
  
  We should not run these two files for too long, it is because the usage of AWS.
  
2.
  Run the website.py and do not close it.
  
  Go to website: http://127.0.0.1:5000/   
  
  input temperature(or other sensor name you want but ensure it exists) in the table.
  
  ![image](https://user-images.githubusercontent.com/100655843/230997865-d85a8838-d634-4a3f-951a-dd02fc53b027.png)

  
  It will jump to http://127.0.0.1:5000/sensor_data and display the temperature data of all stations
  
  ![image](https://user-images.githubusercontent.com/100655843/230997897-d385785e-2eec-48bd-bb1a-03a6f31d7698.png)
  
  Go to http://127.0.0.1:5000/station_1
  
  it will display the latest sensor data values received from all the sensors of station_1
  
  ![image](https://user-images.githubusercontent.com/100655843/230998091-e6b4a2b6-de83-4031-8092-bb401491762b.png)
  
   Go to http://127.0.0.1:5000/station_2
   
   it will display the latest sensor data values received from all the sensors of station_2
   
   
   ![image](https://user-images.githubusercontent.com/100655843/230998144-38eb8235-a12b-49ae-854d-c9b856b13e03.png)


the assignment should run perfectly with the certificate and private keys which i have provided, if there is any problem, please be free to 

contact me: kfeng07@syr.edu

