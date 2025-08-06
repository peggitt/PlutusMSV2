from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseBadRequest
from django import forms
from django.template import RequestContext
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import json
from django.core import serializers
from django.db.models import Avg, Count, Min, Sum, Max
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from Security import Configs
from Security.models import Endpoint
from .models import MainModule
from django.contrib import messages
import sys
from django.db import connection

from django.db.models import F, Value
from django.db.models.functions import Replace
# Create your views here.

@csrf_exempt
def UIConfigs_view(request, *args, **kwargs):
    try:
        #print('Hr')
        UserLog = request.session['username']
        CollabLog = request.session['CollabKey']

        if CollabLog == '':
            return render(request,"login.html",{})
        else:

            #print(UserLog,CollabLog,BranchLog,BankLog)
            #Join with Rights
            
            Userrole = Configs.GetSuperUserRole(UserLog)
            uRoleName = Userrole['SuperAdminUser']
            #print(uRoleName)
            if uRoleName is not None:
                GridModules = MainModule.objects.all().order_by('ParentModuleId','MenuName')

                #GridSubModules = SystemSubModule.objects.all().order_by('MenuKeyHierarchy')
                return render(request,"Configurations/ui.html",{"Modules":GridModules})
            else:
                return render(request,"Configurations/ui.html",{"Modules":[]})

    except:

        return render(request,"login.html",{})
    

@csrf_exempt	
def UIConfigDetails_view(request, *args, **kwargs):

    if Configs.is_ajax(request):
        #print('Hr')
        try:
            UserLog = request.session['username']
            CollabLog = request.session['CollabKey']

            if CollabLog == '':
                return render(request,"login.html",{})
            else:
                
                UserName = UserLog
                Activity = request.POST.get('ActionID', None)

                if Activity=='viewForm':
                    EndPointEnv= Configs.ENDPOINTEnvironment
                    MainEndpoint = Endpoint.objects.filter(EndpointKey='Core'+EndPointEnv).values('Address')
                    Endpointaddress = MainEndpoint[0]['Address']+'ModuleConfigs'

                    ModuleId = request.POST.get('FormId', None)
                    payload = json.dumps({
                        "UserName":UserName,
                        "ModuleId": ModuleId
                    })
                    headers = {
                    'Authorization': 'Bearer '+CollabLog
                    }

                    response = requests.request("GET", Endpointaddress, headers=headers, data=payload)
                    if(response.status_code==204 or response.status_code==403 or response.status_code==404 or response.status_code==401 or response.status_code==422 or response.status_code==500):
                        resText= response.text
                        resJSon=json.loads(resText)
                        return JsonResponse({"Exception": resJSon['detail']}, status=response.status_code)
                    elif(response.status_code==202):
                        resText= response.text
                        resJSon=json.loads(resText)
                        if(resJSon['status']==202):
                            return JsonResponse(resJSon)
                        else:
                            return JsonResponse({"Exception": resJSon['detail']}, status=404)
                        
                elif   Activity=='UpdateFormConfig':

                    EndPointEnv= Configs.ENDPOINTEnvironment
                    MainEndpoint = Endpoint.objects.filter(EndpointKey='Core'+EndPointEnv).values('Address')
                    Endpointaddress = MainEndpoint[0]['Address']+'UpdateModuleConfigs'
                    
                    ModuleId = request.POST.get('FormId', None)
                    QuestionJson = request.POST.get('SelectedSettings', None)

                    payload = json.dumps({
                    "UserName":UserName,
                    "ModuleId":ModuleId,
                    "QuestionJson":QuestionJson
                    })
                    headers = {
                        'Authorization': 'Bearer '+CollabLog
                    }

                    response = requests.request("PUT", Endpointaddress, headers=headers, data=payload)
                    if(response.status_code==403 or response.status_code==404 or response.status_code==401 or response.status_code==422 or response.status_code==500 or response.status_code==405):
                        resText= response.text
                        resJSon=json.loads(resText)
                        return JsonResponse({"Exception": resJSon['detail']}, status=response.status_code)
                    elif(response.status_code==201):
                        resText= response.text 
                        resJSon=json.loads(resText)
                        if(resJSon['status']==202):
                            return JsonResponse(resJSon)
                        else:
                            return JsonResponse({"Exception": resJSon['detail']}, status=404)
            
        except:
            response = {
                'login_status':'Exception' # response message
            }
            return JsonResponse(response)
    else:
        try:
            #print('Hr')
            UserLog = request.session['username']
            CollabLog = request.session['CollabKey']

            if CollabLog == '':
                return render(request,"login.html",{})
            else:
                ListItems = list(kwargs.values())
                ModuleId=ListItems[0]
                print(ModuleId)
                #print(UserLog,CollabLog,BranchLog,BankLog)
                #Join with Rights
                
                return render(request,"Configurations/uidetails.html",{"ModuleId":ModuleId})

        except  Exception as e:
            eString = str(e)
            if eString.find("username") ==1:
                return render(request,"login.html",{})
            else:
                print(eString)
                messages.add_message(eString, 50, 'Error')
                return render(request,"Configurations/uidetails.html",{})
            

