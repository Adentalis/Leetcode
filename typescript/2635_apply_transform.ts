function map(arr: number[], fn: (n: number, i: number) => number): number[] {
  arr.forEach((e, i) => {
    arr[i] = fn(e, i);
  });
  return arr;
}

console.log(map([1, 2, 3], (n: number) => n + 1));
