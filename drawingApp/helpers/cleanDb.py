import shelve

def clean():
    d = shelve.open('imgNum.txt')
    d['fileNum'] = 0
    d.close()

clean()
