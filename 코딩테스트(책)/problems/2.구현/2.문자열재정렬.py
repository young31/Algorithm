# input
ex1 = 'K1KA5CB7'
ex2 = 'AJKDLSI412K4JSJ9D'
# answer: ABCKK13, ADDIJJJKKLSS20

# algo
def sol(ex):
    no = 0
    let = []
    for l in ex:
        try:
            n = int(l)
            no += n
        except:
            let.append(l)

    let = sorted(let, key=lambda x: ord(x))
    let = ''.join(let)
    let += str(no)
    return let

print(sol(ex1))
print(sol(ex2))