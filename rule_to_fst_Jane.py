import itertools

class FST:
   def __init__(self, states, transitions, initial, finalouts):
      self.Q = states
      self.delta = transitions
      self.q0 = initial
      self.rho = finalouts
   def deltaf (self,q,i):           # gives the output from q on i
      for t in self.delta:
         if t[0] == q and t[1] == i:
            return (t[2],t[3])
   def rhof (self,q):         # gives the final output for q
      for x in self.rho:
         if x[0] == q:
            return x[1]
      return 'undefined'
def find_trans(q,a):
   for d in delta:
      if d[0] == q and d[1] == a:
         return d
def find_qtrans (q):
   trans = set()
   for d in delta:
      if d[0] == q:
         trans.add(d)
   return trans

# returns a set of prefixes of input string w
def prefixes(w):
   pref = set()
   l = len(w)
   i = 1
   while i < l+1:
      pref.add(w[0:i])
      i += 1
   return pref

def prefixes_set(S):
   pref = set()
   for s in S:
      pref.update(prefixes(s))
   return pref

# returns a set of prefixes of input string w, except for w itself
def prefixes_minus(w):
   pref = set()
   l = len(w)
   i = 1
   while i < l:
      pref.add(w[0:i])
      i += 1
   return pref

# returns the max length string common to the two input sets
def lcstr (s1, s2):
    inter = s1.intersection(s2)
    if not inter:
        return ''
    else:
        return max (inter)

# returns the set of suffixes for the input string s
def suffixes (s):
    i = len(s)
    suffixes = set()
    j = 0
    while (j < i+1):
        suffixes.add(s[j:])
        j += 1
    return suffixes

# returns the k-1 length suffix of a string s, or s if len(s) < k-1
def suffix_n (s,n):
   i = len(s)
   if i < n:
      return s
   else:
      return s[i-n:]


# Functions for printing FST in .dot format ------------------------------
def lookup_index (Q,l):
   for q in Q:
      if q[0] == l:
         return str(q[1])

def print_FST (f):
   print ("digraph G { rankdir = LR")

   i = 0
   indexed_states = []
   for q in f.Q:
      q_index = [q, i]
      indexed_states.append(q_index)
      finals = f.rhof(q)
      if finals == 'undefined':
         print (str(i) + "[label=\"" + q + "\",shape=doublecircle]")
      else:
         print (str(i) + "[label=\"" + q + ',' + finals + "\",shape=doublecircle]")
      i += 1

   for d in f.delta:
      print (lookup_index(indexed_states, d[0]) + "->"+ lookup_index(indexed_states,d[3])+ "[label = \"" + d[1] + ":" + d[2] + "\"]")

   print ("}")
#--------------------------------------------------------------------------

# Alphabet
Sigma = set(['T','D','V','N'])

# Rule format is X -> Y / U_V
# Example rule: T -> D / V_V
U = set(['V'])
V = set(['V'])
XY = set([('T','D')])

# Instead of a single uxv string, we need a set, one for each x,y pair, for each combination of lc and rc

UXV = set()
H = set()

for u in U:
   for xy in XY:
      for v in V:
         UXV.add(u+xy[0]+v)
         H.add(xy[0]+v)

# Assuming all strings in each set U, V are the same length, we can determine the k value by adding these lengths (otherwise we add the max length of the set).  These individual lengths will also be used in the delta function construction.

len_u = len(max(U,key=len))
len_v = len(max(V,key=len))

# For the length of x, pop an example, get its length and then return it to the set
ex_x = XY.pop()
len_x = len(ex_x[0])
XY.add(ex_x)

k = len_u + len_v + len_x

# Need a way to lookup the corresponding y for an x

def lookupy (x):
   for xy in XY:
      if xy[0] == x:
         return xy[1]
   return 'not found'

# Returns the index of the last occurence of a string in U
def contains_last_u (q):
   i = 0
   if U == set(['']):
      return i
   i = len(q)-len_u
   while i > -1:
      if q[i:i+len_u] in U:
         return i
      i -= 1
   return "not found"

def contains_u (q):
   i = 0
   if U == set(['']):
      return i
   else:
      while i < len(q):
         if q[i:i+len_u] in U:
            return i
         i += 1
   return "not found"


# State set - initially just the start state lambda and word-initial boundary

# The states are substrings up to k-1

Q = set(['&#955;'])
j = 1

for w in UXV:
   Q.update(prefixes_minus(w))

# This function returns the string being held in the input state q; if q is not a holding state it will return lambda
def held_string (q):
   u = contains_u(q)
   if u == "not found":
      return ''
   for h in H:
      if q[u+len_u:] in prefixes_minus(h):
         return q[u+len_u:]
   u2 = contains_last_u(q)
   for h in H:
      if q[u2+len_u:] in prefixes_minus(h):
         return q[u2+len_u:]
   return ''


# Build the final output function
rhof = set()

for q in Q:
   if q == '&#955;':
      rhof.add((q,'&#955;'))
   elif q+'#' in UXV:
      just_v = q[len_u+len_x:]
      if len_x == 0:
         x = XY.pop()
         y = x[1]
         XY.add(x)
      else:
         if len_u == 0:
            just_x = q[:k-(len_v-1)]
         else:
            just_x = q[len_u:k-(len_v-1)]
         y = lookupy(just_x)
      rhof.add((q,y+just_v))
   else:
      rhof.add((q, held_string(q)))


