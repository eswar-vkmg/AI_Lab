from collections import deque

def solve(domain, adj):
    q = deque(list(adj.keys()))
    
    while(q):
        curr_node = q.popleft()
        domain[curr_node] = list(domain[curr_node][0])
        
        for dest_node in adj[curr_node]:
            colors = domain[dest_node]
            if(domain[curr_node][0] in colors):
                colors.remove(domain[curr_node][0])
            

if __name__ == "__main__":
    adj, ad = dict(), dict()
    adj['q'] = ['nt', 'nsw', 'sa']
    adj['sa'] = ['wa', 'nt', 'q', 'nsw', 'v']
    adj['nsw'] = ['sa', 'q', 'v']
    adj['nt'] = ['wa', 'sa', 'q']
    adj['wa'] = ['nt', 'sa']
    adj['v'] = ['sa', 'nsw']
    adj['t'] = []
    temp = sorted(adj, key = lambda ele : len(adj[ele]), reverse = True)
    for ele in temp:
        ad[ele] = adj[ele][:]
    domain =  dict()
    colors = ['r', 'g', 'b']
    for key in ad.keys():
        domain[key] = colors[:]
    solve(domain, adj)
    print(domain)