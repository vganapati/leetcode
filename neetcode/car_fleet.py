from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_inds = sorted(range(len(position)), key=position.__getitem__)[::-1]
        num_fleets = 0

        for count, sorted_ind in enumerate(sorted_inds):
            position_i = position[sorted_ind]
            speed_i = speed[sorted_ind]
            time_i = (target - position_i)/speed_i  # position_i + speed_i*time_i = target
            if count == 0:
                time = time_i
                num_fleets += 1
            elif time_i <= time:
                pass # car is part of previous fleet
            else:
                # new fleet starts
                time = time_i
                num_fleets += 1
        return num_fleets

    def carFleet_unionFind(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sorted_inds = sorted(range(len(position)), key=position.__getitem__)[::-1]
        num_parents = len(position)
        parents = list(range(num_parents))
        rank = [1]*num_parents
        times = [0]*num_parents

        def find(ind):
            while parents[ind] != ind:
                parents[ind] = parents[parents[ind]] # path compression
                ind = parents[ind]
            return ind

        def join(ind_0, ind_1):
            par_0, par_1 = find(ind_0), find(ind_1)
            if par_0 == par_1:
                return 0
            else:
                if rank[par_0] > rank[par_1]:
                    parents[par_1] = par_0
                    rank[par_0] += rank[par_1]
                else:
                    parents[par_0] = par_1
                    rank[par_1] += rank[par_0]
                return 1


        for count, sorted_ind in enumerate(sorted_inds[:-1]):
            if count == 0:
                position_1 = position[sorted_ind]
                speed_1 = speed[sorted_ind]
                time_1 = (target - position_1)/speed_1
            else:
                time_1 = times[count]

            # does car bump into next car?
            position_0 = position[sorted_inds[count+1]]
            speed_0 = speed[sorted_inds[count+1]]
            # when does car 0 reach finish line?
            time_0 = (target - position_0)/speed_0 # position_0 + speed_0*time = target 
            

            if time_0 <= time_1:
                # join the disjoint sets
                num_parents -= join(count, count+1)
                times[count+1] = time_1
            else:
                times[count+1] = time_0
        return num_parents


solution = Solution()

target=10; position=[0,4,2]; speed=[2,1,3]
assert solution.carFleet(target, position, speed) == 1


target = 10; position = [1,4]; speed = [3,2]
assert solution.carFleet(target, position, speed) == 1

target = 10; position = [4,1,0,7]; speed = [2,2,1,1]
assert solution.carFleet(target, position, speed) == 3

