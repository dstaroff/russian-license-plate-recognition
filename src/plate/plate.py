class LicensePlateError(ValueError):
    pass


class InappropriateSeriesCharacterError(LicensePlateError):
    pass


class InappropriateNumberCharacterError(LicensePlateError):
    pass


class LicensePlate:
    _series_character_white_list = ['A',
                                    'B',
                                    'C',
                                    'E',
                                    'H',
                                    'K',
                                    'M',
                                    'O',
                                    'P',
                                    'T',
                                    'X',
                                    'Y',
                                    '8',  # B
                                    '0',  # O
                                    '7',  # T
                                    ]
    _number_character_white_list = ['0',
                                    '1',
                                    '2',
                                    '3',
                                    '4',
                                    '5',
                                    '6',
                                    '7',
                                    '8',
                                    '9',
                                    'O',  # 0
                                    'T',  # 7
                                    'B',  # 8
                                    ]

    def __init__(self, series, number, region):
        self.series = series
        self.number = number
        self.region = region

    def __str__(self):
        return f'{self.series[0]}{"".join(self.number)}{"".join(self.series[1:3])}{"".join(self.region[:len(self.region)])}'

    @staticmethod
    def _get_series_entry_from_character(character: str):
        upper_character = character.upper()

        if upper_character not in LicensePlate._series_character_white_list:
            raise InappropriateSeriesCharacterError()

        if upper_character == '8':
            return 'B'
        elif upper_character == '0':
            return 'O'
        elif upper_character == '7':
            return 'T'
        else:
            return upper_character

    @staticmethod
    def _get_number_entry_from_character(character: str):
        upper_character = character.upper()

        if upper_character not in LicensePlate._number_character_white_list:
            raise InappropriateNumberCharacterError()

        if upper_character == 'B':
            return '8'
        elif upper_character == 'O':
            return '0'
        elif upper_character == 'T':
            return '7'
        else:
            return upper_character

    @staticmethod
    def from_characters(characters):
        series = ''.join([LicensePlate._get_series_entry_from_character(characters[0]),
                          LicensePlate._get_series_entry_from_character(characters[4]),
                          LicensePlate._get_series_entry_from_character(characters[5])])
        number = ''.join([LicensePlate._get_number_entry_from_character(characters[1]),
                          LicensePlate._get_number_entry_from_character(characters[2]),
                          LicensePlate._get_number_entry_from_character(characters[3])])
        region = [LicensePlate._get_number_entry_from_character(characters[6]),
                  LicensePlate._get_number_entry_from_character(characters[7])]
        if len(characters) == 9:
            region.append(LicensePlate._get_number_entry_from_character(characters[8]))
        region = ''.join(region)

        return LicensePlate(series, number, region)
