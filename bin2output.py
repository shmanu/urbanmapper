
''' Takes as input a 0-1 array and converts it to the output format'''

import argparse
import numpy as np 


def parse_args():
    parser = argparse.ArgumentParser(description='convert binary to output')

    parser.add_argument('--input_dir', type=str,
                        required=False, default='./')
    return parser.parse_args()

def dfs(bin_arr, index_arr, i, j, cur_index):
    stack = [(i,j)]
    (N1,N2) = bin_arr.shape
    while len(stack)> 0:
        (x,y) = stack.pop()
        index_arr[x,y] = cur_index
        if (x < N1 -1) and (bin_arr[x+1,y] == 1) and (index_arr[x+1,y] < 0):
            stack.append((x+1,y))
        if (y < N2 - 1) and (bin_arr[x,y+1] == 1) and (index_arr[x,y+1] < 0):
            stack.append((x,y+1))
        if (x > 0) and (bin_arr[x-1,y] == 1) and (index_arr[x-1,y] < 0):
            stack.append((x-1,y))
        if (y > 0) and (bin_arr[x,y-1] == 1) and (index_arr[x,y-1] < 0):
            stack.append((x,y-1))

def find_index(bin_arr):
    cur_index = 1
    index_arr = np.ones(bin_arr.shape)*-1
    for i in range(0,bin_arr.shape[0]):
        for j in range (0,bin_arr.shape[1]):
            if index_arr[i,j] >=0:
                continue
            elif bin_arr[i,j] == 0:
                index_arr[i,j] = 0 
            else:
                dfs(bin_arr, index_arr, i,j, cur_index)
                cur_index = cur_index + 1
    return index_arr


def index2output(index_arr):
    lin_size = index_arr.shape[0]*index_arr.shape[1]
    lin_arr = np.reshape(index_arr,newshape=lin_size)
    output = []
    count = 1
    for i in range(0, lin_size):
        if (i < lin_size-1) and (lin_arr[i] == lin_arr[i+1]):
            count = count + 1
        else:
            output.extend([int(lin_arr[i]), int(count)])
            count = 1
    print output
    return output

def main():
    args = parse_args() 
    for file in glob.glob(args.input_dir + '/*.npy'):
        print(file)
        bin_arr = np.fromfile(file)

        index_arr = find_index(bin_arr)

        output_list = index2output(index_arr)
        
if __name__ == '__main__':
    main()