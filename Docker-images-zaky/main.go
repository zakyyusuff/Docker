package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.Handlefunc("/", func(w http.ResponseWrite, r *http.Request){
		fmt.Fprintf(w, "Hallo ini zaky main_go")
	})

	http.ListenAndServe(":8000," nil)
}