function createCounter(n: number): () => number {
    var i : number;
    i = n - 1;
    return function() {
        i = i + 1;
        return i;
    }
}
