
function btnLogin()
{

    if(GetInputValue("BranchId")==='')
    {
        LoadCollabError('Branch ID Not Provided');
        return false;
    }

    if(GetInputValue("UserEmai")==='')
    {
        LoadCollabError('User Email Not Provided');
        return false;
    }

    if(GetInputValue("Password")==='')
    {
        LoadCollabError('Password Not Provided');
        return false;
    }


    $.ajax({
        type : "POST",
        url: "/Commons/",
        data: $("form").serialize()+'&ActionID='+'LoginUser',
            success: function(response) {
            if(response!=="[]" && response!=="") {

                var login_status = response.login_status;

                if(login_status == 'invalid')
                {
                    LoadCollabError('invalid username/password!');
                }else {
                    var MainModuleIds="";
                    var MainModuleNames="";
                    var MainModules=response.mainMenu;
                    var Notifications=response.Notifications['Notification'];;
                    var Names= response.SystemUser['Name'];

                    

                    setCookie("mainMenu", JSON.stringify(MainModules), 7);
                    setCookie("Notifications", Notifications, 7);
                    setCookie("Names", Names, 7);


                    LoadCollabInfo('Welcome to Plutus Core!');
                    window.location.href = '/home/';
                }
            }
        }
    });
}