
# Author : @jimmg35
# using python typing module for static check
# python 3.7.3

from typing import List

class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


def calTriArea(A: Point , B: Point , C: Point) -> float:
    # Calculate Triangle Area
    return abs((A.x*B.y - A.y*B.x) + (B.x*C.y - B.y*C.x) + (C.x*A.y - C.y*A.x))/2
    
    

if __name__ == '__main__':
    # data input
    P_1: Point = Point(1, 4)
    P_2: Point = Point(2, -1)
    P_3: Point = Point(-4, -4)
    P_4: Point = Point(-3, 4)
    origin: Point = Point(0, 0)    
    pointSeries: List[Point] = [P_1, P_2, P_3, P_4]

    # Calculate Polygon area
    area_Big_Polygon: float = calTriArea(P_1, P_2, P_3) + calTriArea(P_3, P_4, P_1)
    
    # Calculate the area of each triangle with origin
    accum_area: float = 0
    for i in range(0, len(pointSeries)-1):
        accum_area += calTriArea(pointSeries[i], pointSeries[i+1], origin)
        if i == (len(pointSeries)-2):
            accum_area += calTriArea(pointSeries[0], pointSeries[3], origin)

    # check the area to determine whether origin is inside the box
    if accum_area == area_Big_Polygon:
        print(1)
    else:
        print(0)
            

    

    



    
    