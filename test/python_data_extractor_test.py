from python_data_extractor import entity_extractor as e_e

if __name__ == "__main__":
    function_name = "def new_function(first, second_2):"
    result = e_e.method_extractor(function_name)
    print(result)

    class_name = "class  this_class(other):\n\tbell=FALSE"
    extractor = e_e.class_data_extractor()
    result = extractor.class_extractor(class_name)
    print(result)