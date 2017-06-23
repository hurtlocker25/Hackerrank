def mutate_string(string, position, character):
    templist = list(string)

    templist[position] = character

    finalstring = ''.join(templist)

    return finalstring