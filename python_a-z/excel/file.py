import pandas as pd

# read_excel = pd.read_excel(
#     'c:\\Users\\hp\\Pictures\\pyhton_101\\python_a-z\\excel\\data.xlsx',
#     engine='openpyxl'  # specify engine explicitly
# )
# print(read_excel)

#wiriting on file
data = {
    "Name": ["abel", "beni"],
    "phone": ["754646", "754646"],
    "age": [50, 89]
}
# df= pd.DataFrame(data)
# df.to_excel('c:\\Users\\hp\\Pictures\\pyhton_101\\python_a-z\\excel\\output.xlsx', index=False, engine='openpyxl')
df=pd.read_excel('c:\\Users\\hp\\Pictures\\pyhton_101\\python_a-z\\excel\\output.xlsx', engine='openpyxl')
print(df)