var myControls = [];

function LoadCollabError(errMessage)
{
    var opts = {
        "closeButton": true,
        "debug": false,
        "positionClass": "toast-bottom-right",
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    };
    
    toastr.error(errMessage, "Error Message", opts);
}

function showPleaseWait() { 
    
    if (document.querySelector("#pleaseWaitDialog") == null) {
        var modalLoading = '<div class="modal" id="pleaseWaitDialog" data-backdrop="static" data-keyboard="false" role="dialog">\
            <div class="modal-dialog">\
                <div class="modal-content">\
                    <div class="modal-header">\
                        <h4 class="modal-title">Please wait...</h4>\
                    </div>\
                    <div class="modal-body">\
                        <div class="progress">\
                          <div class="progress-bar progress-bar-success progress-bar-striped active" role="progressbar"\
                          aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width:100%; height: 40px">\
                          </div>\
                        </div>\
                    </div>\
                </div>\
            </div>\
        </div>';
        $(document.body).append(modalLoading);
    }
  
    $("#pleaseWaitDialog").modal("show");
} 

function hidePleaseWait() {
    $("#pleaseWaitDialog").modal("hide");
}

function showBusyPopup() {
    // Show the overlay and busy popup
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('busyPopup').style.display = 'block';


}

function hideBusyPopup() {
    // Hide the overlay and busy popup
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('busyPopup').style.display = 'none';
}


function LoadCollabSuccess(successMsg)
{
    var opts = {
        "closeButton": true,
        "debug": false,
        "positionClass": "toast-bottom-right",
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    };
    
    toastr.success(successMsg, "Great!", opts);
}


function LoadCollabInfo(infoMsg)
{
    var opts = {
        "closeButton": true,
        "debug": false,
        "positionClass": "toast-bottom-right",
        "toastClass": "black",
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    };
                
    toastr.info(infoMsg);
}


