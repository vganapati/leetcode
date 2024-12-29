class Logger:
    def __init__(self):
        self.message_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.message_dict.keys():
            timestamp_prev = self.message_dict[message]
            if (timestamp - timestamp_prev) >= 10:
                self.message_dict[message] = timestamp
                return True
            else:
                return False
        else:
            self.message_dict[message] = timestamp
            return True