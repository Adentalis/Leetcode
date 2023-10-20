const createCounter = (n: number): (() => number) => {
  return (): number => {
    return n++;
  };
};

let inc = createCounter(10);
console.log(inc());
console.log(inc());
console.log(inc());
