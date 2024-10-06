data = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

a = input()
print(data.index(a) if a in data else 'error')
