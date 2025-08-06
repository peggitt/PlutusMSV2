from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Security import Configs
from .models import Endpoint
from django.http import JsonResponse
import json
import requests

# Create your views here.

def public_login(request, *args, **kwargs):
    try:
		#print('Hr')
        request.session['username']=''
        request.session['CollabKey']=''
        request.session['BranchID']=''
        request.session['Modules']=''
        request.session['MenuModules']=''

        return render(request,"login.html",{})
     
    except:
        return render(request,"login.html",{})
	

def public_logintoken(request, *args, **kwargs):
    try:
		
        username = request.POST.get('UserEmail', '')
        password = request.POST.get('Password', '')
        branchcode = request.POST.get('BranchId', '')

        EndPointEnv= Configs.ENDPOINTEnvironment
        MainEndpoint = Endpoint.objects.filter(EndpointKey='Core'+EndPointEnv).values('Address')


        if not MainEndpoint:
            request.session['username']=''
            request.session['CollabKey']=''
            request.session['BranchID']=''
            request.session['Modules']=''
            request.session['MenuModules']=''

            response = {
                'login_status':'invalid' # response message
            }
            
            return JsonResponse(response)

        else:
            Endpointaddress = MainEndpoint[0]['Address']+'login'

            payload = json.dumps({
                "UserName": username,
                "Password": password,
                "BranchID": branchcode

            })
            headers = {
            'Content-Type': 'application/json'
            }
            print(Endpointaddress)
            response = requests.request("GET", Endpointaddress, headers=headers, data=payload)
            print('response..',response)
            if(response.status_code==403 or response.status_code==404 or response.status_code==401 or response.status_code==422 or response.status_code==405 or response.status_code==500):
                request.session['username']=''
                request.session['CollabKey']=''
                request.session['BranchID']=''
                request.session['Modules']=''
                request.session['MenuModules']=''

                resText= response.text
                resJSon=json.loads(resText)
                print(resJSon) 
                #print(response.json())
                response = {
                    'login_status':'invalid' # response message
                }
                return JsonResponse(response)
            
            


            elif(response.status_code==200):
                request.session['username']=''
                request.session['CollabKey']=''
                request.session['BranchID']=''
                request.session['Modules']=''
                request.session['MenuModules']=''
 
                resText= response.text
                
                resJSon=json.loads(resText)
                #print(resJSon)
                request.session['CollabKey']=resJSon["collab_key"]
                Modules=resJSon['returnModules']
                print(resJSon['returnModules'])
                main_modules=[]
                try:
                    main_modules = [
                        {'id': item['id'], 'modulename': item['ModuleName'],'modulegroup': item['ModuleGroup']}
                        for item in Modules
                        if item['IsMainModule']
                    ]
                except  Exception as e:
                    eString = str(e)
                    print(eString)
                    main_modules = []
                    
                Notifications=resJSon['returnNotifications']
                Name=resJSon['returnName']
                request.session['username'] = username
                request.session['BranchID'] = branchcode
                request.session['Modules']=Modules
                request.session['MenuModules']=main_modules
                
                
                return JsonResponse({"login_status": "Access Granted","mainMenu":main_modules,"Notifications":Notifications,"SystemUser":Name}, status=200)
            
            else:
                response = {
                    'login_status':'Services Unavailable' # response message
                }
                return JsonResponse({"Exception": response}, status=404)
	
    except:
        return render(request,"login.html",{})


@csrf_exempt
def public_view(request, *args, **kwargs):
	try:
		#print('Hr')
		UserLog = request.session['username']
		CollabLog = request.session['CollabKey']

		if CollabLog == '':
			return render(request,"login.html",{})
		else:

			#print(UserLog,CollabLog,BranchLog,BankLog)
			#Join with Rights
			#GridModules = SystemModule.objects.all().order_by('ModuleOrder')
			#GridSubModules = SystemSubModule.objects.all().order_by('MenuKeyHierarchy')
			return render(request,"analytics.html",{})

	except:
		return render(request,"login.html",{})
     

def public_logout(request, *args, **kwargs):
    try:
		#print('Hr')
        #Call Endpoint to Release all Locks
        request.session['username']=''
        request.session['CollabKey']=''
        request.session['BranchID']=''
        request.session['Modules']=''
        request.session['MenuModules']=''

        return render(request,"login.html",{})
     
    except:
        return render(request,"login.html",{})

    