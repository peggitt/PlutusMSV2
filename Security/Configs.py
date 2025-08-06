ENDPOINTEnvironment =  "_Development"
from Security.models import SystemUser

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def GetSuperUserRole(PassUserId):
    # Get the user ID based on the provided email
    Uid = SystemUser.objects.filter(UserEmail=PassUserId).values_list('id', flat=True).first()
    
    if Uid is not None:
        # Get the user role using the user ID
        userRole = SystemUser.objects.filter(id=Uid).values('SuperAdminUser').first()

        if userRole is not None:
            return userRole
        else:
            return None  # Handle case where user role is not found    
    else:
        return None  # Handle case where user is not found
