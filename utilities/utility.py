import re

def is_valid_input_string(string_value):
    return isinstance(string_value, str) and string_value.strip() != ""

# valida o padrão de data dd/mm/YYYY
def is_valid_string_date(date_string): 
    return re.match(r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$", date_string)