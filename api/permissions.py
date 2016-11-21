"""
# Name:           api/permissions.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   N.A
# Last Modified:  Nov 21 2016
# Modified by:    Phuc Le-Sanh
"""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
