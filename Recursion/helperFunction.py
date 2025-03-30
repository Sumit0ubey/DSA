def substring(string:str, startwith:int, endwith:int=0) -> str:
    if endwith == 0: endwith = len(string)
    return string[startwith:endwith]

