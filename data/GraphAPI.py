import json

import requests


class GraphAPI:
    def __init__(self):
        self.__headers = {'Content-Type': 'application/json'}

    def _lead(self, args):
        url = f"https://graph.facebook.com/v21.0/{args['pixel']}/events?access_token={args['token']}"

        payload = json.dumps({
            "data": [
                {
                    "event_name": "Lead",
                    "event_time": f"{args['event_time']}",
                    "event_id": f"{args['event_id']}",
                    "action_source": "website",
                    "user_data": {
                        "client_ip_address": f"{args['client_ip']}",
                        "client_user_agent": f"{args['user_agent']}",
                        "fbc": f"fb.1.{args['event_time']}.{args['fbclid']}",
                        "fbp": f"fb.1.{args['event_time']}.{args['random_num']}"
                    }
                }
            ]
        })

        return requests.request("POST", url, headers=self.__headers, data=payload)

    def _complete_registration(self, args: dict[str]):
        url = f"https://graph.facebook.com/v21.0/{args['pixel']}/events?access_token={args['token']}"

        payload = json.dumps({
            "data": [
                {
                    "event_name": "CompleteRegistration",
                    "event_time": f"{args['event_time']}",
                    "event_id": f"{args['event_id']}",
                    "action_source": "website",
                    "user_data": {
                        "client_ip_address": f"{args['client_ip']}",
                        "client_user_agent": f"{args['user_agent']}",
                        "fbc": f"fb.1.{args['event_time']}.{args['fbclid']}",
                        "fbp": f"fb.1.{args['event_time']}.{args['random_num']}"
                    }
                }
            ]
        })

        return requests.request("POST", url, headers=self.__headers, data=payload)

    def _purchase(self, args):
        url = f"https://graph.facebook.com/v21.0/{args['pixel']}/events?access_token={args['token']}"

        payload = json.dumps({
            "data": [
                {
                    "event_name": "Purchase",
                    "event_time": f"{args['event_time']}",
                    "event_id": f"{args['event_id']}",
                    "action_source": "website",
                    "user_data": {
                        "client_ip_address": f"{args['client_ip']}",
                        "client_user_agent": f"{args['user_agent']}",
                        "fbc": f"fb.1.{args['event_time']}.{args['fbclid']}",
                        "fbp": f"fb.1.{args['event_time']}.{args['random_num']}"
                    },
                    "custom_data": {
                        "value": f"{args['amount_value']}",
                        "currency": "USD"
                    }
                }
            ]
        })

        return requests.request("POST", url, headers=self.__headers, data=payload)
