def dice_code_conv(code):

    try:
        if 'D' not in code:
            return None
        else:
            pass
    except TypeError:
        return None

    else:

        DICE_DIC = {'D3': 3, 'D4': 4, 'D6': 6 , 'D8': 8, 'D10': 10, 'D12': 12, 'D20':20, 'D100': 100}

        code = '0' + code
        separated_code = ''

        for char in code:
            if char in 'D+-':
                separated_code = separated_code + ' ' + char
            else:
                separated_code += char

        param_lst = separated_code.split(' ')

        if len(param_lst) == 2:
            param_lst.append('0')
        if int(param_lst[0]) == 0:
            param_lst[0] = 1

        try:
            res = [int(param_lst[0]), DICE_DIC[param_lst[1]], int(param_lst[2])]
        except KeyError:
            return None

        return tuple(res)


def dice(dice_code):

    if dice_code_conv(dice_code) == None:
        print("Wrong format of code!")
        return None
    else:
        throws_num, dice_num, modif = dice_code_conv(dice_code)
        return throws_num * dice_num + modif




print(dice('2D10+10'))
print(dice('D6'))
print(dice('2D3'))
print(dice('D12-1'))
# print(dice('asd'))
# print(dice(123))
# print(dice(True))
# print(dice('D12#1'))