# Add transitions from each state on each alphabet symbol (numbers in comments correspond to explanations in chapter 3)

lambd = '&#955;'

mode = 'S'

delta = set()

for q in Q:
   for a in Sigma:

# (4)
      if q == lambd:
         qp = suffix_n(a,k-1)
         if U == set(['']):
            check = 0
            for h in H:
               if a in prefixes_minus(h):
                  delta.add((q,a,lambd,a,'4a'))
                  check = 1
                  break
            if check == 0:
               if qp in Q:
                  delta.add((q,a,a,qp))
               else:
                  delta.add((q,a,a,lambd))
         else:
            if qp in Q:
               delta.add((q,a,a,qp))
            else:
               delta.add((q,a,a,lambd))

# (3) If the next state is one of the uxv strings,
      elif q+a in UXV:
         just_u = (q+a)[:len_u]
         just_v = (q+a)[len_u+len_x:]
         if len_x == 0:
            x = XY.pop()
            y = x[1]
            XY.add(x)
         else:
            if len_u == 0:
               just_x = (q+a)[:(k-len_v)]
            else:
               just_x = (q+a)[len_u::(k-len_v)]
            y = lookupy(just_x)

         if mode == 'LR':
            qp = suffix_n(just_u+y+just_v,k-1)
            if qp in Q:
               t = held_string(qp)
               r = lcstr(suffixes(y+just_v),prefixes(t))
               delta.add((q,a,(y+just_v)[:len(y+just_v)-len(r)],qp))
            else:
               delta.add((q,a,(y+just_v),lambd))

         else:
            qp = suffix_n(q+a,k-1)
            if qp in Q:
               if len_v == 0 and len_x == 0:
                  held_in_dest = held_string(qp)
                  keep_holding = lcstr(suffixes(a+y),prefixes(held_in_dest))
                  delta.add((q,a,(a+y)[:len(a+y)-len(keep_holding)],qp))
               elif len_v == 0:
                  held_in_dest = held_string(suffix_n(qp))
                  keep_holding = lcstr(suffixes(y),prefixes(held_in_dest))
                  delta.add((q,a,y[:len(y)-len(keep_holding)],qp))
               else:
                  r = lcstr(suffixes(y+just_v),prefixes(held_string(qp)))
                  delta.add((q,a,(y+just_v)[:len(y+just_v)-len(r)],qp))
            else:
               delta.add((q,a,(y+just_v),lambd))

# If you've seen a string in U
      elif contains_u(q) != "not found":
         check = 0
         i = contains_last_u(q)
         for h in H:
            if q[i+1:]+a in prefixes_minus(h):
               # special case: a creates self loop on q. This means a is the last needed symbol, so it's already being held.
               if suffix_n(q+a,k-1) == q:
                  delta.add((q,a,a,q))
               else:
# (1) and q starting after u ends + a is a prefix of some h = xv in XV
                  o = held_string(q)+a
                  if mode == 'LR':
                     qp = suffix_n(q+o,k-1)
                     t = held_string(qp)
                     r = lcstr(suffixes(o),prefixes(t))
                     if qp in Q:
                        delta.add((q,a,o[:len(o)-len(r)],qp))
                     else:
                        delta.add((q,a,o,lambd))
                  else:
                     qp = suffix_n(q+a,k-1)
                     t = held_string(qp)
                     r = lcstr(suffixes(o),prefixes(t))
                     if qp in Q:
                        delta.add((q,a,o[:len(o)-len(r)],qp))
                     else:
                        delta.add((q,a,o,lambd))
               check = 1
               break
# (2) and q starting after u ends + a is not a prefix of some h = xv in XV
         if check == 0:
            o = held_string(q)+a
            if mode == 'LR':
               qp = suffix_n(o,k-1)
               t = held_string(qp)
               r = lcstr(suffixes(o),prefixes(t))
               if qp in Q:
                  delta.add((q,a,o[:len(o)-len(r)],qp))
               else:
                  delta.add((q,a,o,lambd))
            else:
               qp = suffix_n(q+a,k-1)
               t = held_string(qp)
               r = lcstr(suffixes(o),prefixes(t))
               if qp in Q:
                  delta.add((q,a,o[:len(o)-len(r)],qp))
               else:
                  delta.add((q,a,o,lambd))

# (4) Otherwise we just move the window, again holding output if needed based on the destination state

      else:
         qp = suffix_n(q+a,k-1)
         if qp in Q:
            delta.add((q,a,a,qp))
         else:
            delta.add((q,a,a,lambd))

#T1 = FST(Q,delta,lambd,rhof)

T1 = FST(Q,delta,'#',rhof)

print_FST(T1)

#print T1.Q

#print T1.delta

'''AI--------------------------------------------------------------------------
    Rules for language 17
--------------------------------------------------------------------------AI'''
# If there is a suffix, hyphenate
# Check if i is the only type of vowel in the stem
#     if not, run stem + suffix through 17
#     if yes, don't process the stem. Input the suffix into 17P. Output is the stored stem + output of 17P
