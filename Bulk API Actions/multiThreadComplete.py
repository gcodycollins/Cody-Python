##############################################
#
# Created by Grayson Cody Collins
#
# Please reach out to cody.collins@alfresco.com or skypeId cody.collins_3
# with any questions, improvements, or requests.
#
##############################################

##############################################
#
# This is a python script used to collect a list of list of task ids
# then to use the list of lists in multithreaded request calls to complete the tasks
#
##############################################

# Still in progress, so far, not true multiprocessing and does not complete faster

import threading
import requests
from requests.auth import HTTPBasicAuth
import json
import multiprocessing









#function for completing set of processes in thread
def form_thread (count):

    #this will be a list of lists
    #tasksT = []
    
    #this is a list of all task IDs in the below api call
    tasks = []
        
    # API 1 get all currently running tasks in batches of 100. use count for pagination
    url = "http://54.175.46.136:8080/activiti-app/api/enterprise/tasks/query"

    headers = {
        'content-type': "application/json"
    }
                
    payload = "{\n\"appDefinitionId\":1,\n\"size\":\"100\",\n\"start\":"+str(count)+",\n\"state\":\"active\"\n}"
                
    response = requests.request("POST", url, data=payload, headers=headers, auth=HTTPBasicAuth('admin@app.activiti.com','admin'))

    #print(response.text)

    jData = json.loads(response.content)
            
           

    # Add all results of get running task api into a list. also used index exception to avoid index out of bounds once last task is reached.
    j = 0
    end = False

    while (end!=True):
        try:
            tasks.append(str(jData['data'][j]['id']))
            j+=1
        except IndexError:
            end=True

    #add the list to the list of lists
    #tasksT.append(tasks)


        
        

    #API 2 complete the processes using the tasks list
    for i in range(0,len(tasks)):
         
        # API 2 complete task
        url2 = "http://54.175.46.136:8080/activiti-app/api/enterprise/tasks/"+tasks[i]+"/action/complete"

        headers2 = {
            'content-type': "application/json",

        }

        response2 = requests.request("PUT", url2, headers=headers2, auth=HTTPBasicAuth('admin@app.activiti.com','admin'))

            
        #if (i==99):
            #print(response2.text)
            
            
    print("######################")
    print(str(count)+" thread complete")
    print("######################")











threadnum=50

#loop to define how many times to make the multi-threaded requests
for k in range (0,10):

       
        
    threads = []

    #multithreaded processing
    for i in range(0,threadnum):
    
        if __name__ == "__main__":
        
            t = multiprocessing.Process(target=form_thread(i))
            threads.append(t)
            t.start()
            t.join()
		
		
	#print to confirm thread loop completion
    print("######################")
    print(str(k)+" loop complete")
    print("######################")