function GetInputValue()
{
    if (arguments.length > 0)
    {
        for (var intIndex = 0; intIndex < arguments.length; intIndex++)
        {
            var control=null;
            var IsBlockedValue=null;
            var bolIsNumeric=false;
            try
            {
                control = GetControl(arguments[intIndex]);
                IsBlockedValue = control.getAttribute("IsAccessBlocked");
                IsBlockedValue =  parseBoolean(IsBlockedValue);
                bolIsNumeric=parseBoolean(control.getAttribute("IsNumeric"));
            }catch(e){}
            if (document.getElementById(arguments[intIndex]).type == "text")
            {
                if(IsBlockedValue!=null &&IsBlockedValue!=undefined && IsBlockedValue==true)
                {
                   return control.getAttribute("BlockedValue");
                }
//                if(parseBoolean(bolIsNumeric)==true && value=="")// && document.getElementById(ctrl).type!="radio" )
//                {
//                    document.getElementById(ctrl).value="0";
//                    return false;
//                }
                var strUserLanguageID="en";

                if(parent!=null && parent!=undefined && parent!="")
                {
                    try
                    {
                        strUserLanguageID = parent.dhxWins.GetUserLanguageID();
                    }
                    catch(e){strUserLanguageID="en";}
                }
                var dblValue=document.getElementById(arguments[intIndex]).value;
                if(strUserLanguageID!="en" && parseBoolean(bolIsNumeric)==true)
                {
                    // International Numeric Conventions
                    //Danish,Finnish,French,Swedish,Canadian (English and French)    4 294 967 295,000
                    //German 4 294 967.295,000
                    //Italian,Spanish ,Norwegian 4.294.967.295,000
                    //Thai Same as UK,US English

                    switch(strUserLanguageID)
                    {
                        //4 294 967 295,000
                        case "fr"://French
                        case "da"://Danish
                        case "fi"://Finnish
                        case "sv"://Swedish
                        case "de"://German
                        case "it"://Italin
                        case "sw"://Swahili
                        case "es"://Spanish
                        case "no"://Norwegian
                        {
                            dblValue=dblValue+"";
                            dblValue=dblValue.replace(/ /g, "");
                            dblValue=dblValue.replace(/,/g, ".");
                            return dblValue;
                            break;
                        }
                    }
                }
                else if (parseBoolean(bolIsNumeric)==true)
                {
                    dblValue=dblValue+"";
                    dblValue=dblValue.replace(/,/g, "");
                    //dblValue=dblValue.replace(/,/g, ".");
                    return dblValue;
                }

                return document.getElementById(arguments[intIndex]).value;
            }
            else if (document.getElementById(arguments[intIndex]).type == "hidden")
            {
                if(IsBlockedValue!=null &&IsBlockedValue!=undefined && IsBlockedValue==true)
                {
                   return control.getAttribute("BlockedValue");
                }
                return document.getElementById(arguments[intIndex]).value;
            }
            else if (document.getElementById(arguments[intIndex]).type == "textarea")
            {
                if(IsBlockedValue!=null &&IsBlockedValue!=undefined  && IsBlockedValue==true)
                {
                   return control.getAttribute("BlockedValue");
                }
                return document.getElementById(arguments[intIndex]).value;
            }
            else if (document.getElementById(arguments[intIndex]).type == "password")
            {
                if(IsBlockedValue!=null &&IsBlockedValue!=undefined  && IsBlockedValue==true)
                {
                   return control.getAttribute("BlockedValue");
                }
                return document.getElementById(arguments[intIndex]).value;
            }
            else if (document.getElementById(arguments[intIndex]).type == "checkbox")
            {
                if(IsBlockedValue!=null &&IsBlockedValue!=undefined && IsBlockedValue==true)
                {
                   return control.getAttribute("BlockedValue");
                }
                return document.getElementById(arguments[intIndex]).checked;
            }
            else if (document.getElementById(arguments[intIndex]).type == "radio")
            {
                if(IsBlockedValue!=null &&IsBlockedValue!=undefined && IsBlockedValue==true)
                {
                   return control.getAttribute("BlockedValue");
                }
                return document.getElementById(arguments[intIndex]).checked;
            }
            else if (document.getElementById(arguments[intIndex]).type == "select-one")
            {
                if(IsBlockedValue!=null &&IsBlockedValue!=undefined && IsBlockedValue==true)
                {
                   return control.getAttribute("BlockedValue");
                }
                if (document.getElementById(arguments[intIndex]).selectedIndex == -1)
                {
                    return "";
                }
                else if (document.getElementById(arguments[intIndex]).selectedIndex == 0)
                {
                    return "";
                }
                else
                {
                    return document.getElementById(arguments[intIndex]).options[document.getElementById(arguments[intIndex]).selectedIndex].value;
                }

            }
            else if (document.getElementById(arguments[intIndex]).type == "select-multiple")
            {
                const selectedItems = [];

                    for (let i = 0; i < control.options.length; i++) {
                        const option = control.options[i];
                        if (option.selected) {
                            selectedItems.push(option.value);
                        }
                    }
                return selectedItems;
            }
        }
    }
    return false;
}
function ClearCombo()
{
    try
    {
    if (arguments.length > 0)
    {
        for (var intIndex = 0; intIndex < arguments.length; intIndex++)
        {
            document.getElementById(arguments[intIndex]).selectedIndex =-1;
            document.getElementById(arguments[intIndex]).options.length=0;
//            for(var into=0;into <= document.getElementById(arguments[intIndex]).options.length;into++)
//            {
//                document.getElementById(arguments[intIndex]).remove(into);
//            }
//            if(document.getElementById(arguments[intIndex]).options.length>0)
//            {
//                for(var into=0;into <= document.getElementById(arguments[intIndex]).options.length;into++)
//                {
//                    document.getElementById(arguments[intIndex]).remove(into);
//                }
//            }
            //document.getElementById(id).options.length = 0;
        }

    }
    }catch(ex)
    {}
}

