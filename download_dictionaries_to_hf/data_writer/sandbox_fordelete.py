import sys
print(sys.path)
print(__package__)


from .parser import CsvIoParser


with open('sandbox_data_fordelete.csv') as file:
    CsvIoParser(file)
