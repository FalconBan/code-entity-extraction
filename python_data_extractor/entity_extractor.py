import re

def method_extractor(function_name_str):
    #string_vals is a list of string tokens
    if "def " in function_name_str:
        found = re.findall("\w+", function_name_str)
        found.remove("def")
        return [True, found[0], found[1:]]

def class_extractor(class_name_str):
    #string_vals is a list of string tokens
    if "class " in class_name_str:
        found = re.findall("[\w.]+", class_name_str)
        found.remove("class")
        return [True, found[0], found[1:]]

