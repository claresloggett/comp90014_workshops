
def traceback(a,b,scoregrid,x=None,y=None,
              indel_score=-1, match_score=2, mismatch_score=-1):
    """
    Trace back recursively from given coordinates.
    Returns a list of top-scoring traces. If only one trace is possible
    for the top score, returns a list containing just one trace.
    If x and y are none, they will be set to the bottom-right corner of
    the grid.
    """
    X,Y = scoregrid.shape
    assert X==len(a)+1
    assert Y==len(b)+1
    if x==0 and y==0:
        # We have reached the end of the traceback
        # return a list containing one trace, where that starting trace
        # is just a tuple of two empty strings
        return [[('','')]]
    # Start at bottom right if coordinates not specified yet
    if x is None:
        x = X-1
    if y is None:
        y = Y-1
    # Make a list of possible paths to follow from x,y
    # Include any of the three cells where we could have got the current score
    # Perform a trace from each of those cells
    # Each traceback will return a list of paths; concatenate these lists
    # Note that we have to compare a[x-1] to b[y-1] again, but only along the path,
    # not for every cell of the grid, i.e. O(N) not O(N^2)
    current_score = scoregrid[x,y]
    if a[x-1]==b[y-1]:
        match_mismatch_score = match_score
    else:
        match_mismatch_score = mismatch_score
    traces = []
    if x>0 and scoregrid[x-1,y]+indel_score == current_score:
        # Do a deletion at this step: 
        #  add a letter to the first alignment string but a '-' to the second string,
        #  and go from x-1
        deletion_traces = traceback(a,b,scoregrid,x-1,y,indel_score,match_score,mismatch_score)
        traces += [trace + [(a[x-1],'-')] for trace in deletion_traces]
    if y>0 and scoregrid[x,y-1]+indel_score == current_score:
        # Do an insertion at this step: 
        #  add a letter to the second alignment string but a '-' to the first string,
        #  and go from y-1
        insertion_traces = traceback(a,b,scoregrid,x,y-1,indel_score,match_score,mismatch_score)
        traces += [trace + [('-',b[y-1])] for trace in insertion_traces]
    if x>0 and y>0 and scoregrid[x-1,y-1]+match_mismatch_score == current_score:
        # Do a match or mismatch at this step: 
        #  add a letter to both alignment strings, and go from
        #  and go from x-1, y-1
        match_mismatch_traces = traceback(a,b,scoregrid,x-1,y-1,indel_score,match_score,mismatch_score)
        traces += [trace + [(a[x-1],b[y-1])] for trace in match_mismatch_traces]

    return traces


def get_alignment(trace):
    """
    Convert a trace to a pair of strings representing the alignment.
    """  
    aligned_string_a = ''.join([c1 for (c1,c2) in trace])
    aligned_string_b = ''.join([c2 for (c1,c2) in trace])
    return (aligned_string_a, aligned_string_b)