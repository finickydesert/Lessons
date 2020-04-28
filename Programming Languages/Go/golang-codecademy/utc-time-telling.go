package main

import(
 "fmt"
 "time"
)

func main(){
	fmt.Println(time.Now())
}
/*notes: 
why this tool?
the answer: cuz i can
also i double checked the actual functions within the time package and according to https://golang.org/pkg/time/
it seems like the language has both chronological "they indicate "wall" clock and something called monotonic clocks.
intresting read on time and measurement if you are intrested.
also you can find more on commenting in GO here: https://github.com/golang/go/wiki/Comments
*/