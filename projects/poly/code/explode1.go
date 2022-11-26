package main

import (
	"fmt"
)

// return a list of n numbers
// with decreasing values from 2 + n down
// e.g:
//   explode(10)
// returns:
//   [11,10,9,8,7,6,5,4,3,2,1]
func explode(n int) []int {
	r := []int{}
	for i := 0; i < n; i++ {
		v := 2 + n - i
		r = append(r, v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", explode(11))
}
