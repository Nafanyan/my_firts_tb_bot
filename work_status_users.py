source: dict = {}

def read_status(id):
    file_status = open(f'C:/Users/01112/PycharmProjects/my_firts_tb_bot/status_users/{id}.txt','r')
    elements_status = []
    for info in file_status:
        info_status = info.split('\n')
        diff_status = info_status[0].split()
        for i in range(1, len(diff_status)):
            elements_status.append(diff_status[i])
        source[diff_status[0]] = elements_status
        elements_status = []
    file_status.close()
    return source
read_status('0')

def change_status(new_source, id):
    file_status = open(f'C:/Users/01112/PycharmProjects/my_firts_tb_bot/status_users/{id}.txt','w')
    for i in new_source:
        file_status.writelines(f'{i} ')
        for el_st in new_source[i]:
            file_status.writelines(f'{el_st} ')
    file_status.close()
