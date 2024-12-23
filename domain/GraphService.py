import requests

from data.GraphAPI import GraphAPI


class GraphService(GraphAPI):

    def proccess_action(self, event, args):
        try:
            if event == "CompleteRegistration":
                response = self._complete_registration(args)
            elif event == "Purchase":
                response = self._purchase(args)
            else:
                response = self._lead(args)

            response_data = response.json()  # Перетворюємо відповідь у JSON

            # Перевіряємо статус відповіді
            if response.status_code == 200:
                if response_data.get("events_received", 0) > 0:
                    print("Event successfully sent!")
                    return {"status": "success", "details": response_data}
                else:
                    print("Event sent but not processed!")
                    return {"status": "warning", "details": response_data}
            else:
                print(f"Error Event: {response_data.get('error', {}).get('message', 'Unknown error')}")
                return {"status": "error", "details": response_data}

        except Exception as e:
            print(f"Event Request failed: {e}")
            return {"status": "error", "details": str(e)}

