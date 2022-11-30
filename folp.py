import shutil
shutil.rmtree('./__pycache__',ignore_errors=True)



def create(www):
    ju = open(str(www)+'.folp', 'a', -1, 'utf-8')
    ju.write('')
    ju.close()


def read(www):
    ju = open(str(www)+'.folp', 'r', -1, 'utf-8')
    ss = ju.read()
    ju.close()
    ss = ss.split('\n')
    # удаление всех ненужных элементов
    i = 0
    try:
        while True:
            if len(ss[i].split('>>')) == 1:
                ss.pop(i)
                i -= 1
            if ss[i] == '':
                ss.pop(i)
                i -= 1
            i += 1
    except:
        pass


    i = 0
    oi = {}
    while i < len(ss):
        ew = ss[i].split('>> ')
        if (ew[1])[0] == "'":
            oi[ew[0]] = ew[1].replace("'","")
        else:
            oi[ew[0]] = int(ew[1])

        i += 1

    return oi


def record(www,gf,ooo):
    oi = read(www)
    oi[gf] = ooo
    oiw = list(oi)
    ju = open(str(www)+'.folp', 'w', -1, 'utf-8')
    i = 0
    while i <= len(oiw)-1:
        if type(oi[oiw[i]]) == str:
            ju.write('\n'+oiw[i]+'>> \''+str(oi[oiw[i]])+'\'')
        else:
            ju.write('\n'+oiw[i]+'>> '+str(oi[oiw[i]]))
        i += 1
    ju.close()


def test():

    s = 0
    uy = 3
    while s < uy:
        # print(str(100//uy*s)+'%', end='\n')

        if 100//uy*1 == 100//uy*s:
            create('test')
        if 100//uy*2 == 100//uy*s:    
            record('test','saa','w888')
        if 100//uy*3 == 100//uy*s:
            read('test')
        s += 1
    print('100%')