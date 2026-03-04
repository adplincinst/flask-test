package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"
)

// 1. Setup Configuration
const (
	Host = "0.0.0.0"
	Port = "5009"
)

// 2. Execution Wrapper (Pygeoapi-style)
// In Go, we pass a function that returns a map and a status code
func executeRequest(w http.ResponseWriter, r *http.Request, apiFunc func() (map[string]interface{}, int)) {
	log.Printf("[%s] Incoming: %s %s", time.Now().Format(time.RFC3339), r.Method, r.URL.Path)

	// Call the core logic
	content, status := apiFunc()

	// Set headers and return JSON
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	json.NewEncoder(w).Encode(content)

	log.Printf("[%s] Completed: %d", time.Now().Format(time.RFC3339), status)
}

// 3. Core Logic
func getStatusData() (map[string]interface{}, int) {
	// 4. Non-blocking Sleep
	// In Go, time.Sleep pauses the current Goroutine, 
	// but the scheduler simply moves to the next one.
	time.Sleep(10 * time.Second)

	return map[string]interface{}{
		"status":    "online",
		"server":    "Go (Standard Library)",
		"mechanism": "Goroutines",
		"slept":     "10s",
	}, http.StatusOK
}

func main() {
	// 5. Route Definition (Blueprint equivalent)
	mux := http.NewServeMux()

	mux.HandleFunc("/status", func(w http.ResponseWriter, r *http.Request) {
		executeRequest(w, r, getStatusData)
	})

	address := fmt.Sprintf("%s:%s", Host, Port)
	fmt.Printf("Go server listening on http://%s\n", address)

	// Start the server
	if err := http.ListenAndServe(address, mux); err != nil {
		log.Fatal(err)
	}
}

