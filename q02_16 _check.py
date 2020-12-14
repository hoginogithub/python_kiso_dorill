def dropped_list(src_list, i):
    temp = [x for k, x in enumerate(src_list) if k != i]
    # print('dropped_list=' + str(temp))
    return temp

def all_permutations(num_list):
    print('---------------------------')
    print('num_list=' + str(num_list))
    if num_list == []:
        return [[]]
    result_list = []
    for i, elem in enumerate(num_list):
        print('=============================')
        print(f'i={i} elem={elem}')
        temp_list = all_permutations(dropped_list(num_list, i))
        print(temp_list)
        
        for tmp in temp_list:
            print(f'result_list(before)={result_list} [elem]={[elem]} tmp={tmp}')
            result_list += [[elem] + tmp]
            print(f'result_list(after)={result_list}')
        
        # result_list += list(map(lambda perm: [[elem] + perm], temp_list))

        #print(f'result_list(after)={result_list}')
    return result_list

print(all_permutations([4, 5, 6]))

