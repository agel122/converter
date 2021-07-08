def weight_converter(value_to_convert):
    result = value_to_convert / 1000
    return {'result': result,
            'initial_value': value_to_convert,
            'initial_unit': 'g',
            'result_unit': 'kg'}


dispatcher = {'weight_converter': weight_converter}







