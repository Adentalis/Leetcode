function addDigits(num: number): number {
  if (num > 9) {
    let s = Array.from(num.toString());
    let res = 0;
    s.forEach((e) => {
      res += parseInt(e);
    });

    if (res > 9) {
      return addDigits(res);
    } else {
      return res;
    }
  } else {
    return num;
  }
}

console.log(addDigits(331));
