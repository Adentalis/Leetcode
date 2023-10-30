type ToBeOrNotToBe = {
  toBe: (val: any) => boolean;
  notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
  return {
    toBe: (val2) => {
      if (val === val2) {
        return true;
      } else {
        throw 'Not Equal';
      }
    },
    notToBe: (val2) => {
      if (val !== val2) {
        return true;
      } else {
        throw 'Equal';
      }
    },
  };
}

expect(5).notToBe(null); // true
