n = 5; m = 8; k = 3
arr = [2, 4, 5, 4, 6]
sort_arr = sorted(arr, reverse=True)

big1 = sort_arr[0]

if sort_arr[0] == sort_arr[1]:
    print(big1*m)
else:
    bigN = m//(k+1)
    big2 = sort_arr[1]
    print(big2 * bigN + big1 * (m - bigN))


