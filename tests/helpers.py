def compare_dict(dict1, dict2):
    if dict1 and dict2:
        for key in dict1:
            if key not in dict2 or dict1[key] != dict2[key]:
                return False
    return True
