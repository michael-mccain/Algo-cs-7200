### Imports ###
from pathlib import Path
import itertools

### Functions ###
# Read input file, return dictionary and integer from first line
def read_file(in_file):
    final_dict = {}
    with open(in_file, 'r') as file:
        match_int = file.readline().strip()
        lines = file.read()
        names = lines.strip().split('\n')

    for name in names: # Populate name dictionary
        x = name.split(' ')
        final_dict.update({x[0] : x[1:(len(x))]})

    return int(match_int), final_dict

### MAIN ###
def main():
    ### Variables ###
    # Path Variables
    in_file = Path(__file__).parent / 'Input.txt'
    out_path = Path(__file__).parent

    # Other variables
    name_dict = {} # Intialized list of all names
    proposer_dict = {} # Intialized list of propser preference
    proposee_dict = {}  # Initilaized list of propsee preference
    unmatched_proposers = [] # Initlaized List of unmatched propsers
    matched_proposees = [] # initialized list for matched proposees
    engaged_pairs = [] # list of tuples of (proposer, proposee)
    match_count = 0

    # Read Input.txt to get dictionary and match count
    match_count, name_dict = read_file(in_file)

    proposer_dict = dict(itertools.islice(name_dict.items(), 0, match_count)) # populate proposer dictionary (Men)
    proposee_dict = dict(itertools.islice(name_dict.items(), match_count,len(name_dict))) # Populate propsee dictionary (Ladies)

    print('Men: ', proposer_dict)
    print('Women: ', proposee_dict)

    for key in proposer_dict.keys():    # Populate unmatched list for while condition
        unmatched_proposers.append(key)


    # While there is a man m who is free and hasn’t proposed to
    # every woman w for which (m, w) ~F
    while (len(unmatched_proposers) != 0):

        # choose the man; he has not yet proposed; always get the "head" of list.
        # We don't pop/remove until he is matched
        man_chosen = unmatched_proposers[0]

        #print(f"man chosen is: {man_chosen}")

        #print(f"matched proposees list is: {matched_proposees}")

        # get the man's preference list
        man_chosen_pref_list = proposer_dict[man_chosen]

        #print(f"man chosen pref list is: {man_chosen_pref_list}")

        # man goes through his pref list which will be updated
        while (len(man_chosen_pref_list) != 0):

            # let w be the highest ranked woman in m's pref list
            # that m has not yet proposed to
            woman_chosen = man_chosen_pref_list.pop(0)

            #print(f"woman chosen is {woman_chosen}")

            # if w is free, then m, w become engaged
            # remove m, w, from unmatched proposer/proposee list
            # add engaged_pair to engaged_pairs list
            if (woman_chosen not in matched_proposees):
                #print("{woman_chosen} is NOT IN matched_proposees; is free, will add")

                engaged_pair = (man_chosen, woman_chosen)

                #print(f"unmatched proposers in if woman chosen block is: {unmatched_proposers}")
                #print(f"man chosen to remove right before remove: {man_chosen}")

                unmatched_proposers.remove(man_chosen)
                matched_proposees.append(woman_chosen)
                engaged_pairs.append(engaged_pair)

                #print("exiting out of if woman chosen block by doing break")
                break
            else:
                # Else w is currently engaged to m'
                # find the pair and get m'
                for (each_man, each_woman) in engaged_pairs:
                    if (each_woman == woman_chosen):
                        man_already_chosen = each_man

                        # get pref positions of man already chosen (m') vs current man chosen (m)
                        pref_man_already_chosen = proposee_dict[woman_chosen].index(man_already_chosen)
                        pref_man_chosen = proposee_dict[woman_chosen].index(man_chosen)

                        # w prefers m to m'
                        # (index of man_chosen is smaller than index of man already chosen, i.e, higher in pref list)
                        # put m' in unmatched_proposers list, delete old engaged pair and add new pair in engaged_list
                        if (pref_man_chosen < pref_man_already_chosen):

                            # put m' in unmatched proposers list
                            unmatched_proposers.append(man_already_chosen)

                            # remove the old pair out
                            engaged_pairs.remove((man_already_chosen, woman_chosen))

                            # put the new pair in
                            engaged_pairs.append((man_chosen, woman_chosen))

                            # remove m from unmatched proposers list
                            unmatched_proposers.remove(man_chosen)

            #print("going to next man!!!!")


    print(f"final list is: {engaged_pairs}")














if __name__ == "__main__":
    main()
