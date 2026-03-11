import statistics


class ComputeStatistics:
    def __init__(self, file):
        """Constructor to take file path."""
        self.file = file

    def read_int(self):
        """Reads integers from file and returns them as a list."""
        data = []
        try:
            with open(self.file, "r") as f:
                for line in f:
                    num = int(line.strip())
                    data.append(num)
        except Exception as e:
            print("Error:", e)
        return data

    def count(self):
        """Returns count of integers."""
        data = self.read_int()
        return len(data)

    def summation(self):
        """Returns sum of integers."""
        data = self.read_int()
        return sum(data)

    def average(self):
        """Returns average of integers."""
        data = self.read_int()
        return statistics.mean(data)

    def minimum(self):
        """Returns minimum value."""
        data = self.read_int()
        return min(data)

    def maximum(self):
        """Returns maximum value."""
        data = self.read_int()
        return max(data)


if __name__ == "__main__":
    file = "random_nums.txt"
    cs = ComputeStatistics(file)

    print("The values are:", cs.read_int())
    print("Total values in file are:", cs.count())
    print("Summation of data is:", cs.summation())
    print("Average of data is:", cs.average())
    print("Minimum value from data is:", cs.minimum())
    print("Maximum value from data is:", cs.maximum())
