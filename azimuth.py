def degree(deg_val):

    deg_val = int(deg_val)
    if deg_val <= 22.5:
        return "Северный"
    if deg_val >= 22.6:
        if deg_val <= 67.5:
            return "Северо-восточный"
    if deg_val >= 67.6:
        if deg_val <= 112.5:
            return "Восточный"
    if deg_val >= 112.6:
        if deg_val <= 157.5:
            return "Юго-восточный"
    if deg_val >= 157.6:
        if deg_val <= 202.5:
            return "Южный"
    if deg_val >= 202.6:
        if deg_val <= 247.5:
            return "Юго-восточный"
    if deg_val >= 247.6:
        if deg_val <= 292.5:
            return "Восточный"
    if deg_val >= 292.6:
        if deg_val <=337.5:
            return "Северо-западный"
        elif deg_val <= 360:
            return "Северный"
        else:
            return "error value"


