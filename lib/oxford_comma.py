def oxford_comma(items):
    if len(items) == 1:
        return ''.join(items)
    elif len(items) == 2:
        return " and ".join(items)
    elif len(items) == 3:
       return f"{items[0]}, {items[1]}, and {items[2]}"
    elif len(items) > 3:
        item_names = items[0:-1]
        return ", ".join(item_names) + f", and {items[-1]}"
