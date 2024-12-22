import json

import requests


class GraphAPI:
    def __init__(self):
        self.__headers = {'Content-Type': 'application/json'}

    def _lead(self, pixel, token, fbclid, client_ip, user_agent, event_time, event_id, random_num):
        url = f"https://graph.facebook.com/v21.0/{pixel}/events?access_token={token}"

        payload = json.dumps({
            "data": [
                {
                    "event_name": "Lead",
                    "event_time": f"{event_time}",
                    "event_id": f"{event_id}",
                    "action_source": "website",
                    "user_data": {
                        "client_ip_address": f"{client_ip}",
                        "client_user_agent": f"{user_agent}",
                        "fbc": f"fb.1.{event_time}.{fbclid}",
                        "fbp": f"fb.1.{event_time}.{random_num}"
                    }
                }
            ]
        })

        return requests.request("POST", url, headers=self.__headers, data=payload)

    def _complete_registration(self, pixel, token, fbclid, client_ip, user_agent, event_time, event_id, random_num):
        url = f"https://graph.facebook.com/v21.0/{pixel}/events?access_token={token}"

        payload = json.dumps({
            "data": [
                {
                    "event_name": "CompleteRegistration",
                    "event_time": f"{event_time}",
                    "event_id": f"{event_id}",
                    "action_source": "website",
                    "user_data": {
                        "client_ip_address": f"{client_ip}",
                        "client_user_agent": f"{user_agent}",
                        "fbc": f"fb.1.{event_time}.{fbclid}",
                        "fbp": f"fb.1.{event_time}.{random_num}"
                    }
                }
            ]
        })

        return requests.request("POST", url, headers=self.__headers, data=payload)

    def _purchase(self, pixel, token, fbclid, client_ip, user_agent, event_time, event_id, random_num, amount_value):
        url = f"https://graph.facebook.com/v21.0/{pixel}/events?access_token={token}"

        payload = json.dumps({
            "data": [
                {
                    "event_name": "Purchase",
                    "event_time": f"{event_time}",
                    "event_id": f"{event_id}",
                    "action_source": "website",
                    "user_data": {
                        "client_ip_address": f"{client_ip}",
                        "client_user_agent": f"{user_agent}",
                        "fbc": f"fb.1.{event_time}.{fbclid}",
                        "fbp": f"fb.1.{event_time}.{random_num}"
                    },
                    "custom_data": {
                        "value": f"{amount_value}",
                        "currency": "USD"
                    }
                }
            ]
        })

        return requests.request("POST", url, headers=self.__headers, data=payload)
