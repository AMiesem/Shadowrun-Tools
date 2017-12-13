#!/usr/bin/env python3

#simple program to roll success tests and display them in a table

from dice.successtest import SuccessTest

st = SuccessTest()

POOL = 5
THRESHOLD = st.AVERAGE
ROLLS = 5

#Edge test?
EDGE = False

st.pool = POOL
st.threshold = THRESHOLD
st.edge = EDGE

if EDGE:
    print('Edge Test -- Rule of Six is active\n')

template = "{:^5} {:^15} {:^6} {:<40}"
print(template.format('HITS','RESULT','GLITCH','ROLLS'))
print(template.format('_'*5, '_'*15, '_'*6, '_'*(POOL*3)))

for roll in range(ROLLS):
    result, glitch, crit, rolls = st.rollTest()
    col1 = '{:>5} {:>15} {:^6} '
    cols = '{:2} '
    if glitch:
        glitch_txt = 'YES'
    else:
        glitch_txt = 'NO'

    hit_count =rolls.count(5) + rolls.count(6)

    if result:
        print(col1.format(hit_count, 'HIT',glitch_txt),end='')
    elif crit:
        print(col1.format(hit_count, 'CRITICAL GLITCH',glitch_txt),end='')
    else:
        print(col1.format(hit_count, 'MISS',glitch_txt),end='')

    for result in rolls:
        print(cols.format(result),end='')

    print()
