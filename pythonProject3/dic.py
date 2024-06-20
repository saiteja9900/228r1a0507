def invert_content(dic):
    invert_dic = {}

    invert_dic = {v: k in for k, v in dic.items}

    return invert_dic

