from python_data_extractor import entity_extractor

if __name__ == "__main__":
    function_name = "def new_function(first, second_2):"
    result = entity_extractor.method_extractor(function_name)
    print(result)

    class_name = "class  this_class(other):\n\tbell=FALSE"
    result = entity_extractor.class_extractor(class_name)
    print(result)