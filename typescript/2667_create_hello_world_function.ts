function createHelloWorld() {
  return function (...args: any): string {
    return 'Hello World';
  };
}

const f = createHelloWorld();
console.log(f());

// Some play arounds

// This function takes all parameters and stores them within one array
const restArgumentFunction = (...args: any) => {
  return args.length;
};

console.log(restArgumentFunction('3', 33));
console.log(restArgumentFunction('3', 33, {}));
