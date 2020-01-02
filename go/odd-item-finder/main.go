package main

import (
	"fmt"
	"log"
)

type Obj struct {
	weight int
	mem    int
	cpu    int
}

func main() {
	fmt.Println("Hello, World!")
}

func heavier(left []Obj, right []Obj, m func([]Obj) int) int {

	if m(left) == m(right) {
		return 0
	}
	if m(left) > m(right) {
		return 1
	}
	return 2
}

func Cpu(o []Obj) int {
	cpu := 0
	for _, i := range o {
		cpu = cpu + i.cpu
	}
	return cpu
}

func weight(o []Obj) int {
	w := 0
	for _, i := range o {
		w = w + i.weight
	}
	return w
}

func mem(o []Obj) int {
	m := 0
	for _, i := range o {
		m = m + i.mem
	}
	return m
}

func findOddItem(o []Obj, fn func([]Obj) int) int {
	r := heavier(o[:3], o[3:6], fn)
	if r == 1 {
		r2 := heavier(o[0:1], o[1:2], fn)
		log.Printf("Second round (%T): %d", fn, r2)
		if r2 == 0 {
			return 1
		}
		if r2 == 1 {
			return 2
		}
		if r2 == 2 {
			return 3
		}
	}
	if r == 2 {
		r2 := heavier(o[4:5], o[5:6], fn)
		if r2 == 0 {
			return 4
		}
		if r2 == 1 {
			return 5
		}
		if r2 == 2 {
			return 6
		}
	}
	return 7 //len(o)
}
