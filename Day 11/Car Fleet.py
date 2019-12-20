class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ordered_pos = sorted(zip(position, speed), reverse=True)
        
        remaining_time_for_each_car = [(target - x) / y for x, y in ordered_pos]
        total_cars = len(position)
        fleet_count = 0
        i = 0
        while i < total_cars:
            # Only 1 car is remaining
            if i == (total_cars - 1):
                fleet_count += 1
                break
            next_pos_to_visit = i + 1
        
            while next_pos_to_visit <= (total_cars - 1) and remaining_time_for_each_car[next_pos_to_visit] <= \
                remaining_time_for_each_car[next_pos_to_visit - 1]:
                    next_pos_to_visit += 1
            
            while next_pos_to_visit <= (total_cars - 1) and remaining_time_for_each_car[next_pos_to_visit] <= \
            remaining_time_for_each_car[i]:
                next_pos_to_visit += 1
            i = next_pos_to_visit
            fleet_count += 1

        return fleet_count