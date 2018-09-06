def fix_url_chars(string):
    string = string.replace("$slash$", "/")
    string = string.replace("$qmark$", "?")
    return(string)