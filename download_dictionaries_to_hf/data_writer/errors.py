class ValidationError(Exception):
    '''
        Возбуждается при неудачной попытке преобразовать CSV файл в объект Python
    '''
    pass


class NotCsvFormatError(ValidationError):
    '''
        Возбуждается в том случае если строка байт переданная на вход не соответствует файлу CSV
    '''
    pass


class UnexpectedCsvDelimiterError(ValidationError):
    '''
        Возбуждается в том случае если разделитель в файле CSV не является переданным резделителем
    '''

    def __init__(self, delimiter=';'):
        self.delimiter = delimiter

    def __str__(self):
        return 'Разделитель в файле не соответствует'.format(self.delimiter)
