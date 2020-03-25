"""
TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

- first_channel() - turns on the first channel from the list.
- last_channel() - turns on the last channel from the list.
- turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
- next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
- previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
- current_channel() - returns the name of the current channel.
- is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
  exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    pass

controller = TVController(CHANNELS)



controller.first_channel() == "BBC"

controller.last_channel() == "TV1000"

controller.turn_channel(1) == "BBC"

controller.next_channel() == "Discovery"

controller.previous_channel() == "BBC"

controller.current_channel() == "BBC"

controller.is_exist(4) == "No"

controller.is_exist("BBC") == "Yes"
"""


class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.current = channels[0]

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, channel):
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


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

if (
    controller.first_channel() == "BBC"
    and controller.last_channel() == "TV1000"
    and controller.turn_channel(1) == "BBC"
    and controller.next_channel() == "Discovery"
    and controller.previous_channel() == "BBC"
    and controller.current_channel() == "BBC"
    and controller.is_exist(4) == "No"
    and controller.is_exist("BBC") == "Yes"
):
    print("TVController works!")
else:
    print("TVController doesnt work!")

