def isIPv4Address(inputString):
    list_address = list(inputString.split('.'))

    if '' in list_address or len(list_address) != 4:
        return False

    try:

        for i in list_address:
            if not 0 <= int(i) <= 255:
                return False
    except ValueError:
        return False
    except TypeError:
        return False
    return True



inputString = '0.254.255.0'


print(isIPv4Address(inputString))
