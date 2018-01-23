from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profiles"""

    def has_object_permissions(self,request,view,obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id

class PostOwnStatus(permissions.BasePermission):
    """allow user to post status own"""


    def has_object_permission(self,request,view,obj):
        """checks the user is trying to update their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id==request.user.id
