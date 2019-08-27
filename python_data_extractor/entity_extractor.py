import re
from . import class_data_holder

class class_data_extractor:
    entered_class = False
    member_declaration = False
    cls_dat_holder = None

    def extract_class_data(self, string):
        if not self.entered_class:
            possible_class = self.class_extractor(string)
            return possible_class
        elif self.member_declaration:
            if "def" in string:
                self.member_declaration = False
                self.method_extractor(string)
            else:
                self.member_extractor(string)
        else:
            self.method_extractor(string)

    def class_extractor(self, class_name_str):
        # string_vals is a list of string tokens
        if "class " in class_name_str:
            self.entered_class = True
            self.member_declaration = True
            found = re.findall("[\w.]+", class_name_str)
            found.remove("class")
            self.cls_dat_holder = class_data_holder.python_class_data_holder(found[0])
            self.cls_dat_holder.add_base_calsses(found[1:])
            return [True, found[0], found[1:]]
        else:
            return None

    def member_extractor(self, string):
        self.cls_dat_holder.add_member(string)

    def method_extractor(self, function_name_str):
        # string_vals is a list of string tokens
        if "def " in function_name_str:
            found = re.findall("\w+", function_name_str)
            found.remove("def")
            return [True, found[0], found[1:]]