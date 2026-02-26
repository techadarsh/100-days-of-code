# How to add python packages and use PyPi
# https://pypi.org

from prettytable import PrettyTable

table = PrettyTable()
# print(table) # print empty table

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Pokemon Type",["Electric","Water","Fire"])
print(table.align)
table.align = "l" 
print(table.align)
print(table)