function ClearControls()
{
    var IsBlockedValue=null;
    var bolIsNumeric=null;
   if (arguments.length > 0)
    {
        for (var intIndex = 0; intIndex < arguments.length; intIndex++)
        {
        try
        {
            var control = GetControl(arguments[intIndex]);
            IsBlockedValue = control.getAttribute("IsAccessBlocked");
            IsBlockedValue =  parseBoolean(IsBlockedValue);
            bolIsNumeric = control.getAttribute("IsNumeric");
            if(bolIsNumeric!=null && bolIsNumeric!=undefined && bolIsNumeric==true)
            {
                document.getElementById(arguments[intIndex]).value="0";
            }
            else  if (document.getElementById(arguments[intIndex]).type == "text")
            {
                 document.getElementById(arguments[intIndex]).value="";
            }
            else if (document.getElementById(arguments[intIndex]).type == "hidden")
            {
                document.getElementById(arguments[intIndex]).value="";
            }
            else if (document.getElementById(arguments[intIndex]).type == "file")
            {
                document.getElementById(arguments[intIndex]).value="";
            }
            else if (document.getElementById(arguments[intIndex]).type == "textarea")
            {
                document.getElementById(arguments[intIndex]).value="";
            }
            else if (document.getElementById(arguments[intIndex]).type == "password")
            {
                document.getElementById(arguments[intIndex]).value="";
            }
            else if (document.getElementById(arguments[intIndex]).type == "label")
            {
                document.getElementById(arguments[intIndex]).innerText="";
            }
            else if (document.getElementById(arguments[intIndex]).type == "checkbox")
            {
                  document.getElementById(arguments[intIndex]).checked=false;
            }
            else if (document.getElementById(arguments[intIndex]).type == "radio")
            {
                document.getElementById(arguments[intIndex]).checked=false;
            }
            else if (document.getElementById(arguments[intIndex]).type == "date")
            {
                document.getElementById(arguments[intIndex]).value="";
            }
            
            else if (document.getElementById(arguments[intIndex]).type == "select-one")
            {
                document.getElementById(arguments[intIndex]).value='';
                //document.getElementById(arguments[intIndex]).selectedIndex=0;

            }

            else if (document.getElementById(arguments[intIndex]).type == "select-multiple")
            {
                document.getElementById(arguments[intIndex]).value='';
            }

            }catch(er){}
          
        }
    }
    return false;
}



function removeReadOnly() {
    // Get the control by its ID
    if (arguments.length > 0)
        {
            for (var intIndex = 0; intIndex < arguments.length; intIndex++)
            {
                try
                {
                    const c = arguments[intIndex];
                    const control = document.getElementById(c);
                    
                    // Check if the control exists
                    if (control) {
                        // Remove the readonly property
                        control.readOnly = false; // Or use control.removeAttribute('readonly');
                    } else {
                        console.warn(`Control with ID "${c}" not found.`);
                    }
                }catch(er){}
            }
        }
}

function ResetCombo()
{
    try
    {
    if (arguments.length > 0)
    {
        for (var intIndex = 0; intIndex < arguments.length; intIndex++)
        {
            document.getElementById(arguments[intIndex]).selectedIndex =-1;
            document.getElementById(arguments[intIndex]).options.length=0;
            var optn = document.getElementById(arguments[intIndex]);
            var option = document.createElement("option");
            option.text = "< Select >";
            option.value = "Select";
            if(parent.dhxWins.GetUserLanguageID()!="en")
            {
                 option.text = GetUIErrorMessage("< Select >");
            }

        }

    }
    }catch(ex)
    {}
}

function populateComboHeads(selectbox)
{
    
    var optn = document.getElementById(selectbox);
    var option = document.createElement("option");
    option.text = "< Select >";
    option.value = "Select";
    try {
        optn.add(option, null); //Standard 
    }catch(error) 
    {
        optn.add(option); // IE only
    }

}
function PopulateCustomCombo(cID,cDesc,selectbox)
{

    var optn = document.getElementById(selectbox);
    var optionItem = document.createElement("option");
    optionItem.text = cDesc;
    optionItem.value = cID;

    try {//For FIREFOX
            optn.add(optionItem, null);
        }
    catch (e) {//For IE
            optn.add(optionItem);
        }    
}

