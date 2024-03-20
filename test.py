from pprint import pprint

a = {i: {j: None for j in range(5)} for i in range(10)}

pprint(a[0][0])