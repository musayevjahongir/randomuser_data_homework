from get_data import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    a=[]
    for i in data["results"]:
        a.append(i["email"])
    return a
s=get_data("randomuser_data.json")
print(get_email(s))