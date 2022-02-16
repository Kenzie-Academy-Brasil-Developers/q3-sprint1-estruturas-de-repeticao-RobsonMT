def corresponding_parenthesis(text : str) -> str:
    parenthesis = ['()',')(']

    while any(x in text for x in parenthesis):
        for corresponding in parenthesis:
            text = text.replace(corresponding, '')

    return text

def remove_more_than_two_repetitions(text : str) -> str:
    text_without_repetitions = ""

    for i, letter in enumerate(text):
        if letter != text[i -1] or letter != text[i-2]:
            text_without_repetitions += letter

    return text_without_repetitions