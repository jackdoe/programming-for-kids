package main

import "fmt"

// return a list of N numbers
// with values from 1 to n
// e.g
//   explode(10)
// returns:
//   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func explode(n int) []int {
	r := []int{}
	for i := 1; i <= n; i++ {
		r = append(r, i)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", explode(11))
}
