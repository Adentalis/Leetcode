function isPalindrome(s: string): boolean {
  s = s.toLowerCase();
  s = Array.from(s)
    .filter(
      (e) =>
        (e.charCodeAt(0) >= 48 && e.charCodeAt(0) <= 57) ||
        (e.charCodeAt(0) >= 96 && e.charCodeAt(0) <= 122)
    )
    .toString();

  while (s.length > 1) {
    if (s[0] === s[s.length - 1]) {
      s = s.substring(1, s.length - 1);
    } else {
      return false;
    }
  }

  return true;
}

console.log(isPalindrome('A man, a plan, a canal: Panama'));
console.log(isPalindrome('race a car'));
console.log(isPalindrome(' '));
console.log(isPalindrome('0P'));

// Test to use regex to get only alphanumeric string
let test = 'cr403=?ot.0.,';

let res = test.replace(/[^A-Za-z0-9]/g, '');
console.log(res);
