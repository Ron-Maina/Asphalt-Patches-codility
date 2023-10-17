function Solution(S){
    let patches = 0
    let i = 0
    while (i < S.length){
        if (S[i] === "X"){
            patches += 1
            i += 3
        } else {
            i +=1
        }
    }
    console.log(patches)
}
Solution(".X..X")
Solution("X.XXXXX.X.")
Solution("XX.XXX..")
Solution("XXXX")
Solution('.X...XX')