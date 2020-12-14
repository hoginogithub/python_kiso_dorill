from multiprocessing import Pool

def proc(value):
    return -value

if __name__ == '__main__':
    with Pool(20) as pool:
        print(pool.map(proc, range(1,11)))