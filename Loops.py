#List comprehensions provide a concise way to create lists.
sports = [ "Football", "Basketball", "Tennis", "Golf", "Volleyball"]
group = [x for x in sports if "ball" in x]
print(group)

words = ["tree", "button", "cat", "window", "defenestrate"]
required = [x for x in words if len(x) > 4 ]
print(required)

