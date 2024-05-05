#!/usr/bin/env python
# coding: utf-8

# In[2]:


my_list = []

print("value of my list before loop", my_list)
for i in range(1,10):
    my_list.append(i)  
print("Value of my list after loop", my_list)    


# DHCP

# In[36]:


ip_pool = []

#all mapped ips and devices put in this dictionary
assigned_ip ={}

print("value of my list before loop", ip_pool)

#This gives us a range of different ips from 192.168.1.2 -100
for i in range(2,101):
    ip_address = "192.168.1." + str(i)
    ip_pool.append(ip_address) 
    
#print("Value of my list after loop", ip_pool) 

#This function takes the ips and maps it to devices in the dictionary
def request_ip(device_id):
    
    ip_address_to_assign =ip_pool.pop(0)
    assigned_ip[device_id] = ip_address_to_assign
    
#This function gets the ips from the dictionary based on the device id and returns it    
def return_ip(device_id):
    return assigned_ip[device_id]
    
#print(assigned_ip)
print(request_ip("my_TV"))
#print(request_ip("my_Phone"))
#print(request_ip("my_Laptop"))
#print(request_ip("my_Tablet"))
#print(assigned_ip)
print(return_ip("my_TV"))


# In[ ]:




