import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(12345)

class TSP:
    def __init__(self, points, initialNode):
        self.points = points
        self.initialNode = initialNode
        self.N = points.shape[0]
        self.distanceMatrix = []
        self.alpha = 0.9
        self.time = (1, 500)
        self.t = self.time[1]
        self.time2 = 5000
        self.path = np.arange(self.N)
        self.distance = 0
        self.K = 0.8
        self.result = []
        self.tempPath = self.path.copy()
        self.bestPath = self.path.copy()
        self.bestdis = 10000

    def createBoard(self):

        pass

    def drawRoute(self, journey, totalDistance):
        plt.cla()
        plt.title('Best Path=%.4f' % totalDistance)
        xplot = [self.points[i][0] for i in range(self.N)]
        yplot = [self.points[i][1] for i in range(self.N)]
        plt.scatter(xplot, yplot, color='b')
        xplot = np.array(xplot)
        yplot = np.array(yplot)

        for i in range(self.N-1):
            plt.plot(xplot[[journey[i], journey[i+1]]], yplot[[journey[i], journey[i+1]]], color='y')
        
        plt.plot(xplot[[journey[self.N - 1], 0]], yplot[[journey[self.N - 1], 0]], color='y')
        plt.scatter(xplot[0], yplot[0], color='k', linewidth=10)

    def getDistanceMatrix(self, points):
        self.distanceMatrix = np.zeros((self.N, self.N))
        for i in range(self.N):
            for j in range(i, self.N):
                self.distanceMatrix[i][j] = self.distanceMatrix[j][i] = np.linalg.norm(
                    points[i]-points[j])
        return self.distanceMatrix

    def calcDistance(self, path):
        self.distance = 0
        for i in range(self.N - 1):
            self.distance += self.distanceMatrix[path[i]][path[i+1]]
        self.distance += self.distanceMatrix[path[self.N-1]][path[0]]
        return self.distance

    def calcTSP(self):
        while self.t > self.time[0]:
            for i in range(self.time2):
                random_number = np.random.rand()
                if random_number > 0.5:
                    flag = True
                    while flag:
                        nodeOne = np.int(np.ceil(np.random.rand()*(self.N-1)))
                        nodeTwo = np.int(np.ceil(np.random.rand()*(self.N-1)))
                        if (nodeOne != nodeTwo):
                            flag = False
                    self.tempPath[nodeOne], self.tempPath[nodeTwo] = self.tempPath[nodeTwo], self.tempPath[nodeOne]
                else:
                    flagTwo = True
                    while flagTwo:
                        nodeOne = np.int(np.ceil(np.random.rand()*(self.N-1)))
                        nodeTwo = np.int(np.ceil(np.random.rand()*(self.N-1)))
                        nodeThree = np.int(
                            np.ceil(np.random.rand()*(self.N-1)))
                        if ((nodeOne != nodeTwo) and (nodeOne != nodeThree) and (nodeTwo != nodeThree)):
                            flagTwo = False

                        if nodeOne > nodeTwo:
                            nodeOne,nodeTwo = nodeTwo,nodeOne
                        if nodeTwo > nodeThree:
                            nodeTwo,nodeThree = nodeThree,nodeTwo
                        if nodeOne > nodeTwo:
                            nodeOne,nodeTwo = nodeTwo,nodeOne

                        temp = self.tempPath[nodeOne:nodeTwo].copy()
                        self.tempPath[nodeOne:nodeThree - nodeTwo + 1 + nodeOne] = self.tempPath[nodeTwo:nodeThree + 1].copy()
                        self.tempPath[nodeThree - nodeTwo + 1 + nodeOne:nodeThree + 1] = temp.copy()
                temporalDistance = self.calcDistance(self.tempPath)

                if temporalDistance < self.distance:
                    self.path = self.tempPath.copy()
                    self.distance = temporalDistance
                if temporalDistance < self.bestdis:
                    self.bestPath = self.tempPath.copy()
                    self.bestdis = temporalDistance
                    self.drawRoute(self.bestPath,self.bestdis)
                else:
                    random_number = np.random.rand()
                    if random_number < np.exp(-(temporalDistance - self.distance)/self.t):
                        self.path = self.tempPath.copy()
                        self.distance = temporalDistance
                    else:
                        self.tempPath = self.path.copy()
            self.t *= self.alpha
            self.result.append(self.bestdis)
        plt.show()
    

    def printResults(self):
        print("Best Path:%s " % np.array(self.result[-1]))
        for i in self.bestPath:
            print(i, end="=>")
        print(self.bestPath[0])