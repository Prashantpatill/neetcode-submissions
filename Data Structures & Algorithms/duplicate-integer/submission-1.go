func hasDuplicate(nums []int) bool {
    arrmap := make (map[int]bool)
    for _, num :=range nums {
        if arrmap[num] {
            return true
        }
        arrmap[num] = true
    }
    return false
}
