function findKthLargest(nums: number[], k: number): number {
  let sorted = nums.sort((a, b) => b - a);

  return sorted[k - 1];
}

console.log(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4));
