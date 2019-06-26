J = [4, 4, 4, 9, 10, 11, 12]
p = 3

i = 0

from typing import List, Dict

def gen_seq(j_list: List[int], p: int) -> Dict[float, float]:
    """Generates a sequence of tuples from a list & returns the min-max means
    """ 
    sequences = []
    for ind, val in enumerate(j_list):
        end_range = ind + p
        sequence = j_list[ind:end_range]
        if len(sequence) == p:
            sequences.append(sequence)
    avgs = [sum(sequence)/len(sequence) 
            for sequence in sequences]
    
    output = {}
    output["min"] = min(avgs)
    output["max"] = max(avgs)

    return output

print (gen_seq(j_list=J, p=p))
        #print(f"The val {val} has an ind of {ind}")

#gen_seq(J,p)

# toys = [[1, 2, 3], [4, 5, 6], [100, 300, 700]]
# avg = [sum(toy)/len(toy) for toy in toys]
# print(f"""
# The average of each sequence is {avg}.

# The min average is {min(avg)}.

# The max average is {max(avg)}.
# """)