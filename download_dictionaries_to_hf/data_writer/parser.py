import abc
import csv
import logging
from .errors import NotCsvFormatError, UnexpectedCsvDelimiterError


logger = logging.getLogger(__name__)


class Parser(abc.ABC):
    '''
    Абстрактный класс, отвечающий за преобразование данных в объект словаря
    '''
    def __init__(self, file):
        self.file = file

    @abc.abstractmethod
    def __validate(self):
        pass

    @abc.abstractmethod
    def parse(self):
        pass


# Что может пойти не так при чтении файла?
# 1. Файл не CSV формата
#   1.1

# 2. Разделитель в файле не соответствует ожидаемому
#   2.1

# 3. На вход подана не строка байт
#   3.1

class CsvIoParser(Parser):
    '''
        Получает на вход файл csv в видей строки байт
        Преобразовывает файл в кортеж именнованных кортежей (NamedTuple)

        Если на вход подан не CSV файл, то возбуждается исключение
        Если в процессе преобразования возникает ошибка, то возбуждается исключение
    '''

    def __validate(self):
        try:
            dialect = csv.Sniffer().sniff(self.file.read(1024))
        except csv.Error:
            logger.exception('Входные данные не соответствуют формату CSV')
            raise NotCsvFormatError()
        if dialect.delimiter != ';':
            logger.exception('Разделитель в файле CSV не соответствует ;')
            raise UnexpectedCsvDelimiterError()
        file.seek(0)
        logger.debug('the file was validated')

    def parse(self):
        self.__validate()
        logger.debug('the file was parsed')
