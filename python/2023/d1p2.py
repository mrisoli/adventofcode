from d1 import two_digits, number_mapping

two_digits('(?=(\d|' + '|'.join(number_mapping.keys()) + '))')
