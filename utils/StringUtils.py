def rreplace(string, old_str_part, new_str_part, occurrence):
    split_str = string.rsplit(old_str_part, occurrence)
    return new_str_part.join(split_str)


def rremove(string, str_part, occurrence):
    split_str = string.rsplit(str_part, occurrence)
    return split_str[0]
