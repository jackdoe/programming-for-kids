package main

import "fmt"

// rotate the input list to the left
//   [1,2,3,4]
// returns:
//   [2,3,4,1]
func rotate_left(x []int) []int {
	r := []int{}

	for i := 0; i < len(x); i++ {
		// go to the second element
		// then wrap around
		// example if x.len is 4:
		// (0 + 1) % 4 = 1
		// (1 + 1) % 4 = 2
		// (2 + 1) % 4 = 3
		// (3 + 1) % 4 = 0
		idx := (i + 1) % len(x)
		v := x[idx]
		r = append(r, v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", rotate_left([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 9}))
}
