import copy


class TempUserData:
    def __init__(self):
        super(TempUserData, self).__init__()
        self.__user_data = {}
        self.__default = [False]

    def temp_data(self, user_id):
        if user_id not in self.__user_data.keys():
            self.__user_data.update({user_id: [False]})  # status, lang, main_question, counter_of_sub_quests, answers
        return self.__user_data