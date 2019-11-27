#!/usr/local/bin/python3

import sys
import re

def sqrt(a):
    return a ** 0.5

def syntax_checking(s):
    if len(s.split(' = ')) != 2:
        return 0
    s = s.split(' = ')
    r = []
    r.append(re.split(' [+-] ', s[0]))
    r.append(re.split(' [+-] ', s[1]))
    reg1, reg2, reg3 = '-?[\d]+(.[\d]+)* \* X(\^[\d]+)?', '-?[\d](.[\d]+)*', 'X(\^[\d]+)?'
    for row in r:
        for el in row:
            wit = 0
            M = [re.compile(reg1).match(el), re.compile(reg2).match(el),
            re.compile(reg3).match(el)]
            for m in M:
                if m and m.group() == el:
                    wit = 1
            if not wit:
                return 0
    return 1

def print_reduced_form(d):
    init = "Reduced form: "
    string = ""
    for i in sorted (d.keys()):
        if d[i] < 0:
            if string != "":
                string = string[:-2] + '-' + string[-1:]
            else:
                string = '- '
        string += str(abs(d[i])) + " * X^" + str(i) + " + "
    string = string[:-2]
    if not d:
        string += "0 "
    string += "= 0"
    print(init + string)

def append_to_dict(c, d, u, k):
    if c == '-':
        u = -u
    if k in d.keys():
        d[k] += u
    else:
        d[k] = u


def upd_dict(c, eq, d):
    for i, _ in enumerate(eq):
        if 'X' in eq[i]:
            if i == 0 or eq[i - 1] == '+':
                u = 1
            elif eq[i - 1] == '-':
                u = -1
            elif eq[i - 1] == '*':
                u = eq[i - 2]
                try:
                    u = int(u)
                except ValueError:
                    u = float(u)
                if i >= 3 and eq[i - 3] == '-':
                    u = -u
            if 'X^' in eq[i]:
                k = int(eq[i][2:])
            if eq[i] == 'X':
                k = 1
            append_to_dict(c, d, u, k)

        elif eq[i] not in ['+', '-', '*']:
            if (i == 0 or eq[i - 1] == '+') \
                    and (i == len(eq) - 1 or eq[i + 1] in ['+', '-']):
                u = eq[i]
                try:
                    u = int(u)
                except ValueError:
                    u = float(u)
                append_to_dict(c, d, u, 0)
            elif eq[i - 1] == '-' \
                    and (i == len(eq) - 1 or eq[i + 1] in ['+', '-']):
                u = eq[i]
                try:
                    u = -int(u)
                except ValueError:
                    u = -float(u)
                append_to_dict(c, d, u, 0)

def solve(degree, d):
    if degree == 0:
        if d:
            print("There is no solution")
        else:
            print("All numbers are solutions")
        sys.exit(0)
    elif degree == 1:
        print("The solution is:")
        if 0 in d:
            print(-d[0], '/', d[1], '=', -d[0] / d[1])
        else:
            print("0")
    elif degree == 2:
        if 0 not in d:
            d[0] = 0
        if 1 not in d:
            d[1] = 0
        D = d[1] * d[1] - 4 * d[2] * d[0]
        print("Discriminant: " + str(D))
        if D < 0:
            print("Discriminant negative, there are two complex solutions:")
            print(str(-d[1] / (2 * d[2])) + " - " + str(abs(sqrt(-D) / (2 * d[2]))) + " * i")
            print(str(-d[1] / (2 * d[2])) + " + " + str(abs(sqrt(-D) / (2 * d[2]))) + " * i")
        elif D == 0:
            print("Discriminant null, the solution is:\n" + str(-d[1] / (2 * d[2])))
        else:
            print("Discriminant positive, the two solutions are:")
            print(-d[1] - sqrt(D), '/', 2 * d[2], '=', (-d[1] - sqrt(D)) / (2 * d[2]))
            print(-d[1] + sqrt(D), '/', 2 * d[2], '=', (-d[1] + sqrt(D)) / (2 * d[2]))
    else:
        print("The polynomial degree is strictly greater than 2, I can't solve")

if __name__ == "__main__":
    d, l = {}, []
    if len(sys.argv) < 2:
        print('Wrong argument')
        sys.exit(0)
    formule = sys.argv[1].upper()
    if not syntax_checking(formule):
        print('Syntax error')
        sys.exit(0)
    formule = formule.split('=')
    eqx, eqy = formule[0].split(), formule[1].split()
    upd_dict('+', eqx, d)
    upd_dict('-', eqy, d)
    for k in d:
        if d[k] == 0:
            l.append(k)
    for element in l:
        del d[element]
    print_reduced_form(d)
    degree = '0'
    if d:
        degree = str(max(d.keys()))
    print("Polynomial degree: " + degree)
    solve(int(degree), d)
