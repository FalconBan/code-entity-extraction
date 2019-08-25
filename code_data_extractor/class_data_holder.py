class class_data_holder:
    class_name = ''
    definitions = {}
    members = []

    def __init__(self, class_name):
        self.class_name = class_name

    def add_method(self, method_name, args, types):
        return False

    def add_memeber(self, member_name):
        self.members.append(member_name)