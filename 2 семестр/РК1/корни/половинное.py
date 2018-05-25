# половинное деление

def half_del(a, b, f):
    count = 0
    while (b - a) >= eps:
        count += 1
        x = (a + b) / 2
        if f(x) == 0:
            break
        if f(a) * f(x) <= 0:
            b = x
        else:
            a = x
    if count > it:
        code = 2
    else:
        code = 0
    mcode.append(code)
    mcount.append(count)
    mx.append(x)
    
    return x
