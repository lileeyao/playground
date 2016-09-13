package main

/*
{"data": {"children": [
  {"data": {
	    "title": "The Go homepage",
		    "url": "http://golang.org/"
			  }},
				  ...
					]}}

*/
type Item struct {
	Title string
	URL   string
}

type Response struct {
	Data struct {
		Children []struct {
			Data Item
		}
	}
}
