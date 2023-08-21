name = 'salman md sultan'
up_case = name.upper()
lower_case = up_case.lower()
cap_case = name.capitalize()

demo1 = 'sms , developer , food lover'
rep_text = demo1.replace('developer','Software Developer')

# split_text1 = demo1.split() #space oriented separator
# split_text2 = demo1.split('d')

# print(split_text1)
# print(split_text2)

demo3 = "Electronics items found in Headphones found & Headsets"

pos1 = demo3.find("Headsets")
pos2 = demo3.index("Headsets")


pref = demo3.startswith("items")
pref = demo3.endswith("Headsets")


cnt = demo3.count("found")
print(pref)
# split_text4 = demo3.split(" ")
# count = split_text4[0]
# size_demo3 = len(demo3)

# print(split_text4[])


# import re
# text = "16608 items found in Headphones & Headsets 160000"
# pattern = re.compile(r'\d+')
# matches = pattern.finditer(text)
# for match in matches:
#     print(match.group())


