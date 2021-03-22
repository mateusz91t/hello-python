import algorytm_trojkat_silowy as ts





def write_neo(data_list: list) -> str:
    out = 'Create\n(we:Wezel {weight:-1, row:-1, element:-1}),\n'
    len_data = len(data_list)
    for row in range(len_data):
        for el in range(len(data[row])):
            out += '(w%re%r:Wezel {weight:%r, row:%r, element:%r}),\n' % (row, el, data[row][el], row, el)
    out += '(wxex:Wezel {weight:-2, row: -2, element: -2}),\n'
    out += '(we)-[:leads {cost:%r}]->(w0e0),\n' % data[0][0]
    for row in range(len_data-1):
        for el in range(len(data[row])):
            out += '(w%re%r)-[:leads {cost:%r}]->(w%re%r),\n' % (row, el, data[row+1][el], row+1, el)
            out += '(w%re%r)-[:leads {cost:%r}]->(w%re%r),\n' % (row, el, data[row+1][el+1], row+1, el+1)
    for el in range(len(data[-1])):
        out += '(w%re%r)-[:leads {cost:%r}]->(wxex),\n' % (len_data-1, el, 0)
    return out


data = ts.get_data(ts.mt)
print(data)
ve_s = write_neo(data)
print(ve_s)
