import my_utils

lofd = [{'num': 1}, {'num': 2}]

def act_link(larg):
    if len(larg) == 0:
        return ""
    return '<a href="/delete/'+str(larg[0])+'">Delete</a> | <a href="/edit/'+str(larg[0])+'>Edit</a>'

print(my_utils.add_column_to_list_of_dict(lofd, column='links', funcname=act_link, args=['num']))
print(lofd)
