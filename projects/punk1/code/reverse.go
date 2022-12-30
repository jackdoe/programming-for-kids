package main

import "fmt"

// reverse the input list
//   [1,2,3,4,5]
// returns:
//   [5,4,3,2,1]
func reverse(x []int) []int {
	r := []int{}
	for i := 0; i < len(x); i++ {
		v := x[len(x)-1-i]
		r = append(r, v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", reverse([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
