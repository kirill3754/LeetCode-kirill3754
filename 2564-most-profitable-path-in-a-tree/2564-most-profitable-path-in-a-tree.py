class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Create a dict of all paths
        directions = defaultdict(list)
        for edge1, edge2 in edges:
            directions[edge1].append(edge2)
            directions[edge2].append(edge1)
        # Locate bob's path
        
        bob_prev = defaultdict(list)
        stack_bob = [(bob, -1)]
        while stack_bob:
            path_found = False
            new_stack_bob = []
            for loc, prev in stack_bob:
                if loc == 0:
                    path_found = True
                    break
                for direction in directions[loc]:
                    if direction != prev:
                        bob_prev[direction] = loc
                        new_stack_bob.append((direction, loc))
            if path_found:
                break
            stack_bob = new_stack_bob
        
        cur = 0
        bob_path = []
        while cur != -1:
            bob_path.append(cur)
            cur = bob_prev.get(cur, -1)
            
        bob_path = bob_path[::-1]
        #print(bob_path)
        
        # locate A path by updating weights on each bob's step
        max_income = -inf
        stack_alice = [(0, -1, 0)]
        step = 0
        visited = set()
        while stack_alice:
            #print(step)
            #print(stack_alice)
            if step < len(bob_path):
                amount[bob_path[step]] //= 2
            new_stack_alice = []
            for loc, prev, balance in stack_alice:
                if loc in visited:
                    continue
                visited.add(loc)
                balance += amount[loc]
                if step and len(directions[loc]) == 1:
                    max_income = max(max_income, balance)
                else:
                    for direction in directions[loc]:
                        if direction != prev and direction not in visited:
                            new_stack_alice.append((direction, loc, balance))
            stack_alice = new_stack_alice
            if step < len(bob_path):
                amount[bob_path[step]] = 0
            step += 1
        return max_income




        