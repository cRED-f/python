num_list=[1,2,3]
new_num_list=[item+1  for item in num_list]
print(new_num_list)


names=["fahim","jahid","asif","mark","jhonny","naif","jihan"]
short_names=[n for n in names if len(n)<5]
print(short_names)

long_name=[n.upper() for n in names if len(n)==5]
print(long_name)