function majorityElement(nums: number[]): number[] {
  let m = new Map();
  nums.forEach((e) => {
    if (m.get(e)) {
      m.set(e, m.get(e) + 1);
    } else {
      m.set(e, 1);
    }
  });

  const keys = Array.from(m.keys());
  let res: number[] = [];
  keys.forEach((e) => {
    if (m.get(e) > Math.floor(nums.length / 3)) {
      res.push(e);
    }
  });

  return res;
}

console.log(majorityElement([3, 2, 3]));
