from python_data_extractor import entity_extractor
import re

if __name__ == "__main__":
    file = open('../test_data/a3c_cartpole.py', 'r+')
    lines = file.readlines()

    for line in lines:
        result = entity_extractor.class_extractor(line)
        result_2 = entity_extractor.method_extractor(line)
        if (result_2):
            print(result_2, "\n")