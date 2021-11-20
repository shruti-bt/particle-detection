def check_title(input_string):
    r"""TO BE DOCUMENTED"""
    output = (input_string.split('|'))[-1]

    if output == "FBS":
        return "Fragment"
    elif output == "SBF":
        return "Sphere"
    else:
        return output
