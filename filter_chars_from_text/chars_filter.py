
def filter_text(text, filtered_chars_set):
    output_text = ''
    for i in text:
        if i not in filtered_chars_set:
            output_text += i
    return output_text
