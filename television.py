class Television:
    """
    Television class simulates basic TV remote functionality.
    Such as, power on/off, channel control, volume control, and mute.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self) -> None:
        """
        Constructor. Initializes the television with power off, volume at MIN_VOLUME,
        channel at MIN_CHANNEL, and unmuted.
        """
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to power on or off.
        """
        self.__status = not self.__status

    def mute(self):
        """
        Method to mute or unmute.
        """
        if self.__status:
            self.__muted = not self.__muted


    def channel_up(self) -> None:
        """
        Method to increase the tv channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status
        """
        if self.__status:
            volume_display = 0 if self.__muted else self.__volume
            return f'Power = True, Channel = {self.__channel}, Volume = {volume_display}'
        else:
            return f'Power = False, Channel = {self.__channel}, Volume = {self.__volume}'