@csrf_exempt
def UIModule_view(request, *args, **kwargs):

    if Configs.is_ajax(request):
        #print('Hr')
        try:

            UserLog = request.session['username']
            CollabLog = request.session['CollabKey']
            BranchId = request.session['BranchID']



            if CollabLog == '':
                return render(request,"login.html",{})
            else:
                
                UserName = UserLog
                Activity = request.POST.get('ActionID', None)
                ModuleId = request.POST.get('hdnId', None)


                if Activity=='viewData':
                    EndPointEnv= Configs.ENDPOINTEnvironment
                    MainEndpoint = Endpoint.objects.filter(EndpointKey='Core'+EndPointEnv).values('Address')
                    Endpointaddress = MainEndpoint[0]['Address']+'ModuleConfigsDefaultUserViewData'

                    ModuleId = request.POST.get('FormId', None)
                    Id = request.POST.get('Id', None)

                    payload = json.dumps({
                        "UserName":UserName,
                        "ModuleId": ModuleId,
                        "Id": Id
                    })
                    headers = {
                    'Authorization': 'Bearer '+CollabLog
                    }

                    #print(payload)
                    response = requests.request("GET", Endpointaddress, headers=headers, data=payload)
                    if(response.status_code==204 or response.status_code==403 or response.status_code==404 or response.status_code==401 or response.status_code==422 or response.status_code==500):
                        resText= response.text
                        resJSon=json.loads(resText)
                        return JsonResponse({"Exception": resJSon['detail']}, status=response.status_code)
                    elif(response.status_code==202):
                        resText= response.text
                        resJSon=json.loads(resText)
                        if(resJSon['status']==202):
                            return JsonResponse(resJSon)
                        else:
                            return JsonResponse({"Exception": resJSon['detail']}, status=404)
                        
                elif Activity=='updateFormData':
                    #print('Here')
                    EndPointEnv= Configs.ENDPOINTEnvironment
                    MainEndpoint = Endpoint.objects.filter(EndpointKey='Core'+EndPointEnv).values('Address')
                    Endpointaddress = MainEndpoint[0]['Address']+'ModuleConfigsDefaultUserPostData_'+ModuleId
                    #print(Endpointaddress)
                    form_data = request.POST.dict()
                    
                    if "AccessAllowed" not in form_data:
                        form_data["AccessAllowed"] = ""

                    if "AccessLocked" not in form_data:
                        form_data["AccessLocked"] = ""

                    
                    # Convert the form data to JSON
                    json_data = json.dumps(form_data)

                    MainModuleId = request.POST.get('hdnId', None)

                    payload = json.dumps({
                    "UserName":UserLog,
                    "ModuleId":MainModuleId,
                    "JsonData":json_data
                    })
                    headers = {
                        'Authorization': 'Bearer '+CollabLog
                    }

                    #print(payload)
                    
                    response = requests.request("PUT", Endpointaddress, headers=headers, data=payload)
                    if(response.status_code==403 or response.status_code==404 or response.status_code==401 or response.status_code==422 or response.status_code==500 or response.status_code==405):
                        resText= response.text
                        resJSon=json.loads(resText)
                        return JsonResponse({"Exception": resJSon['detail']}, status=response.status_code)
                    elif(response.status_code==201):
                        resText= response.text 
                        resJSon=json.loads(resText)
                        if(resJSon['status']==202):
                            return JsonResponse(resJSon)
                        else:
                            return JsonResponse({"Exception": resJSon['detail']}, status=404)
                        
                elif Activity=='AddNew':
                    EndPointEnv= Configs.ENDPOINTEnvironment
                    MainEndpoint = Endpoint.objects.filter(EndpointKey='Core'+EndPointEnv).values('Address')
                    Endpointaddress = MainEndpoint[0]['Address']+'ModuleConfigsDefaultUserPostData_'+ModuleId
                    #print(Endpointaddress)
                    form_data = request.POST.dict()
   
                    
                    # Convert the form data to JSON
                    json_data = json.dumps(form_data)

                    print(json_data)

                    MainModuleId = request.POST.get('hdnId', None)

                    payload = json.dumps({
                    "UserName":UserLog,
                    "ModuleId":MainModuleId,
                    "JsonData":json_data
                    })
                    headers = {
                        'Authorization': 'Bearer '+CollabLog
                    }
                    
                    response = requests.request("PUT", Endpointaddress, headers=headers, data=payload)
                    if(response.status_code==403 or response.status_code==404 or response.status_code==401 or response.status_code==422 or response.status_code==500 or response.status_code==405):
                        resText= response.text
                        resJSon=json.loads(resText)
                        return JsonResponse({"Exception": resJSon['detail']}, status=response.status_code)
                    elif(response.status_code==201):
                        resText= response.text 
                        resJSon=json.loads(resText)
                        if(resJSon['status']==202):
                            return JsonResponse(resJSon)
                        else:
                            return JsonResponse({"Exception": resJSon['detail']}, status=404)


        except:
            response = {
                'login_status':'Exception' # response message
            }
            return JsonResponse(response)
    else:
        try:
            #print('Hr')
            UserLog = request.session['username']
            CollabLog = request.session['CollabKey']
            BranchId = request.session['BranchID']

            if CollabLog == '':
                return render(request,"login.html",{})
            else:
                ListItems = list(kwargs.values())
                MainModuleId=ListItems[0]

                MainModuleName=''
                MainModuleDescription=''
                ModuleFolder = ''
                GridData = MainModule.objects.filter(id=MainModuleId).values('ModuleName', 'ModuleDescription','ModuleGroup','IsMainModule','ParentModuleId','IsSubModule')
                if GridData.exists():
                    # Extract the ModuleName from the first result
                    MainModuleName = GridData.first()['ModuleName'] 
                    MainModuleDescription = GridData.first()['ModuleDescription'] 
                    ModuleFolder = GridData.first()['ModuleGroup']
            
                EndPointEnv= Configs.ENDPOINTEnvironment
                MainEndpoint = Endpoint.objects.filter(EndpointKey='Core'+EndPointEnv).values('Address')
                Endpointaddress = MainEndpoint[0]['Address']+'ModuleConfigsDefaultUserView'
                
                payload = json.dumps({
                "UserName":UserLog,
                "ModuleId":MainModuleId,
                "BranchId":BranchId,
                "SearchJson":''
                })
                headers = {
                    'Authorization': 'Bearer '+CollabLog
                }
                
                response = requests.request("GET", Endpointaddress, headers=headers, data=payload)
               
                if(response.status_code==403 or response.status_code==404 or response.status_code==401 or response.status_code==422 or response.status_code==500 or response.status_code==405):
                    resText= response.text

                    resJSon=json.loads(resText)
                    #print(resJSon['detail'])
                    messages.add_message(request, 50, resJSon['detail'])
                    return render(request,"Shared/main.html",{})
                elif(response.status_code==202):
                    resText= response.text 
                    resJSon=json.loads(resText)
                    #print(resJSon)
                    if(resJSon['status']==202):
                        returnGridDetails=resJSon['returnGridDetails']
                        returnFormDetails=resJSon['returnFormDetails']
                        returnDataDetails=[]
                        try:
                            returnDataDetails=resJSon['returnDataDetails']
                        except  Exception as e:
                            eString = str(e)

                        returnComboDetails=resJSon['returnComboDetails']

                        #Get Rights for the Module

                        modules = request.session.get('Modules', [])
    
                        # Find the module with matching id
                        moduleRights = next((m for m in modules if m['id'] == MainModuleId), None)
                        #print(moduleRights)

                        return render(request,ModuleFolder+"/"+MainModuleId+".html",{"MainModuleId":MainModuleId,"MainModuleName":MainModuleName,"MainModuleDescription":MainModuleDescription,
                                                                  "Fields":returnGridDetails,"Form":returnFormDetails,"Data":returnDataDetails,"Combos":returnComboDetails,
                                                                  "ModuleRights":moduleRights})
                    else:
                        messages.add_message(request, 50, 'Error')
                        return render(request,"Shared/main.html",{})
                else:
                    messages.add_message(request, 50, 'No Data Found')
                    return render(request,"Shared/main.html",{})

        except  Exception as e:
            eString = str(e)
            if eString.find("username") ==1:
                return render(request,"login.html",{})
            else:
                print(eString)
                messages.add_message(eString, 50, 'Error')
                return render(request,"Shared/main.html",{})