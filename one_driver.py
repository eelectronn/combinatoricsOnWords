from prefer_one import generate_prefer_one

for i in range(1, 10):
    ndr, db = generate_prefer_one(i)
    print('n:', i)
    print(db)
    print(ndr)

