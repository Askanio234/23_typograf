import re


def process_text(users_text):
    replace_quotes = re.sub(r'([\'"])(.*?)(\1)', r'«\2»', users_text)
    replace_dashes = re.sub(r'–', "—", replace_quotes)
    replace_long_dashes_in_phones = re.sub(r'(\d*)—(\d*)—(\d*)—(\d*)—(\d*)',
                                        r'\1–\2–\3–\4–\5', replace_dashes)
    replace_exceeding_whitespaces = re.sub(r'(\s){2,}', r'\1',
                                            replace_long_dashes_in_phones)
    replace_space_with_non_break_space = re.sub(r'(\d+)\s+(\w+)',
                                                u'\\1\u00A0\\2',
                                                replace_exceeding_whitespaces)
    link_conjuctions_with_next_word = re.sub(r'(\w{1,3})\s(\w{3,})',
                                            u'\\1\u00A0\\2',
                                            replace_space_with_non_break_space)
    return link_conjuctions_with_next_word
