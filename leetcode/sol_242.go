package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
	fmt.Println(isAnagram("aa", "bb"))
}

func isAnagram(s string, t string) bool {
	lens := len(s)
	if lens != len(t) {
		return false
	} else if lens <= 0 {
		return false
	} else {
		//m := make(map[string]int, lens)
		arr1 := make([]rune, lens)
		arr2 := make([]rune, lens)
		for idx, val := range s {
			arr1[idx] = val
		}
		for idx, val := range t {
			arr2[idx] = val
		}
		sort.Slice(arr1, func(p, q int) bool {
			return arr1[p] < arr1[q]
		})
		sort.Slice(arr2, func(p, q int) bool {
			return arr2[p] < arr2[q]
		})

		for i := 0; i <= lens-1; i++ {
			if arr1[i] != arr2[i] {
				return false
			}
		}
		return true
	}
}
