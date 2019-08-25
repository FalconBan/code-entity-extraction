from code_data_extractor import class_data_holder

class python_class_data_holder(class_data_holder):
    class_name = ''
    definitions = {}
    members = []

    def __init__(self, class_name):
        self.class_name = class_name

    def add_method(self, method_name, args, types):
        is_string = isinstance(method_name, str)
        if (is_string):
            self.definitions[method_name] = [args, types]
            return True
        else:
            return False

    def add_memeber(self, member_name):
        self.members.append(member_name)