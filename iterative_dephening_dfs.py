def vec_sum(u, v):
    x_a, y_a = u 
    x_b, y_b = v
    return x_a + x_b, y_a + y_b

def vec_scale(u, k):
    x, y = u
    return x * k, y * k

def f(u):
    x, y = u
    if x < 0 or y < 0:
        return 0
    return 1

def g(u):
    M, C = u
    if M > 0 and M < C:
        return 0
    return 1

def p(s, k_peek, k, exec_stk):
    if exec_stk != []:
        kp = None
        for si, _, ki in exec_stk:
            if s == si and (kp, ki) == (k_peek, k):
                return 0
            kp = ki
    return 1

def q(exec_stk, d):
    if len(exec_stk) == d:
        return 0
    return 1

def t(s, w, k):
    u, v = s
    return vec_sum(u, vec_scale(w, -k)), vec_sum(v, vec_scale(w, k))

def j(s):
    _, v = s
    M, C = v
    return M + C

def iterative_dephening_dfs(s, sf, W, d):
    solution = []
    searching = True
    exec_stk = [(s, [], 1)]
    while searching:

        s, w_valid, k = exec_stk.pop()
        if w_valid == []:
            for w in W:
                sn = t(s, w, k)
                u, v = sn
                if f(u) + f(v) + g(u) + g(v) + p(sn, k, -k, exec_stk) + q(exec_stk, d) == 6:
                    w_valid.append(w)
        
        if w_valid != [] and w_valid != None:
            w = w_valid.pop()
            sn = t(s, w, k)
            if w_valid == []:
                w_valid = None
            exec_stk.append((s, w_valid, k))
            exec_stk.append((sn, [], -k))

        if exec_stk != []:
            s, _, _ = exec_stk[-1]
            if s == sf:
                searching = False

                #saving solution
                for i, cell in enumerate(exec_stk[:-1]):
                    s, _, k = cell
                    sup, _, _ = exec_stk[i + 1]
                    Ms, Cs = s[0]
                    Mup, Cup = sup[0]
                    w = abs(Ms - Mup), abs(Cs - Cup)
                    solution.append((s, k, w))
                solution.append((sf, None, None))
                #end saving solution

        else:
            searching = False
            solution = []
    return solution
    


if __name__ == '__main__':
    s = (3, 3), (0, 0)
    sf = (0, 0), (3, 3)
    W = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 1)]

    d = 0
    solution = []
    while solution == []:
        solution = iterative_dephening_dfs(s, sf, W, d)
        d += 1

    print('d = {}'.format(d))
    print('solution length = {}'.format(len(solution)))
    print('')
    print('solution')
    for s in solution:
        print(s)