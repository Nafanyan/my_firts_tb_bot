import work_status_users


def check_status(id):
    if (len(work_status_users.read_status(id)['cities']) == 0):
        return True
    else: return False


#def add_status(id):
def a():
    b = input()
    c = input()
