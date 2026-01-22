def adress_validator(adress):
    if '@' not in adress or "." not in adress:
        return False
    
    at = adress.find("@")
    dot = adress.find('.')

    if at == 0 or dot == len(adress) - 1:
        return False
    
    if at > dot :
        return False
    
    return True

def adress_teller(adress):
    if not adress_validator(adress):
        return "Inavlid Adress"
    
    domain = adress.split("@")[1]

    match domain:
        case "gmail.com":
            return "Gmail"
        case "yahoo.com":
            return "Yahoo mail"
        case "outlook.com":
            return "Microsoft mail"
        case _:
            return "Unknown Domain"


adress = input("Enter your adress:")
print(adress_teller(adress))