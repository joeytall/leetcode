class TwoSum(object):
  def __init__(self, nums, target):
    self.target = target
    self.nums = nums
    self.originalNums = list(nums)
    self.scannedNums = []
    self.result = []
    self.findMatch();

  def solve(self):
    print self.result

  def findMatch(self):
    while len(self.nums) > 0:
      num = self.nums.pop(0)
      match = target - num
      if match in self.nums:
        self.result = [self.findIndex(num), self.findIndex(match)]
      else:
        self.scannedNums.append(num)

  def findIndex(self, num):
    return self.originalNums.index(num)


nums = [7,11,15,2]
target = 9
TwoSum(nums, target).solve()