function PopulateCombo(jsonstring,selectbox)
{
    var optn = document.getElementById(selectbox);
    var option = document.createElement("option");
    option.text = "< Select >";
    option.value = "Select";
    try {
        optn.add(option, null); //Standard 
    }catch(error) 
    {
        optn.add(option); // IE only
    }
    if(jsonstring!==undefined && jsonstring!=="")
    {
        for (var i = 0 ; i < jsonstring.length ; i++) 
        {
            var optionItem = document.createElement("option");
            optionItem.text = jsonstring[i][1];
            optionItem.value = jsonstring[i][0];

           try {//For FIREFOX
                  optn.add(optionItem, null);
               }
            catch (e) {//For IE
                  optn.add(optionItem);
              }  
        }
    }    
}

function addComboOptions(selectbox, value) {
    var optn = document.getElementById(selectbox);
    var option = document.createElement("option");
    option.text = "--- Select to View ---";
    option.value = "";
    try {
        optn.add(option, null); //Standard 
    } catch (error) {
        optn.add(option); // IE only
    }

    if (value != undefined && value != "") {
        for (var i = 0; i < value.length; i++) {
            var optionItem = document.createElement("option");
            optionItem.text = value[i].Name;
            optionItem.value = value[i].Id;

            try {//For FIREFOX
                optn.add(optionItem, null);
            }
            catch (e) {//For IE
                optn.add(optionItem);
            }
        }
    }

}


function addComboOptionsLowerCase(selectbox, value) {
    var optn = document.getElementById(selectbox);
    var option = document.createElement("option");
    option.text = "--- Select to View ---";
    option.value = "";
    try {
        optn.add(option, null); //Standard 
    } catch (error) {
        optn.add(option); // IE only
    }

    if (value != undefined && value != "") {
        for (var i = 0; i < value.length; i++) {
            var optionItem = document.createElement("option");
            optionItem.text = value[i].name;
            optionItem.value = value[i].id;

            try {//For FIREFOX
                optn.add(optionItem, null);
            }
            catch (e) {//For IE
                optn.add(optionItem);
            }
        }
    }

}

function FullComboReset()
{
    if (arguments.length > 0)
        {
            for (var intIndex = 0; intIndex < arguments.length; intIndex++)
            {
                var combobox =  document.getElementById(arguments[intIndex])
                combobox.innerHTML = "";
                combobox.selectedIndex = -1;
            }
        }
}

function DeleteComboOptions(combo,opts)
{
 try
    {
   var optItems=opts.split(',');
    if (optItems.length > 0)
    {
        for (var intIndex = 0; intIndex < optItems.length; intIndex++)
        {

            for(var into=0;into < document.getElementById(combo).options.length;into++)
            {
                if(document.getElementById(combo).options[into].value.toString().toLowerCase() ==optItems[intIndex].toString().toLowerCase())
                {
                    document.getElementById(combo).remove(into);

                }
            }
        }
    }
    }catch(ex)
    {}
}

function GetControl(ct)
{
    var ctrl = document.getElementById(ct);
    return ctrl;

}

function parseBoolean(value)
{

    if(value=="true" || value=="True" || value=="1" || value==1 || value==true)
    {
        return true;
    }
    else
    {
        return false;
    }
}

