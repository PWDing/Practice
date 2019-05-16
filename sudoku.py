import random


# Cross product of elements in A and elements in B.
def cross(list_a, list_b):
    return [a + b for b in list_b for a in list_a]


"""
大多数数独爱好者用 A-Z 表示行，用 1-9 表示列
一个小九宫格称为一个单元,一个数独中有9个单元
与某个方格在同一行、同一列或者同一个单元的其他方格称为该方格的搭档
每个方格都有20个搭档
"""
rows = 'ABCDEFGHI'
cols = '123456789'
digits = cols
cells = cross(rows, cols)
# 生成所有的单元和行、列
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') 
            for cs in ('123', '456', '789')])
# 对每一个方格，求出与它相关的单元
units = dict((cell, [unit for unit in unitlist if cell in unit]) 
             for cell in cells)
# 对每一个方格，求出它所有的搭档
peers = dict((cell, set([cell for unit in units[cell] for cell in unit])) 
             for cell in cells)


# Convert grid into a dict of {cell: digit_string} with '0' or '.' for empty.
def convert_grid_to_dict(grid):
    values = [cell for cell in grid if cell in digits or cell in '0.']
    assert len(values) == 81
    return dict(zip(cells, values))


# Convert grid to a dict of possible values, {cell: digits}
# or return False if a contradiction is detected.
def parse_grid(grid):
    # To start, every square can be any digit
    # then assign values from the grid.
    grid_dict = dict((cell, digits) for cell in cells)
    for c, d in convert_grid_to_dict(grid).items():
        # Fail if we can't assign digit d to cell c
        if d in digits and not assign(grid_dict, c, d):
            return False
    return grid_dict


def assign(dicts, cell, digit):
    """
    Eliminate all the other values (except digit) from dicts[cell] and propagate.
    Return dicts, except return False if a contradiction is detected.
    """
    other_dicts = dicts[cell].replace(digit, '')
    if all(eliminate(dicts, cell, v) for v in other_dicts):
        return dicts
    else:
        return False


def eliminate(dicts, c, d):
    """
    Eliminate d from dicts[c]; propagate when values or places <= 2.
    Return dicts, return False except if a contradiction is detected.
    """
    # Already eliminated
    if d not in dicts[c]:
        return dicts
    dicts[c] = dicts[c].replace(d, '')

    # If a cell c is reduced to one value v
    # then eliminate value d from the peers.
    if len(dicts[c]) == 0:
        # COntradiction: removed all values
        return False
    elif len(dicts[c]) == 1:
        v = dicts[c]
        if not all(eliminate(dicts, p, v) for p in peers[c]):
            return False

    # If a unit u is reduced to only one place for a value d
    # then put it there.
    for u in units[c]:
        places = [c for c in u if d in dicts[c]]
        # Contradiction: no place for this value
        if len(places) == 0:
            return False
        elif len(places) == 1:
            # d can only be in one place in unit, assign it there
            if not assign(dicts, places[0], d):
                return False
    return dicts


# Display these values as a 2-D grid.
def display(dicts):
    width = max(len(dicts[cell]) for cell in cells) + 1
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in rows:
        print(''.join(dicts[row + col].center(width) +
              ('|' if col in '369' else '')for col in cols))
        if row in 'CFI':
            print(line)


print(display(parse_grid('4.....8.5.3..........7......2....\
    .6.....8.4......1.......6.3.7.5..2.....1.4......')))
