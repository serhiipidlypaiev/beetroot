CHANNELS = ["Discovery", "BBC", "TV1000"]
DICT_CHANNELS = dict(enumerate(CHANNELS, start=1))
CHENNEL = DICT_CHANNELS.get(1)
CHENNEL_NUMBER = 1


class ConrollerTV:
    def __init__(self, channels=list) -> None:
        pass

    def first_channel():
        global CHENNEL, CHENNEL_NUMBER
        CHENNEL = DICT_CHANNELS.get(1)
        CHENNEL_NUMBER = 1
        return CHENNEL

    def last_channel():
        global CHENNEL, CHENNEL_NUMBER
        CHENNEL_NUMBER = list(DICT_CHANNELS.keys())[-1]
        CHENNEL = DICT_CHANNELS.get(CHENNEL_NUMBER)
        return CHENNEL

    def turn_channel(self, n):
        global CHENNEL, CHENNEL_NUMBER
        CHENNEL = DICT_CHANNELS.get(n)
        CHENNEL_NUMBER = n
        return CHENNEL

    def next_channel():
        global CHENNEL, CHENNEL_NUMBER
        CHENNEL_NUMBER = CHENNEL_NUMBER + 1
        CHENNEL = DICT_CHANNELS.get(CHENNEL_NUMBER)
        return CHENNEL

    def previous_channel():
        global CHENNEL, CHENNEL_NUMBER
        CHENNEL_NUMBER = CHENNEL_NUMBER - 1
        CHENNEL = DICT_CHANNELS.get(CHENNEL_NUMBER)
        return CHENNEL

    def current_channel():
        global CHENNEL
        return CHENNEL

    def controller_is_exist(self, chennel):
        for i, k in DICT_CHANNELS.items():
            if i == chennel or k == chennel:
                return "Yes"
        return "No"
