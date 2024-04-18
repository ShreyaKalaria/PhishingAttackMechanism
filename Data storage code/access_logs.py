class AccessLogs:
    def __init__(self):
        self.logs = []

    def record_access_timestamp(self):
        self.logs.append({"timestamp": getting_current_timestamp()})

    def record_attacker_ip(self, ip_of_attacker):
        self.logs.append({"ip_of_attacker": ip_of_attacker})

    def record_data_retrieved(self, data):
        self.logs.append({"data_retrieved": data})
