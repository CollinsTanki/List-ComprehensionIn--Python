from friends import friends

# Check on people who have registered
FakeGenz = [f for f in friends if not f["Registered"]]

# for f in friends:
#   if not f["Registered"]:
#     FakeGenz.append(f)

print(FakeGenz)