function SetControlValue(ctrl,value)
{
    var bolIsInt=false;
    var tmp=GetControl(ctrl);
    if(tmp==null || tmp==undefined)
    {
        return "";
        if(ctrl="txtSupervisedBy")
        {
           tmp=GetControl("txtSupervisedBy")
           if(tmp!=null && tmp!=undefined)
           {
               ctrl=tmp;
           }
        }
    }
    if(value==undefined)
        return "";
            var IsBlockedValue;
            try
            {
                var control = GetControl(ctrl);
                IsBlockedValue = control.getAttribute("IsAccessBlocked");
                IsBlockedValue =  parseBoolean(IsBlockedValue);
                bolIsNumeric = control.getAttribute("IsNumeric");
                bolIsInt = control.getAttribute("IsInt");
                if(parseBoolean(bolIsInt))
                {
                    bolIsNumeric=false;
                }
                if(IsBlockedValue!=null && IsBlockedValue!=undefined && parseBoolean(IsBlockedValue)==true)
                {
                    $(control).attr('BlockedValue',value);
                    if (document.getElementById(ctrl).type == "label")
                    {
                        document.getElementById(ctrl).innerText=GetUIErrorMessage("ACCESS BLOCKED");
                    }
                    else if (document.getElementById(ctrl).type == "checkbox" || document.getElementById(ctrl).type == "radio")
                    {
                        if(value=="True" || value=="true" || value==true)
                        {
                            document.getElementById(ctrl).checked=false;
                        }
                        else
                        {
                          document.getElementById(ctrl).checked=false;
                        }
                    }
                    else
                    {
                        document.getElementById(ctrl).value=GetUIErrorMessage("ACCESS BLOCKED");
                    }
                   //control.getAttribute("BlockedValue");
                   return false;
                }
            }
            catch(e)
            {
            }
            if(parseBoolean(bolIsNumeric)==true && value=="")// && document.getElementById(ctrl).type!="radio" )
            {
                document.getElementById(ctrl).value="0";
                return false;
            }
            var strUserLanguageID="en";
            if (document.getElementById(ctrl).type == "text")
            {

                if(strUserLanguageID!="en" && parseBoolean(bolIsNumeric)==true)
                {
                    // International Numeric Conventions
                    //Danish,Finnish,French,Swedish,Canadian (English and French)    4 294 967 295,000
                    //German 4 294 967.295,000
                    //Italian,Spanish ,Norwegian 4.294.967.295,000
                    //Thai Same as UK,US English
                    document.getElementById(ctrl).value=value;
                    switch(strUserLanguageID)
                    {
                        //4 294 967 295,000
                        case "fr"://French
                        case "da"://Danish
                        case "fi"://Finnish
                        case "sv"://Swedish
                        case "de"://German
                        case "it"://Italin
                        case "sw"://Swahili
                        case "es"://Spanish
                        case "no"://Norwegian
                        {
                            value=value+"";
                            dblValue=ParseNumeric(value);
                            dblValue=dblValue.toLocaleString("fr-FR");

                            document.getElementById(ctrl).value=value;
                            break;
                        }
                    }
                }
                else
                {
                    document.getElementById(ctrl).value=value;
                    if(parseBoolean(bolIsNumeric)==true)
                    {
                        document.getElementById(ctrl).value=addCommas(value);
                    }
                }
            }
            else if (document.getElementById(ctrl).type == "hidden")
            {
                document.getElementById(ctrl).value=value;
            }
            else if (document.getElementById(ctrl).type == "date")
            {
                document.getElementById(ctrl).value=value;
            }
            else if (document.getElementById(ctrl).type == "textarea")
            {
                document.getElementById(ctrl).value=value;
            }
            else if (document.getElementById(ctrl).type == "password")
            {
                document.getElementById(ctrl).value=value;
            }
            else if (document.getElementById(ctrl).type == "label")
            {
                document.getElementById(ctrl).innerText=value;
            }
            else if (document.getElementById(ctrl).type == "checkbox")
            {
                if(value=="True" || value=="true" || value==true)
                {
                    document.getElementById(ctrl).checked=true;
                }
                else
                {
                  document.getElementById(ctrl).checked=false;
                }
            }
            else if (document.getElementById(ctrl).type == "radio")
            {
                if(value=="True" || value=="true" || value==true)
                {
                    document.getElementById(ctrl).checked=true;
                }
                else
                {
                  document.getElementById(ctrl).checked=false;
                }
            }
            else if (document.getElementById(ctrl).type == "select-one")
            {
                document.getElementById(ctrl).value=value;

            }
            else if (document.getElementById(ctrl).type == "select-multiple")
            {
                var selectElement = document.getElementById(ctrl);
                for (var i = 0; i < selectElement.options.length; i++) {
                    selectElement.options[i].selected = value.includes(selectElement.options[i].value);
                }
            }

    return false;
}

