import subprocess


with open(r'E:\Gordey$\WS\Python\files\domen_names.txt', 'r') as f:
    names_pc = f.read().splitlines()

index = 1
for name_pc in names_pc:
    print(index, '-', name_pc)
    index += 1
    proc = subprocess.Popen(['powershell', 'get-WmiObject -class Win32_Share -computer ' + name_pc + ' |'
                            ' Export-Csv "E:\\share\\' + name_pc + '.csv" -UseCulture -NoTypeInformation -Encoding '
                                                                  'Default'])
    proc.wait()

share_list_info = []
problem_pc = []
for name_pc in names_pc:
    try:
        with open('E:\\share\\' + name_pc + '.csv', 'r') as f:
            share = f.read().splitlines()
    except:
        problem_pc.append(name_pc)
        continue

    with open('E:\\share\\' + name_pc + '.txt', "w") as file:
        for name in share:
            file.write(name + '\n')

    with open('E:\\share\\' + name_pc + '.txt', 'r') as f:
        share_list_info.append(f.read().splitlines())

share_list = []
for shares in share_list_info:
    for share in shares:
        share_list.append(share.split(';'))

pc_name_list = [names_pc[0]]
share_file = [pc_name_list[0]]

with open('E:\\Gordey$\\WS\Python\\files\\full_share.txt', "a") as file:
    file.write('PC Name: ' + pc_name_list[len(pc_name_list) - 1] + '\n')

for share_info in share_list:
    if share_info[0] == '\"PSComputerName\"':
        continue

    if share_info[0][1:len(share_info[0]) - 1] == pc_name_list[len(pc_name_list) - 1]:
        share_file.append(share_info[5][20:len(share_info[5]) - 3])
        with open('E:\\Gordey$\\WS\Python\\files\\full_share_folder.txt', "a") as file:
            file.write(share_info[5][20:len(share_info[5]) - 3] + '\n')
    else:
        pc_name_list.append(share_info[0][1:len(share_info[0]) - 1])
        share_file.append('PC Name: ' + pc_name_list[len(pc_name_list) - 1])
        with open('E:\\Gordey$\\WS\Python\\files\\full_share_folder.txt', "a") as file:
            file.write('PC Name: ' + pc_name_list[len(pc_name_list) - 1] + '\n')

with open('E:\\Gordey$\\WS\Python\\files\\share_problem_pc.txt', "w") as file:
    for pc in problem_pc:
        file.write(pc + '\n')
