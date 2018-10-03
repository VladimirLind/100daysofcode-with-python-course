from data import us_state_abbrev, states_list

NOT_FOUND = 'N/A'

def get_every_nth_state(states=states_list, n=10):
    """Return a list with every nth item (default argument n=10, so every
       10th item) of the states list above (remember: lists keep order)"""
    return [states[i] for i in range(n-1,50,n)]


def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
    """Look up a state abbreviation by querying the us_state_abbrev
       dict by full state name, for instance 'Alabama' returns 'AL',
       'Illinois' returns 'IL'.
       If the state is not in the dict, return 'N/A' which we stored
       in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
    try:
        return us_state_abbrev.pop(state_name)
    except KeyError:
        return NOT_FOUND


def get_longest_state(data):
    """Receives data, which can be the us_state_abbrev dict or the states
       list (see above). It returns the longest state measured by the length
       of the string"""
    return sorted(data, key=len,reverse=True)[0]
        


def combine_state_names_and_abbreviations(us_state_abbrev=us_state_abbrev,
                                          states=states_list):
    """Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
       the us_state_abbrev dict, and the last 10 states from the states
       list (see above) and combine them into a new list without losing
       alphabetical order"""
    return sorted(us_state_abbrev.values())[:10]+(sorted(states)[-10:])

if __name__ == "__main__":
    
    print([(k,v) for k,v in us_state_abbrev.items()][9])
    print(states_list[9])
    print([k for k in us_state_abbrev.keys()][44])
    print([v for v in us_state_abbrev.values()][26])