function clearAllControls(AnyAction) {
    // Get all form elements
    var formElements = document.querySelectorAll('form *');
    // If AnyAction is true, clear all controls
    // Loop through the form elements
    for (var i = 0; i < formElements.length; i++) {
      var element = formElements[i];
  
      // Check the type of the form element
      switch (element.type) {
        case 'text':
        case 'password':
        case 'textarea':
          // Clear the value of text-based controls
          element.value = '';
          break;
        case 'checkbox':
        case 'radio':
          // Uncheck checkbox and radio buttons
          element.checked = false;
          break;
        case 'select-one':
        case 'select-multiple':
          // Reset the selected options
          element.selectedIndex = 0;
          break;
        default:
          // Do nothing for other types of controls
          break;
      }
    }

    SetControlValue("hdnActionTag", AnyAction);

    if(AnyAction === "AddNew")
    {
        const btnSupervise = document.getElementById('btnSupervise');
        const btnDelete = document.getElementById('btnDelete');
        const btnUpdate = document.getElementById('btnUpdate');

        if (btnSupervise) btnSupervise.style.display = 'block'; 
        if (btnDelete) btnDelete.style.display = 'block'; 
        if (btnUpdate) btnUpdate.style.display = 'block'; 

        if (btnSupervise) {
            btnSupervise.style.display = 'none';

        }
        if (btnDelete) {
            btnDelete.style.display = 'none';

        }
    }

  }

  function ViewGlobal(ActionTag,Id)
  {
    const btnSupervise = document.getElementById('btnSupervise');
    const btnDelete = document.getElementById('btnDelete');
    const btnUpdate = document.getElementById('btnUpdate');

    if (btnSupervise) btnSupervise.style.display = 'block'; 
    if (btnDelete) btnDelete.style.display = 'block'; 
    if (btnUpdate) btnUpdate.style.display = 'block'; 

    var hiddenModuleId = GetInputValue("hdnId");

    ViewDataDetailsById(hiddenModuleId,Id);

    if(ActionTag === "ViewData")
    {
        clearAllControls("ViewData");

        if (btnSupervise) {
            btnSupervise.style.display = 'none';

        }

        if (btnDelete) {
            btnDelete.style.display = 'none';

        }

        if (btnUpdate) {
            btnUpdate.style.display = 'none';

        }

    }else if(ActionTag === "ViewEditData")
    {
        clearAllControls("ViewEditData");
        if (btnSupervise) {
            btnSupervise.style.display = 'none';

        }

        if (btnDelete) {
            btnDelete.style.display = 'none';

        }

        
    }else if(ActionTag === "ViewDeleteData")
    {
        clearAllControls("ViewDeleteData");
        if (btnSupervise) {
            btnSupervise.style.display = 'none';

        }
        if (btnUpdate) {
            btnUpdate.style.display = 'none';

        }

    }
    else if(ActionTag === "ViewSuperviseData")
    {
        clearAllControls("ViewSuperviseData");
        if (btnDelete) {
            btnDelete.style.display = 'none';

        }
        if (btnUpdate) {
            btnUpdate.style.display = 'none';

        }
        

    }
        
  }

  function ViewDataDetailsById(ModuleId,value)
{
    clearAllControls();
    LoadCollabInfo('Loading....');

    //Load Controls and Current Rights
    //var ModuleId = GetInputValue("hdnId");
    var csrf = GetInputValue("hdncsrf");


    jQuery.ajax({
    type : "POST",
    url: "/module/"+ModuleId+"/",
    data: {
        FormId: ModuleId,
		Id: value,
		ActionID: "viewData",
        csrfmiddlewaretoken: csrf,
        dataType: "json",

    },
        success: function(response)
        {
            if(response!=="[]" && response!=="")
            {

                var jSonSession= response.returnDetails;
                myControls = response.returnFormDetails;
                if(jSonSession!=="")
                {

                    for (var j = 0; j < response.returnFormDetails.length; j++) {
                        {
                            try {
                                ControlName=response.returnFormDetails[j].columnname;
                                var ControlNameLower =  ControlName.toLowerCase();
                                SetControlValue(ControlName,eval('jSonSession[0].'+ControlNameLower));
                                
                            } catch (error) {
                        
                            }
                        }
                    
                    
                    
                    }
                    LoadCollabInfo('Data Loaded.');
                }
                
            }else
            {
                LoadCollabError(request.responseText);
            }
        },
        error: function (request, status, error) {
            LoadCollabError(request.responseText);
        }
    });
}

  

