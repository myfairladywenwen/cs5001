class Point:
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y

    def getX(self):
        return self.xCoord

    def getY(self):
        return self.yCoord

    def midPoint(self, otherPoint):
        # The following 0 assignments are placeholders
        # to make the coe run. They need to be made to 
        # calculate the coordinates of the new midpoint.
        if self.getX() < otherPoint.getX():
            newX = (otherPoint.getX() - self.getX())/2 + self.getX()
        else:
            newX = (self.getX() - otherPoint.getX())/2 + otherPoint.getX()
        if self.getY() < otherPoint.getY():
            newY = (otherPoint.getY() - self.getY())/2 + self.getY()
        else:
            newY = (self.getY() - otherPoint.getY())/2 + otherPoint.getY()
        return Point(newX, newY)
