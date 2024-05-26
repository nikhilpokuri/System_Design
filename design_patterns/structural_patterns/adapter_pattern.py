from abc import ABC, abstractmethod

class DataReader(ABC):
    @abstractmethod
    def read_data(self, path):
        pass

# Adaptees = [JSONReader, XMLReader, CSVReader]
class JSONReader:
    def read_json(self, path):
        return f'Reading data from JSON file at {path}'

class XMLReader:
    def read_xml(self, path):
        return f'Reading data from XML file at {path}'

class CSVReader:
    def read_csv(self, path):
        return f'Reading data from CSV file at {path}'

#Adapter
class DataReaderAdapter(DataReader):
    def __init__(self, adaptee, file_type) -> None:
        self.adaptee = adaptee
        self.file_type = file_type
        self.__reader = {'json': JSONReader().read_json,
                        'xml': XMLReader().read_xml, 
                        'csv': CSVReader().read_csv
                        }

    def read_data(self, file_path):
        if self.file_type in self.__reader:
            return self.__reader[self.file_type](file_path)

#client
def load_data(reader:object, file_type, file_path):
    adapter = DataReaderAdapter(reader, file_type)
    return adapter.read_data(file_path)

print(load_data(JSONReader(), 'json', 'pre_weather_report.json'))
print(load_data(XMLReader(), 'xml', 'post_weather_report_.xml'))
print(load_data(CSVReader(), 'csv', 'floods_report.csv'))