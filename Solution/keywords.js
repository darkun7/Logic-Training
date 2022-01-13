function getKeyWord(sentence) {
    let sentenceGroup = sentence.split(" ");
    let combinations = [];
    let value;
    for (let h=0; h<sentenceGroup.length; h++) {
        let slice = sentenceGroup.slice(h)
        value = slice.join(' ')
        if (!combinations.includes(value) && value.length > 1) {
            combinations.push(slice.join(' '))
        }
        for (let t=slice.length; t>0; t--) {
            value = sentenceGroup.slice(h,t).join(' ')
            if (!combinations.includes(value) && value.length > 1) {
                combinations.push(value)
            }
        }
    }
    sentenceGroup.forEach(function(w){
        if (!combinations.includes(w) && w.length > 1) {
            combinations.push(w)
        }
    })
    return combinations;
  }
  
//   console.log(getKeyWord("clean white paper"))