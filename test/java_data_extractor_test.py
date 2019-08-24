from java_data_extractor import entity_extractor

if __name__ == "__main__":
    function_name = "void new_function(int second_2)"
    result = entity_extractor.method_extractor(function_name)
    print(result[1].group(0))

    class_name = "class  this_class"
    result = entity_extractor.class_extractor(class_name)
    print(result)