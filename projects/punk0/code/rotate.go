package main

import "fmt"

// rotate the input list to the right
//   [1,2,3,4]
// returns:
//   [4,1,2,3]
func rotate(x []int) []int {
	r := []int{}
	for i := 0; i < len(x); i++ {
		// go to the last element and
		// then wrap around
		// example if len is 4:
		// (0 + 4 - 1) % 4 = 3
		// (1 + 4 - 1) % 4 = 0
		// (2 + 4 - 1) % 4 = 1
		// (3 + 4 - 1) % 4 = 2
		idx := (i + len(x) - 1) % len(x)
		v := x[idx]
		r = append(r, v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", rotate([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 9}))
}
