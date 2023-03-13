# a={'email': 'user@example.com', 'first_name': 'Test', 'last_name': 'User', 'password': 'password123', 'password1': 'password123', 'role': 'USER'}

# a['password']='aslfdklskdflkds'

# print(a)

a=[{"Gender": 1, "Name": "Abhash", "associateds": 2}, {"Gender": 2, "Name": "Divya", "associateds": 1}, {"Gender": 1, "Name": "Prakhar", "associateds": 2}]

l=[]
for i in a:
    if i['associateds']==2:
        l.append(i['Name'])


print(l)