import pandas as pd

# Creating 2 paths to read 2 excel files

files7_path, given_file_path = r'file1.xlsx',  r'file2.xlsx'

# Data from the path is saved in the variables
files7  = pd.read_excel(files7_path)
given_values = pd.read_excel(given_file_path)


myList7 = files7['Requirement ID'].tolist() # Converting the files into python lists 
# print(myList7)
myListAll= given_values['ObjectID'].tolist()
# print(myListAll)
uniqueIDs = [] # A new list to store the unique IDs that weren't part of each file.
for ID in myList7:
    if ID not in myListAll:
        uniqueIDs.append(ID) # File1 values are compared with File2 and non existing values are appended to the Unique list.
for ID in myListAll:
    if ID not in myList7:
        uniqueIDs.append(ID) # File2 values are compared with File1 and non existing values are appended to the same Unique list.
# print(uniqueIDs)

# Creating a dictionary to write it into Excel sheet. 
all = {'ObjectID' : myListAll,
'Requirement ID' : myList7,
'Unique ID' : uniqueIDs
}

df = pd.DataFrame({key:pd.Series(value) for key, value in all.items()}) # It is to print the NaN values instead of leaving it blank.
print(df)

writer = pd.ExcelWriter('Result.xlsx', engine='xlsxwriter')
df.to_excel(writer, index = False)
writer.save()

#Writes the data into Excel and saves it.
