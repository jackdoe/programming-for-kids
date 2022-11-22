package main

import (
	"fmt"
)

// return a list of N numbers
// with values from 1 to n/2
// e.g
//   explode(10)
// returns:
//   [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
func explode(n int) []int {
	r := []int{}
	for i := 1; i <= n; i++ {
		r = append(r, (i+1)/2)
	}
	return r
}

func main() {
	fmt.Printf("%v", explode(33))
}
