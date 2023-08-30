user = {"id":1,"name":"salman","dob":"1992-10-23"}
sample_dict = {"a":1,"b":2,"c":3}

new_dict = {key for key in sample_dict if sample_dict[key]<3}
print(new_dict)

# for key,data in user.items():
#     print(key,data)