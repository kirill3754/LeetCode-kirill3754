def find_zero(config):
    for i in range(2):
        for j in range(3):
            if not config[i][j]:
                return i, j
    return None



class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        seen = set()
        board_tuple = tuple(tuple(row) for row in board)
        seen.add(board_tuple)

        solution = [[1,2,3],[4,5,0]]
        moves = 0
        configs = [board]
        while configs:
            new_configs = []
            for config in configs:
                if config == solution:
                    return moves

                i, j = find_zero(config)


                test = copy.deepcopy(config)

                test[0][j], test[1][j] = test[1][j], test[0][j]

                test_tuple = tuple(tuple(row) for row in test)
                if test_tuple not in seen:
                    seen.add(test_tuple)
                    new_configs.append(list(test))
                
                if j != 0:
                    test = copy.deepcopy(config)
                    test[i][j], test[i][j-1] = test[i][j-1], test[i][j]
                    test_tuple = tuple(tuple(row) for row in test)
                    if test_tuple not in seen:
                        seen.add(test_tuple)
                        new_configs.append(list(test))
                
                if j != 2:
                    test = copy.deepcopy(config)
                    test[i][j], test[i][j+1] = test[i][j+1], test[i][j]
                    test_tuple = tuple(tuple(row) for row in test)
                    if test_tuple not in seen:
                        seen.add(test_tuple)
                        new_configs.append(list(test))

            configs = new_configs
            moves += 1


        return -1
        