from rest_framework.permissions import BasePermission

class IsCanndidateUser(BasePermission):
    def has_permission(self,request,view):
        user = request.user
        user_type = User.objects.get(id=user.id).user_type

        return user_type.user_type == "candidate"
