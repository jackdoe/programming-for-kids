package main

import (
	"fmt"
	"math/rand"
)

func explode(n int) []int {
	r := []int{}
	for i := 0; i < n; i++ {
		r = append(r, rand.Int()%20)
	}
	return r
}

func main() {
	fmt.Printf("%v", explode(33))
}
