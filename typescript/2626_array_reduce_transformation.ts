type Fn = (accum: number, curr: number) => number;

function reduce(nums: number[], fn: Fn, init: number): number {
  if (nums.length === 0) {
    return init;
  }

  let current = init;
  nums.forEach((e, i) => {
    current = fn(e, current);
  });
  return current;
}

console.log(reduce([1, 2, 3, 4], (acc, cur) => acc + cur, 0));
