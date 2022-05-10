# import datetime
# import json


# class DateTimeEncoder(json.JSONEncoder):
#     def default(self, z):
#         if isinstance(z, datetime.datetime):
#             return (str(z))
#         else:
#             return super().default(z)




# my_dict = {
#     'Policy': '101126', 
#     'Expiry': datetime.datetime(2021, 12, 31, 0, 0), 
#     'Location': 'Urban', 
#     'State': 'WI', 
#     'Region': 'Midwest', 
#     'InsuredValue': 1776800, 
#     'Construction': 'Frame', 
#     'BusinessType': 'Farming', 
#     'Earthquake': 'N', 
#     'Flood': 'N'
#     }

# print(json.dumps(my_dict,cls=DateTimeEncoder))


a = 1
b = 9

if a < b:
    arr = [i for i in range(a, b+1)]
    print(arr)