function DisableControl()
{
   if (arguments.length > 0)
    {
        for (var intIndex = 0; intIndex < arguments.length; intIndex++)
        {
            if(document.getElementById(arguments[intIndex])!=null)
            {
                if (document.getElementById(arguments[intIndex]).type == "text")
                {
                    //document.getElementById(arguments[intIndex]).disabled = true;
                    document.getElementById(arguments[intIndex]).readOnly=true;
                    SetUpperCase(arguments[intIndex]);
                }
                else if (document.getElementById(arguments[intIndex]).type == "password")
                {
                    //document.getElementById(arguments[intIndex]).disabled = true;
                    document.getElementById(arguments[intIndex]).readOnly=true;
                    SetUpperCase(arguments[intIndex]);
                }
                else
                {
                    document.getElementById(arguments[intIndex]).disabled = true;
                }

            }
            else
            {

            }
        }
    }
    return false;
}


function EnableControl()
{
   if (arguments.length > 0)
    {
        for (var intIndex = 0; intIndex < arguments.length; intIndex++)
        {
            if(document.getElementById(arguments[intIndex])!=null)
            {
                ///document.getElementById(arguments[intIndex]).disabled = false;
                if (document.getElementById(arguments[intIndex]).type == "text")
                {
                    //document.getElementById(arguments[intIndex]).disabled = false
                    document.getElementById(arguments[intIndex]).readOnly=false;
                    SetUpperCase(arguments[intIndex]);
                }
                else
                {
                    document.getElementById(arguments[intIndex]).disabled = false;
                    document.getElementById(arguments[intIndex]).readOnly=false;
                }
            
            }
            else
            {

            }
        }
    }
    return false;
}


function get_browser()
{
    var N = navigator.appName, ua = navigator.userAgent, tem;
    var M = ua.match(/(opera|chrome|safari|firefox|msie)\/?\s*(\.?\d+(\.\d+)*)/i);
    if (M && (tem = ua.match(/version\/([\.\d]+)/i)) != null) M[2] = tem[1];
    M = M ? [M[1], M[2]] : [N, navigator.appVersion, '-?'];
    return M[0];
}
function get_browser_version()
{
    var N = navigator.appName, ua = navigator.userAgent, tem;
    var M = ua.match(/(opera|chrome|safari|firefox|msie)\/?\s*(\.?\d+(\.\d+)*)/i);
    if (M && (tem = ua.match(/version\/([\.\d]+)/i)) != null) M[2] = tem[1];
    M = M ? [M[1], M[2]] : [N, navigator.appVersion, '-?'];
    return M[1];
}

function setCookie(name, value, days) {
    const d = new Date();
    d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000)); // Set expiration time
    const expires = "expires=" + d.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

// Function to get a cookie by name
function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}


 // Function to get a cookie by name
function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// Retrieve the JSON array from the cookie
const storedJson = getCookie('mainMenu');
if (storedJson) {
    const parsedArray = JSON.parse(storedJson);
    const modulesMenu = document.getElementById('modules-menu');

    // Group modules by modulegroup
    const groupedModules = parsedArray.reduce((acc, module) => {
        if (!acc[module.modulegroup]) {
            acc[module.modulegroup] = [];
        }
        acc[module.modulegroup].push(module);
        return acc;
    }, {});

    // Create menu items for each module group
    for (const group in groupedModules) {
        const menuItem = document.createElement('div');
        menuItem.className = 'menu-item has-sub';
        menuItem.innerHTML = `
            <a href="javascript:;" class="menu-link">
                <div class="menu-icon">
                    <i class="bi bi-bag-check"></i>
                    <span class="w-5px h-5px rounded-3 bg-theme position-absolute top-0 end-0 mt-3px me-3px"></span>
                </div>
                <div class="menu-text d-flex align-items-center">${group}</div>
                <span class="menu-caret"><b class="caret"></b></span>
            </a>
            <div class="menu-submenu" style="display: none;">
                ${groupedModules[group].map(module => `
                    <div class="menu-item">
                        <a href="/module/${module.id}"} class="menu-link">
                            <div class="menu-text">${module.modulename}</div>
                        </a>
                    </div>
                `).join('')}
            </div>
        `;
        modulesMenu.appendChild(menuItem);
    }
}

