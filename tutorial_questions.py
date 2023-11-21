from tabulate import tabulate
from decimal import Decimal as D
import random


r = 'r'
q = 'q'
cw = 'cw'
p = 'p'
ans = ''


def q1(roll):
    data = []
    given = [1597, 1652, 1695, 1745, 1904]
    header = ['year', 'population']
    for i in range(0, len(given)):
        given[i] *= roll
        data.append([1971 + i * 10, given[i]])

    print('Given data: ')
    print(tabulate(data, headers=header))
    data.clear()
    print()
    print('Arithmetic Method')
    curr = given[-1]
    mean = ((curr-given[0])/4)
    for i in range(0, 4):
        item = [2011 + i * 10, curr + mean * i]
        data.append(item)

    print('Mean increase: ', mean)
    print(tabulate(data, headers=header))
    print()
    print('Geometric Method')
    data.clear()

    rate = 1
    for i in range(1, len(given)):
        rat = ((given[i] - given[i-1]) / given[i-1]) * 100
        print(f'r{i} = ', rat)
        rate *= pow(rat, 0.5)

    print('R mean =( r1 * r2 * r3 * r4 ) ^ 0.5')
    print('R mean: ', rate)
    print()
    print('Using P = P0 + (1 + r/100) ^ n')

    for i in range(0, 4):
        item = [2011 + i * 10, curr * pow((1 + rate/100), i)]
        data.append(item)

    print(tabulate(data, headers=header))
    print()
    print('Incremental Increase Method')
    data.clear()
    inc = []
    for i in range(1, len(given)):
        inc.append(given[i]-given[i-1])

    print('Increments: ', inc)

    incinc = 0

    for i in range(1, len(inc)):
        print(f'Difference between {i} and {i+1} increment: ', inc[i]-inc[i-1])
        incinc += inc[i]-inc[i-1]

    incinc /= (len(inc)-1)
    print('x bar (mean increment)', sum(inc)/len(inc))
    print('y bar (mean increment\'s increment)', incinc)
    print('Using P = P0 + (x bar) * t + (y bar) * (t * t+1)/2')

    for i in range(0, 4):
        item = [2011 + i * 10, curr + i * sum(inc)/len(given) + (i * (i+1)) / 2 * incinc]
        data.append(item)

    print(tabulate(data, headers=header))
    print('Source: https://www.youtube.com/watch?v=ytgoVjtf_MM')


def q2_helper(avg):
    return 1.8 * avg * 0.264172 * 1e-6


def q2(roll):
    rate = 3.5 * roll
    print('Growth rate: ', rate)
    curr = 280 * roll
    print('Current population', curr)
    avgpc = 135000 / 280
    mul = 2.641726e-7 * 1.8
    print('Consumption per person per day', avgpc)
    avg = 135000 * roll
    print('Current average consumption', avg)
    peak = q2_helper(avg)
    print('Current Peak Consumption = 1.8 * avg: ', 1.8 * avg)
    print('Mgd in 1 ltr: 0.264172 * 10^-6')
    print('Population after t years: P = P0 + r * t')
    print(f'Population after t years: P = {curr} + {rate} * t')
    print(f'average consumption after t years in mgd= P * {avgpc} * 2.641726e-7')
    print(f'Solve for P * {avgpc} * 2.641726e-7 = 5')
    t = ((5 / (avgpc * mul)) - curr) / rate
    print('T in years = ', max(0, t))

    print('Optional (data to verify)')

    data = []
    header = ['year', 'population', 'average demand', 'peak demand']

    year = 1
    item = [year, curr, f'{avg * 1e-6 * 0.264172} mgd', f'{peak} mgd']
    data.append(item)
    while peak <= 5:
        curr += rate
        avg = avgpc * curr
        peak = q2_helper(avg)
        year += 1
        item = [year, curr, f'{avg*1e-6*0.264172} mgd', f'{peak} mgd']
        data.append(item)

    print(tabulate(data, headers=header))


def q3(roll):
    demand = [6, 3, 2, 1, 11, 25, 65, 38, 60, 55, 65, 45, 18, 46, 26, 9, 5, 14, 40, 45, 25, 45, 18, 8]
    header = ['hour', 'demand', 'cumulative demand', 'cumulative supply', 'excess supply', 'excess demand']
    for i in range(0, len(demand)):
        demand[i] *= roll

    print('Demands: ', demand)

    data = []
    cumd = 0
    cums = 0
    rate = D("28.125") * roll
    print('Supply rate', rate)
    mexcs = -999999999
    mexcd = -999999999

    for i in range(0, len(demand)):
        cumd += demand[i]
        cums += rate
        if cums > cumd:
            excs = cums - cumd
            excd = 0
        else:
            excs = 0
            excd = cumd - cums

        mexcs = max(mexcs, excs)
        mexcd = max(mexcd, excd)

        item = [f'{i}-{i+1}', demand[i], cumd, cums, excs, excd]
        data.append(item)

    print(tabulate(data, headers=header))
    print()
    print('Capacity Required = Max Excess Supply + Max Excess Demand')
    print('Capacity Required = ', mexcs, ' + ', mexcd)
    print('Capacity Required = ', mexcs + mexcd)
    print('Source: https://www.youtube.com/watch?v=-7mIGJa120U')


