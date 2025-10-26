
class Report:

    def __init__(self, summary, urgency_level, submitted_by):
        self.__summary = summary
        self.__urgency_level = urgency_level
        self.__submitted_by = submitted_by

    def set_summary(self, summary):
        self.__summary = summary

    def set_urgency_level(self, urgency_level):
        self.__urgency_level = urgency_level

    def set_submitted_by(self, submitted_by):
        self.__submitted_by = submitted_by

    def get_summary(self):
        return self.__summary

    def get_urgency_level(self):
        return self.__urgency_level

    def get_submitted_by(self):
        return self.__submitted_by

