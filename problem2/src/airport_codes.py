def read_airport_codes(file_name):
    
    with open(file_name, 'r') as file:
        file_as_string = file.readlines()
      
    return file_as_string

def parse_airport_codes(file_as_string):
    
    return [code.strip() for code in file_as_string]