// Toggle submenu visibility on click
document.addEventListener('click', function (e) {
    if (e.target.closest('.menu-item.has-sub')) {
        const submenu = e.target.closest('.menu-item.has-sub').querySelector('.menu-submenu');
        if (submenu) {
            submenu.style.display = submenu.style.display === 'none' ? 'block' : 'none';
        }
    }
});


function isGlobalValid()
{
	var dataValid=true;
    populateControls('myForm');

    for (var j = 0; j < myControls.length; j++) 
    {
        try {
            ControlName=myControls[j].columnname;
            let control = document.getElementById(ControlName);

            if (control.required) {
                // Check if the control has a value
                if (control.value.trim() === '') {
                    // If the control is required and has no value, mark the form as invalid
                    dataValid = false;
                    LoadCollabInfo(ControlName+" not provided!");
                    // Add an error class to the control
                } 
            }

        } catch (error) {
    
        }
    }
    

    return dataValid;
}

// Function to read form controls and populate the myControls array
function populateControls(formId) {
    myControls = [];
    // Get the form element
    const form = document.getElementById(formId);
    
    // Check if the form exists
    if (form) {
        // Loop through the form elements
        for (let i = 0; i < form.elements.length; i++) {
            const control = form.elements[i];

            // Check if the control is an input, select, or textarea
            if (control.tagName === 'INPUT' || control.tagName === 'SELECT' || control.tagName === 'TEXTAREA') {
                // Add the control to the myControls array with its column name
                myControls.push({
                    columnname: control.id, // Assuming the ID is used as the column name
                    required: control.required // Store the required property
                });
            }
        }
    } else {
        console.warn(`Form with ID "${formId}" not found.`);
    }
}


function btnGlobalMainUpdateID()
{
    var ModuleId = GetInputValue("hdnId");
    var ActionTag = GetInputValue("hdnActionTag");
    var csrf = GetInputValue("hdncsrf");

    if (isGlobalValid()===true) {
        //DisableControl('btnUpdate');

        $.ajax({
        type : "POST",
        url: "/module/"+ModuleId+"/",
        data: $("form").serialize()+'&ActionID='+ActionTag+'&ModuleId='+ModuleId,
            success: function(response) {
            if(response!=="[]" && response!=="") {
                var jSonSessionData= response.returnDetails;
                LoadCollabSuccess('Information updated successfully!');
                //btnCloseID();
                location.reload();
            }else {
                LoadCollabSuccess('Information updated successfully!');
                }
            },
                error: function (request, status, error) {
                LoadCollabError(request.responseText);
                //EnableControl('btnUpdate');
            }
        });
	}
}

function btnGlobalMainSuperviseID()
{
    var ModuleId = GetInputValue("hdnId");
    var ActionTag = GetInputValue("hdnActionTag");
    var csrf = GetInputValue("hdncsrf");

    if (isGlobalValid()===true) {
        //DisableControl('btnUpdate');

        $.ajax({
        type : "POST",
        url: "/module/"+ModuleId+"/",
        data: $("form").serialize()+'&ActionID='+ActionTag+'&ModuleId='+ModuleId,
            success: function(response) {
            if(response!=="[]" && response!=="") {
                var jSonSessionData= response.returnDetails;
                LoadCollabSuccess('Information updated successfully!');
                //btnCloseID();
                location.reload();
            }else {
                LoadCollabSuccess('Information updated successfully!');
                }
            },
                error: function (request, status, error) {
                LoadCollabError(request.responseText);
                //EnableControl('btnUpdate');
            }
        });
	}
}