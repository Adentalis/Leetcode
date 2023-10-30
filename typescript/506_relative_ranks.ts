function findRelativeRanks(score: number[]): string[] {
  const sorted = [...score].sort((a, b) => b - a);
  let res: string[] = [];

  score.forEach((e) => {
    let place = (sorted.indexOf(e) + 1).toString();

    if (place === '1') {
      res.push('Gold Medal');
    } else if (place === '2') {
      res.push('Silver Medal');
    } else if (place === '3') {
      res.push('Bronze Medal');
    } else {
      res.push(place);
    }
  });

  return res;
}

console.log(findRelativeRanks([10, 3, 8, 9, 4]));

/**
 * I like this solution
 * 
function findRelativeRanks(score: number[]): string[] {
    const sort:number[] = [...score].sort((a, b) => b-a);

    const medals = ["Gold Medal","Silver Medal","Bronze Medal"]

    return score.map((s) => {
        let index = sort.indexOf(s);

        return index < 3 ? medals[index] : String(index + 1)
    })
};
 * 
 */
