type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    if (nums.length == 0) {
        return init;
    }
    nums = [init].concat(nums);
    return nums.reduce(fn);
};
