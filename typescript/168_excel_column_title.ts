function convertToTitle(columnNumber: number): string {
  let res: string = '';
  while (columnNumber >= 1) {
    columnNumber--;
    let reminder = columnNumber % 26;
    let asciChar = String.fromCharCode(65 + reminder);
    res = asciChar + res;
    columnNumber = Math.floor(columnNumber / 26);
  }

  return res;
}

console.log(convertToTitle(1));
console.log(convertToTitle(28));
console.log(convertToTitle(701));
