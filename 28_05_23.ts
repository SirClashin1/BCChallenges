function chooseFuse(ratings: string[], input: string): string {
    const inputNum = parseFloat(input.replace('V', ''));
    let num = -1;
    let bestRating = '';
  
    for (const fuseRating of ratings) {
      const currentNum = parseFloat(fuseRating.replace('V', ''));
      if (currentNum >= inputNum && (num === -1 || currentNum < num)) {
        num = currentNum;
        bestRating = fuseRating;
      }
    }
  
    return bestRating;
  }
  

  