def q4(roll):
    l1 = 120 * roll
    l2 = 75 * roll
    l3 = 60 * roll
    d1 = D("0.075") * roll
    d2 = D("0.060") * roll
    d3 = D("0.045") * roll
    de = D("0.045") * roll

    print('Leq/Deq^5 = ', l1, '/', d1, '^5 + ', l2, '/', d2, '^5 + ', l3, '/', d3, '^5')
    print('Leq/', de, '^5 = ', l1, '/', d1, '^5 + ', l2, '/', d2, '^5 + ', l3, '/', d3, '^5')
    print('Leq/', pow(de, 5), ' = ', l1, '/', pow(d1, 5), ' + ', l2, '/', pow(d2, 5), ' + ', l3, '/', pow(d3, 5))
    print('Leq/', de**5, ' = ', l1/d1**5, ' + ', l2/d2**5, ' + ', l3/d3**5)
    print('Leq/', de**5, ' = ', l1/d1**5+l2/d2**5+l3/d3**5)
    print('Leq = ', (l1/d1**5+l2/d2**5+l3/d3**5)*de**5)
    print('Source: https://www.youtube.com/watch?v=DsNAqSN8xHk')


def q5_helper(itr, loops, common, depth):
    if itr == depth:
        return
    print('Iteration: ', itr)
    header = ['S.no.', 'Pipe', 'r', 'Q0', 'rQ0^2', '2rQ0', 'Q1']

    for i in range(0, len(loops)):
        loop1 = i == 0
        print('Loop', i+1)
        pipes = loops[i]
        data = []
        srq2 = 0
        strq = 0

        for i in range(0, len(pipes)):
            pipe = pipes[i]
            item = [i+1, pipe[p], pipe[r], pipe[q]]
            rq2 = pipe[r] * pipe[q] * pipe[q]
            if not pipe[cw]:
                rq2 *= -1
            srq2 += rq2
            trq = 2 * pipe[r] * pipe[q]
            strq += trq
            item.append(rq2)
            item.append(trq)
            data.append(item)

        dq = -1 * srq2 / strq

        for i in range(0, len(pipes)):
            item = data[i]
            nq = pipes[i][q]
            if pipes[i][cw]:
                nq += dq
            else:
                nq -= dq
            pipes[i][q] = nq
            if loop1:
                loops[1][common][q] = nq
            else:
                loops[0][common][q] = nq
            item.append(nq)

        data.append(['sum', '', '', '', srq2, strq, ''])
        print(tabulate(data, headers=header))
        print('Delta Q:', dq)
        print()

    q5_helper(itr+1, loops, common, depth)


def q5(roll, iterations):
    print('9 iterations are there, leave when delta q is close to 0 or at 3-4 iterations')
    print('randomized initial flow are used so if too many zeros appear, consider rerunning')

    ab = {
        p: 'ab',
        r: 120,
        q: random.randint(2, 4),
        cw: True
    }

    ad = {
        p: 'ad',
        r: 200,
        q: 5-ab[q],
        cw: False
    }

    bc = {
        p: 'bc',
        r: 300,
        q: random.randint(1, ab[q]),
        cw: True
    }

    bd = {
        p: 'bd',
        r: 400,
        q: ab[q]-bc[q],
        cw: True
    }

    cd = {
        p: 'cd',
        r: 150,
        q: ad[q]+bd[q]-2,
        cw: False
    }

    bd2 = {
        p: 'bd',
        r: 400,
        q: ab[q]-bc[q],
        cw: False
    }

    x = [ab, ad, bc, bd, cd]
    for i in range(0, len(x)):
        print(f'{x[i][p]}: {x[i][q]}N')
        x[i][q] *= roll

    loop1 = [ab, ad, bd]
    loop2 = [bc, cd, bd2]

    q5_helper(1, [loop1, loop2], -1, iterations)
    print('Source: https://www.youtube.com/watch?v=RMU-2cLw0V4')


def allq(roll):
    print('Q1')
    q1(roll)
    print('***********************************************\n\n')
    print('Q2')
    q2(roll)
    print('***********************************************\n\n')
    print('Q3')
    q3(roll)
    print('***********************************************\n\n')
    print('Q4')
    q4(roll)
    print('***********************************************\n\n')
    print('Q5')
    q5(roll, 10)
    print('***********************************************\n\n')


if __name__ == '__main__':
    n = int(input('Enter roll number in digits (eg 106 for 2k20/co/106): '))
    allq(n)
