function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  console.log(nums1);
  if (m === 0) {
    nums1 = nums2;
  } else if (n === 0) {
  } else {
    let res: number[] = [];
    let finished = false;
    let i: number = 0;
    let j: number = 0;

    while (!finished) {
      if (j === n) {
      }

      if (nums1[i] < nums2[j]) {
        res.push(nums1[i]);
        i++;
      } else {
        res.push(nums2[j]);
        j++;
      }
      //   nums1[i] < nums2[j]
    }
  }

  console.log(nums1);
}
function merge2(nums1: number[], m: number, nums2: number[], n: number): void {
  console.log(nums1);
  let res: number[] = [];

  console.log(nums1);
}

merge2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3);

/**
 * Test the following ways
 * 1) create a dummy array, create the result in it, assign it to nums1
 *
 */
