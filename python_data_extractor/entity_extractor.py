import re

def method_extractor(function_name_str):
    #string_vals is a list of string tokens
    if "def " in function_name_str:
        found = re.findall("\w+", function_name_str)
        found.remove("def")
        return [True, found[0], found[1:]]

class class_data_extractor:
    entered_class = False

    def class_extractor(self, class_name_str):
        # string_vals is a list of string tokens
        if "class " in class_name_str:
            self.entered_class = True
            found = re.findall("[\w.]+", class_name_str)
            found.remove("class")
            return [True, found[0], found[1:]]


