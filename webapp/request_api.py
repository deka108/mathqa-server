"""
# Name:           webapp/request_api.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   N.A
# Last Modified:  Nov 21 2016
# Modified by:    Phuc Le-Sanh
"""
from django.db import connection
import requests


def get(http_url, user_id):
    headers = {
        'Authorization': __auth_token(user_id)
    }
    r = requests.get(http_url, headers=headers)

    return r.json()


def post(http_url, user_id, json_data):
    headers = {
        'Authorization': __auth_token(user_id)
    }
    r = requests.post(http_url, headers=headers, data=json_data)

    return r.json()


def __auth_token(user_id):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM authtoken_token WHERE user_id = %s',
                   str(user_id))
    return 'Token ' + cursor.fetchone()[0]
