package main

import "fmt"

// take a list of numbers
// and return an average
// floored, e.g:
//   [1,2]
// returns:
//   1
func avg(x []int) int {
	sum := 0
	for _, v := range x {
		sum += v
	}

	return sum / len(x)
}

func main() {
	fmt.Printf("%v\n", avg([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
