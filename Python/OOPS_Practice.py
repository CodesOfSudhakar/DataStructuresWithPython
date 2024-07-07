from workingWithExcel import inputFile

df = inputFile()
print(df)


class record:

    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob




for index, row in df.iterrows():
    recObj = record(name = row['Name'], age=row['Age'], dob=row['Dob'])

    print(f"Name: {recObj.name}, Age: {recObj.age}, Dob: {recObj.dob}")
