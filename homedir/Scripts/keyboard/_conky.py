#!/usr/bin/python3


def get_filepaths():

    with open('/home/tbear/Scripts/conky.files', 'r') as rob:
        file_list = [_.strip() for _ in rob.readlines()]
    try:
        indy = int(file_list[0])
        file_list = file_list[1:]
    except:
        indy = -1

    indy = (indy+1)%len(file_list)

    with open('/home/tbear/Scripts/conky.files', 'w') as wob:
        wob.write(str(indy))
        for _ in file_list:
            wob.write('\n')
            wob.write(_)
        wob.write('\n')

    return indy, file_list


def switch():

    indy, file_list = get_filepaths()
    indy = (indy + 1)%len(file_list)
    with open(file_list[indy], 'r') as rob:
        st = rob.read()

    with open('/home/tbear/Scripts/conky', 'w') as wob:
        wob.write(st)


if __name__ == '__main__': switch()









'''
def get_current():

    try:
        with open('current', 'r') as rob:
            current = rob.read().strip()
    except:
        current = default_file

    return current


def get_new(current):

    dir_ls = sorted(os.listdir('options'))
    try:
        indy = (1+dir_ls.index(current))%len(dir_ls)
    except:
        indy = 0
    ret = dir_ls[indy]

    with open('current', 'w') as wob:
        wob.write(ret)
    print(ret)
    return ret


def switch():

    current = get_current()

    new = get_new(current)

    with open(f'options/{new}', 'r') as rob:
        st = rob.read().strip()
    with open(f'options/conky', 'w') as wob:
        wob.write(st)

#if __name__ == '__main__':
#    switch()







#while True:
#    if input(switch()): break
'''








