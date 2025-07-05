my_list=[12,34,56,778,66,57,453,46,567,688,755,76]
result=list(filter(lambda x:(x%6==0),my_list))
print("Number divisible by 6 are",result)