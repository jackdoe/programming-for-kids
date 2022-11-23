package main

import "fmt"

// return a list of N numbers
// with values from 2 to n*2
// e.g
//   explode(10)
// returns:
//   [2,4,6,8,10,12,14,16,18,20]
func explode(n int) []int {
	r := []int{}
	for i := 1; i <= n; i++ {
		r = append(r, i*2)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", explode(11))
}
