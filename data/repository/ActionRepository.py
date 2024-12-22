from data.DataBaseHelp import DataBaseHelp


class ActionRepository(DataBaseHelp):

    def insert_action(self, action_type, status, details, pixel, fbclid,
                      client_ip, user_agent, event_time, event_id, random_num, currency, amount_value):
        query = ("INSERT INTO `actions` ("
                 "action_type, status, details, pixel, fbclid, "
                 "client_ip, user_agent, event_time, event_id, random_num, currency, amount_value"
                 ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")
        return self._insert(query, (action_type, status, details, pixel, fbclid,
                                    client_ip, user_agent, event_time, event_id, random_num, currency, amount_value))
