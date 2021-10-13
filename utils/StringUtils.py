def rreplace(str, old_str_part, new_str_part, occurrence):
    splitted_str = str.rsplit(old_str_part, occurrence)
    return new_str_part.join(splitted_str)

def rremove(str, str_part, occurrence):
    splitted_str = str.rsplit(str_part, occurrence)
    return splitted_str[0]
