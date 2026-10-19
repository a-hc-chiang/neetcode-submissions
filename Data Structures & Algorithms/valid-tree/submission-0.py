class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        visited = set()
        adj_lists = defaultdict(list) # node: neighbours
        for edge in edges:
            adj_lists[edge[0]].append(edge[1])
            adj_lists[edge[1]].append(edge[0])

        def dfs(node, parent): 
            if node in visited: 
                return False
            visited.add(node)
            adj_list = adj_lists[node]
            curr = True
            for children in adj_list: 
                if children != parent: 
                    curr = curr and dfs(children, node)
            return curr 
        
        result = dfs(0, -1)
        if len(visited) != n:
            return False
        return result

    