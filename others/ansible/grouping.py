"""
DATE            Author                                      Update
28 NOV 2021     Abhay Raj Singh (abhayraja4@gmail.com)      IP grouping version 1 without leveling
28 NOV 2021     Abhay Raj Singh (abhayraja4@gmail.com)      With level 1 edge case
28 NOV 2021     Abhay Raj Singh (abhayraja4@gmail.com)      With N level edge case covered
"""

# open file for reading lines
PATH_OF_INVENTORY = '/PATH/TO/inventory.ini'
with open(PATH_OF_INVENTORY) as f:
    file_lines = f.readlines()


# checks if given line has an IP address
def is_an_ip_address(string_line):
    # replace with regex to be precise, if needed
    not_a_comment = string_line[0] != '#'
    dot_found = '.' in string_line
    return not_a_comment and dot_found


group_parent = dict()
current_group = '[default]'  # if inventory starts without group
ip_list = dict()
for line in file_lines:
    stripped_line = line.strip()
    if stripped_line and stripped_line[0] == '[':
        current_group = stripped_line[1:-1]  # remove square brackets
        if current_group not in group_parent:
            group_parent[current_group] = None
    elif stripped_line and is_an_ip_address(stripped_line):
        current_ip = stripped_line.split()[0]  # strip metadata if any
        if current_ip not in ip_list:
            ip_list[current_ip] = []
        ip_list[current_ip].append(current_group)
    elif stripped_line and stripped_line[0] != '#':
        current_child = stripped_line
        # print('child', current_child, 'parent', current_group)
        group_parent[current_child] = current_group.split(':')[0]

# print(group_parent)
# print(ip_list)
for ip in ip_list:
    ip_groups = ip_list[ip]
    ip_info = ip
    while ip_groups:
        # print(ip_groups)
        ip_group = ip_groups.pop()
        ip_info += ' ' + ip_group
        if ip_group in group_parent and group_parent[ip_group]:
            ip_group_parent = group_parent[ip_group]
            ip_info += ' ' + ip_group_parent
            if ip_group_parent in group_parent:
                ip_groups.append(group_parent[ip_group_parent])
    print(ip_info)
