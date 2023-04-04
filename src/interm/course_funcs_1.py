"Funcs exemplifying unit 2: intermediate pytest"

def i_want_string(string):
    if isinstance(string, str):
        pass
    else:
        raise TypeError("That's not a string!")
    
def num_to_pH(num):
    """Describes the property of a pH"""
    # lets always deal with floats
    if isinstance(num, int):
        num = float(num)
    elif not isinstance(num, float):
        raise ValueError("`num` must be an integer or float.")
    # neutral
    if num == 7.0:
        return "neutral"
    elif num >= 0.0 and num < 7.0:
        return "acid"
    elif num > 7.0 and num <= 14.0:
        return "alkali"
    else:
        return None
    