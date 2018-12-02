def clean_data_string(x):
    if type(x) == str:
        no_spaxce_string = x.replace(" ","")
        lower_case = str.lower(no_spaxce_string)
        return lower_case
    else:
        return ''
        
def clean_data_list(x):
    string_array = []
    for i in x:
        
        no_space_string = i.replace(" ","")
        lower_case = str.lower(no_space_string)
        string_array.append(lower_case)
        
    return string_array