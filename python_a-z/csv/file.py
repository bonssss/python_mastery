import csv


# wrinting on file

data =[
    ["abel","te@gmail.com",50],
    ["beni","hd@gmail.com",89]
]

with open('c:\\Users\\hp\\Pictures\\pyhton_101\\python_a-z\\csv\\data.csv', mode='w') as file:
    
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
    # print(csv_writer)
    
    
    # for row in csv_writer:
    #     print(row)
    
# reading file
with open('c:\\Users\\hp\\Pictures\\pyhton_101\\python_a-z\\csv\\data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    # next(csv_reader)
    
    for row in csv_reader:
        print(row)  # Each row is a list of values from the CSV file
        
        
    

