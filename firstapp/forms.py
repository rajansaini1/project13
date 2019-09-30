from django import forms
from firstapp.models import SiteUser,UserRole,UserPhoto
class SiteUserForm(forms.ModelForm):
    class Meta():
        model=SiteUser
        exclude=["roleid",
                 "userFullName",
                 "userEmail",
                 "userPassword",
                 "userMobile",
                 "isActive",
                ]


class UserRoleForm(forms.ModelForm):
    class Meta():
        model = UserRole
        exclude = ["roleid",
                   "rolename",
                   "isActive",


                  ]

class UserPhotoForm(forms.ModelForm):
    class Meta():
        model = UserPhoto
        exclude = ["roleid",
            "userFullName",
            "userEmail",
            "userPassword",
            "userMobile",
             "photo",
              "isActive",
          ]

