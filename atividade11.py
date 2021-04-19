lista=[5,4,7,6,8]
print(str.join("---", map(lambda x: str(x), filter(lambda x: x > 2 and x < 6, lista))))
