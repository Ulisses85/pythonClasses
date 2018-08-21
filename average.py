
class AverageCalculator(object):

    def __init__(self):
        filename = input("Enter a file name: ")
        with open(filename) as f:
            self.data = [int(line) for line in f]

    def minimal(self):
        print("The minimum value is ", min(self.data))

    def maximal(self):
        print("The maximum value is ", max(self.data))

    def mean(self):
        print("The average value is ", sum(self.data) / len(self.data))

    def median(self):
        print("The median value is ", self.data[len(self.data)//2])

    def mode(self):
        print("The mode value is", max(self.data, key=lambda n: self.data.count(n)))


if __name__ == '__main__':
    s = AverageCalculator()
    s.minimal()
    s.maximal()
    s.median()
    s.mode()

