package main

import "fmt"

func explode(nf float32) []int32 {
	n := int32(nf)
	r := []int32{}
	for i := int32(1); i <= n; i++ {
		r = append(r, i)
		r = append(r, i)
	}
	return r
}

func main() {
	fmt.Printf("%v", explode(33))
}
