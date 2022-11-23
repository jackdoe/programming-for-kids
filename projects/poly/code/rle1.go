package main

import "fmt"

// RunLength Encode a list of numbers
// in the format count, value:
// e.g.
//   [1,1,1,1,1,1,3,3]
// returns:
//   [6,1,2,3]
func rle(x []int) []int {
	r := []int{}
	for _, v := range x {
		if len(r) == 0 || r[len(r)-1] != v {
			r = append(r, 0) // count
			r = append(r, v) // value
		}

		// len - 2 is where we keep
		// the count
		r[len(r)-2] += 1
	}

	return r
}

func main() {
	fmt.Printf("%v\n", rle([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
