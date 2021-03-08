def flatten(list_to_flat: list):
    def wew(list_in: list, start_ind: int = 0):
        for index in range(start_ind, len(list_in)):
            if isinstance(list_in[index], list):
                start_ind = index
                l1 = list_in.pop(index)
                for ins_to in range(index, index + len(l1)):
                    list_in.insert(ins_to, l1.pop(0))
                wew(list_in, start_ind)
        return list_in
    return wew(list_to_flat)
