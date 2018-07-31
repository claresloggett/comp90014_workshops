import numpy as np

def traceback(a,b,scoregrid,indel_score=-1, match_score=2, mismatch_score=-1):
    """
    Traceback for global alignment.
    Returns a top-scoring trace. If multiple traces are possible for the
    top alignment score, this function will return just one of them, arbitrarily.
    """
    X,Y = scoregrid.shape
    assert X==len(a)+1
    assert Y==len(b)+1
    x, y = X-1, Y-1
    # Start with an empty trace
    trace = []
    # Trace back until we reach the top-left corner
    while x>0 or y>0:
        current_score = scoregrid[x,y]
        # Note that we have to compare a[x-1] to b[y-1] again, and compare scores,
        # but only along the path, not for every cell of the grid, i.e. O(N) not O(N^2)
        if a[x-1]==b[y-1]:
            match_mismatch_score = match_score
        else:
            match_mismatch_score = mismatch_score
        # Here we pick just one operation, so we'll only trace one path
        if x>0 and y>0 and scoregrid[x-1,y-1]+match_mismatch_score == current_score:
            # Do a match or mismatch at this step: 
            #  add a letter to both alignment strings, 
            #  and go from x-1, y-1
            trace.append((a[x-1],b[y-1]))
            x -= 1
            y -= 1
        elif x>0 and scoregrid[x-1,y]+indel_score == current_score:
            # Do a deletion at this step: 
            #  add a letter to the first alignment string but a '-' to the second string,
            #  and go from x-1
            trace.append((a[x-1],'-'))
            x -= 1
        elif y>0 and scoregrid[x,y-1]+indel_score == current_score:
            # Do an insertion at this step: 
            #  add a letter to the second alignment string but a '-' to the first string,
            #  and go from y-1
            trace.append(('-',b[y-1]))
            y -= 1
        else:
            raise ValueError("No valid trace found")
    
    return trace[::-1]

def traceback_local(a,b,scoregrid,indel_score=-1, match_score=2, mismatch_score=-1):
    """
    Traceback for local alignment.
    Here we start from a highest-scoring cell in the grid, and stop when we reach a zero.
    Returns a top-scoring trace. If multiple traces are possible for the
    top alignment score, this function will return just one of them, arbitrarily.
    """
    X,Y = scoregrid.shape
    assert X==len(a)+1
    assert Y==len(b)+1
    # Find the highest-scoring square to start
    # If there is more than one, we pick one arbitrarily
    # (better would be to return all traces)
    x,y = np.unravel_index(np.argmax(scoregrid, axis=None), scoregrid.shape)
    # Start with an empty trace
    trace = []
    # Trace back until we reach the top-left corner
    while x>0 or y>0:
        current_score = scoregrid[x,y]
        if current_score==0:
            # We've finished our local alignment
            break
        # Note that we have to compare a[x-1] to b[y-1] again, and compare scores,
        # but only along the path, not for every cell of the grid, i.e. O(N) not O(N^2)
        if a[x-1]==b[y-1]:
            match_mismatch_score = match_score
        else:
            match_mismatch_score = mismatch_score
        # Here we pick just one operation, so we'll only trace one path
        if x>0 and y>0 and scoregrid[x-1,y-1]+match_mismatch_score == current_score:
            # Do a match or mismatch at this step: 
            #  add a letter to both alignment strings, 
            #  and go from x-1, y-1
            trace.append((a[x-1],b[y-1]))
            x -= 1
            y -= 1
        elif x>0 and scoregrid[x-1,y]+indel_score == current_score:
            # Do a deletion at this step: 
            #  add a letter to the first alignment string but a '-' to the second string,
            #  and go from x-1
            trace.append((a[x-1],'-'))
            x -= 1
        elif y>0 and scoregrid[x,y-1]+indel_score == current_score:
            # Do an insertion at this step: 
            #  add a letter to the second alignment string but a '-' to the first string,
            #  and go from y-1
            trace.append(('-',b[y-1]))
            y -= 1
    
    return trace[::-1]

def get_alignment(trace):
    """
    Convert a trace to a pair of strings representing the alignment.
    """  
    aligned_string_a = ''.join([c1 for (c1,c2) in trace])
    aligned_string_b = ''.join([c2 for (c1,c2) in trace])
    return (aligned_string_a, aligned_string_b)