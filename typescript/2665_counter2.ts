type ReturnObj = {
  increment: () => number;
  decrement: () => number;
  reset: () => number;
};

function createCounter2(init: number): ReturnObj {
  let counter = init;
  return {
    increment: () => ++counter,
    decrement: () => --counter,
    reset: () => {
      counter = init;
      return counter;
    },
  };
}

const counter = createCounter2(5);
console.log(counter.increment());
console.log(counter.reset());
console.log(counter.decrement());
