def get_next_target (s):
    start_link = s.find('<a href=')
    start_quote = s.find('"', start_link)        # int representing the position in string where the next target url begins
    end_quote = s.find('"', start_link + 1)      # int representing the position in string where the next target url ends
    url = s[start_quote + 1 : end_quote]
    return url, end_quote