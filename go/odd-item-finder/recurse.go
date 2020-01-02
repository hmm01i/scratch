package main

import "fmt"

func heavierV2(left []Obj, right []Obj, m func([]Obj) int) ([]Obj, error) {

	if m(left) == m(right) {
		return []Obj{}, fmt.Errorf("Groups are equal")
	}
	if m(left) > m(right) {
		return left, nil
	}
	return right, nil
}

func findOddItemRec(o []Obj, fn func([]Obj) int) int {
	// assume we have 7
	half := (len(o) - 1) / 2
	group1 := o[len(o)-1:]
	group2 := o[:half]
	group3 := o[half : len(o)-1]
	if r, err := heavierV2(group2, group3, fn); err != nil {
		findOddItemRec(r, fn)
	}
	return len(group1)

}
