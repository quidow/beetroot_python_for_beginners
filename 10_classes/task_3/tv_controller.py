class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.current = channels[0]

    def first_channel(self):
        self.current = self.channels[0]
        return self.current

    def last_channel(self):
        self.current = self.channels[-1]
        return self.current

    def turn_channel(self, channel):
        if type(channel) is not int:
            raise ValueError
        if channel > len(self.channels):
            self.current = self.channels[-1]
        elif channel <= 0:
            self.current = self.channels[-1]
        else:
            self.current = self.channels[channel - 1]
        return self.current

    def next_channel(self):
        current_index = self.channels.index(self.current) + 1
        if current_index < len(self.channels):
            self.current = self.channels[current_index]
        else:
            self.current = self.channels[0]
        return self.current

    def previous_channel(self):
        current_index = self.channels.index(self.current) - 1
        if current_index < 0:
            self.current = self.channels[-1]
        else:
            self.current = self.channels[current_index]
        return self.current

    def current_channel(self):
        return self.current

    def is_exist(self, channel):
        if type(channel) is int:
            if channel < len(self.channels):
                return "Yes"
            else:
                return "No"
        elif type(channel) is str:
            if channel in self.channels:
                return "Yes"
            else:
                return "No"
        else:
            raise ValueError
