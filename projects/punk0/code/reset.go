package main

import (
	"fmt"
)

// create a new list
// with the value 0,0,0,1
// returns:
//   [0,0,0,1]
func reset() []int {
	r := []int{}
	for i := 1; i <= 4; i++ {
		v := 0
		if i == 3 {
			v = 1
		}
		r = append(r, v)
	}
	return r
}

func main() {
	fmt.Printf("%v\n", reset())
}
