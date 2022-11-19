def oxford_comma(items):
    sz = len(items)
    if sz == 1:
        return items[0]
    elif sz == 2:
        return " and ".join(items)
    else:
        items[-1] = "and " + items[-1]
        return ", ".join(items)
