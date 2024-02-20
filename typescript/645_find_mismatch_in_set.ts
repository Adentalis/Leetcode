function findErrorNums(nums: number[]): number[] {
  let missed = 0;

  let duplicate = nums.find((e, i) => {
    return nums.indexOf(e) !== i;
  });

  for (let i = 1; i <= nums.length; i++) {
    if (nums.indexOf(i) === -1) {
      missed = i;
      break;
    }
  }
  return [duplicate ?? 0, missed];
}

console.log(findErrorNums([1, 2, 2, 4]));
