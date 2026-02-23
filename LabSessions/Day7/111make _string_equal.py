def make_it_equal(A, B):
    if "%" not in A:
        return "" if A == B else -1
    p = A.index("%")
    pre = A[:p]
    suf = A[p+1:]
    if not B.startswith(pre) or not B.endswith(suf):
        return -1
    if len(B) < len(pre) + len(suf):
        return -1
    return B[len(pre):len(B)-len(suf)]
