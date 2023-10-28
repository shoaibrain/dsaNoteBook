from collections import deque

"""
Given an array of integers of size n.
Our aim is to calculate the maximum sum possible for k consecutive elements in the array.
"""


def slideAndPrintFixedSizeWindow(sequence, winSize):
    left = 0
    runningWindow = deque()
    for right in range(len(sequence)):
        runningWindow.append(sequence[right])
        if len(runningWindow) == winSize:
            print(f"Running widow: {runningWindow}")
            runningWindow.popleft()
        else:
            continue


if __name__ == "__main__":
    seq = [1, 2, 3, 5, 3, 3, 5, 6, 6, 342, 5, 34, 5]
    winSize = 3
    slideAndPrintFixedSizeWindow(seq, winSize)
