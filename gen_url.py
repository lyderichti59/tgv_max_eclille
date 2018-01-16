from datetime import date, timedelta

def get_vcode(ville):
    """     return : le code de la Ville en question pour l'url
            arg: ville -> Ville dont on cherche le code
            
            Si le code est inconnu, la fonction retourne "ERREUR"
    """
    
    
    if " " not in ville and "-" not in ville:
        return "FR" + ville.upper()[0:3]
    else:
        return "ERREUR"

def get_dcode(date):
    """     return : le code de la date (en str)  en question pour l'url
            arg: ville -> date (de type datetime.date) dont on cherche le code
            
            Si le code est inconnu, la fonction retourne "ERREUR"
    """
    s= str(date.year)
    if (date.month <10):
        s = s+"0"
    s= s+str(date.month)
    if (date.day <10):
        s = s+"0"
    s= s+str(date.day)
    
    return s




def gen_url(v_dep,v_arr,jour_dep,trajetDirect="false"):
    """
    return : l'url du calendrier des bons plans en fonctions des paramètre suivants
    arg : v_dep = ville de départ textuellement (type str)
    arg : v_arr = ville d'arrivée textuellement (type str)
    arg : jour_dep de départ (type datetime.date)
    arg: trajetDirect (type boolean) type de trajet
    
    """
    
    return "https://www.oui.sncf/bons-plans/tgvmax#!/"+get_vcode(v_dep)+"/"+get_vcode(v_arr)+"/"+get_dcode(jour_dep) + "/ONE_WAY/2/12-HAPPY_CARD?onlyDirectTrains="+str(trajetDirect).lower() + "&lang=fr*"

  