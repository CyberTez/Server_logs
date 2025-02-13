# Use this script to solve the problem
# Start by writing comments for your initial design (and commit before coding)

#import relevent modules
from src.domain import Domain
import csv
import os


# create a function to read in data and separate items in lines by commas
def read_server_log(filepath):
    domain_list = []
#create dictionaries that will contain key: site domain value : bytes accessed

    with open(filepath, 'rt') as file:
        reader = csv.reader(file, delimiter=',')
        for lines in reader:
            date = lines[0]
            ip_addy = lines[1]
            site_name = lines[2]
            bytes_accessed = int(lines[3])

            domain_list.append(Domain(date,ip_addy,site_name,bytes_accessed))


    return domain_list
#create function to read data and return dictionaries
def read_server_log_dict(filepath):
#create dictionaries that will contain key: site domain value : bytes accessed
    com_dict = {}
    net_dict = {}
    org_dict  = {}
    total_bytes = 0

    with open(filepath, 'rt') as file:
        reader = csv.reader(file, delimiter=',')
        for lines in reader:
            date = lines[0]
            ip_addy = lines[1]
            site_name = lines[2]
            bytes_accessed = int(lines[3])

            if site_name.__contains__('.com'):
                com_dict[site_name] = bytes_accessed
                if len(com_dict) == 0:
                    print('no sites with .com domain')
            elif site_name.__contains__('.net'):
                net_dict[site_name] = bytes_accessed
                if len(com_dict) == 0:
                    print('no sites with .net domain')
            elif site_name.__contains__('.org'):
                org_dict[site_name] = bytes_accessed
                if len(org_dict) == 0:
                    print('no sites with .org domain')
    return f'{com_dict}\n {net_dict}\n {org_dict}\n' \
           f' number of .com domains {len(com_dict)} | number of .net domains {len(net_dict)} | number of .org domains {len(org_dict)}\n' \
           f'total bytes accessed by domain:  .com( {sum(com_dict.values())}), .net( {sum(net_dict.values())}), .org( {sum(org_dict.values())})'




# create list to hold all sites
# create separate lists to hold different types of domains
#create a dump function?


if __name__ == '__main__':
    file_path  = os.path.join("data", "shorter.csv")

    server_log_data = read_server_log(file_path)
    server_log_data.sort()
    for domains in server_log_data:
        print(domains)

    server_log_dict = read_server_log_dict(file_path)



    print(server_log_dict)

