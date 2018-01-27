def get_next_target (s):
    start_link = s.find('<a href=')
    if start_link > 0:
        start_quote = s.find('"', start_link)        # int representing the position in string where the next target url begins
        end_quote = s.find('"', start_link + 1)      # int representing the position in string where the next target url ends
        url = s[start_quote + 1 : end_quote]
    else:
        url = None
        end_quote = 0
    return url, end_quote

def rest_of_string(s, position):
    string = str(s)
    if position < len(string):
        new_string = string[position:]
    else:
        new_string = None
    return new_string
    