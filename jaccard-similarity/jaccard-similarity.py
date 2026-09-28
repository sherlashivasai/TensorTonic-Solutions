def jaccard_similarity(set_a: list, set_b: list) -> float:
    """
    Returns the Jaccard similarity of the two item collections.
    """
    # Write code here
    """
    assume set_a contains 10 movie tickets, set_b contains 20 movie tickets and there are 5 movie tickets present in both sets, then the {set_a | set_b} = 25 tickets, {set_a & set_b = 5}. 
    The similarity between these two sets is = len(set_a & set_b)/len(set_a | set_b)
    i.e. score = (5)/ (25)
     -> since, Similarity score = 0.2

     * jaccard Similarity can be used to know ,how well the both matches without considering the magnitude . and it is useful while dealing with set type of data.
     0 - not similar
     1 = highly similar 
     range -{0,1}
    """
    set_a = set(set_a)
    set_b = set(set_b)
    matched_len = len(set_a&set_b)

    union_len = len(set_a | set_b) 
    if union_len == 0:  # edge case, zerodivison error
        return 0.0

    return float(matched_len/union_len) 