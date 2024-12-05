def rearrange_spaces(text):
    space = len([i for i in text if i == ' '])

    if space == 0:
        return text


    word_count = len(text.split())

    divided_space = space / (word_count-1)

    #return [i + ' '*int(divided_space) for i in text.split()]
    modified_text = ''

    for i in text.split():
        modified_text += i
        modified_text += ' '*int(divided_space)
    

    return modified_text.strip()


print(rearrange_spaces(' Hello  World!  '))
