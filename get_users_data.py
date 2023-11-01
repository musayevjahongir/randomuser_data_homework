from get_data import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    l=[]
    for i in data["results"]:
        d={}
        d["ism"]=i["name"]["first"]
        d["familiya"]=i["name"]["last"]
        d["phone"]=i["phone"]
        l.append(d)
    return l
s=get_data("randomuser_data.json")
print(get_users_data(s))