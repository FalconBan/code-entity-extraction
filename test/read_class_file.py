from python_data_extractor import entity_extractor as e_e
import re

if __name__ == "__main__":
    file = open('../test_data/a3c_cartpole.py', 'r+')
    lines = file.readlines()
    extractor = e_e.class_data_extractor()

    for line in lines:
        result = extractor.class_extractor(line)
        result_2 = extractor.method_extractor(line)
        if (result_2):
            print(result_2, "\n")