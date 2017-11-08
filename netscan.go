/*
 * Copyright (c) 2016 Richard B Tilley <brad@w8rbt.org>
 *
 * Permission to use, copy, modify, and distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 *
 */

package main

import "bufio"
import "fmt"
import "log"
import "net"
import "os"
import "sync"
import "time"

// Get current date
var date = time.Now()
var date_string = date.Format("2006-01-02")

// Is the scanner remote to the network or on the
// internal network?
var remote = false

// create a global empty slice of strings
// and a bool for debugging
var ips []string
var ports []string
var debug bool = false

// A WaitGroup waits for a collection of goroutines to finish. The main loop calls Add(1)
// to set the number of goroutines to wait for. Then each of the goroutines runs and calls Done
// when finished.
var wg sync.WaitGroup

// A channel that acts as a counting semaphore. Only allow X concurrent connections.
// The number here can be adjusted up or down. If too many open files/sockets then
// adjust this down. Lower numbers mean slower scan times.
// `ls /proc/pidof netscan/fd | wc -l` should be just under this
var sem = make(chan struct{}, 32768)

// create global constants
const usage string = "usage: ./netscan ips.txt ports.txt > results.txt"
const connection_timeout = 2 * time.Second

// connect
// Take an IP string and a ptr to the ports slice
func connect(ip string, the_ports *[]string) {
	for _, port := range *the_ports {
		if debug {
			fmt.Fprintln(os.Stderr, port)
		}

		hostPort := net.JoinHostPort(ip, port)

		conn, err := net.DialTimeout("tcp", hostPort, connection_timeout)
		if err != nil {
			if debug {
				fmt.Printf("1,%s\n", err.Error())
			}
		} else {
			fmt.Printf("%s,%s,%s 00:00:00,%t\n", ip, port, date_string, remote)
			conn.Close()
		}
	}

	// Decrements wg counter by 1
	defer wg.Done()

	// Receive Signal
	<-sem
}

// Load ips or ports from a text file into a slice
// Return pointer to the slice
func load(fileName string, the_slice []string) *[]string {

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if debug {
			fmt.Fprintln(os.Stderr, scanner.Text())
		}
		the_slice = append(the_slice, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return &the_slice
}

func main() {
	if len(os.Args) != 3 {
		fmt.Println(usage)
		time.Sleep(2 * time.Second)
		os.Exit(1)
	}

	ipFileName := os.Args[1]
	portFileName := os.Args[2]

	pips := load(ipFileName, ips)
	pports := load(portFileName, ports)

	if debug {
		fmt.Fprintf(os.Stderr, "ips size: %d\n", len(ips))
		fmt.Fprintf(os.Stderr, "ports size: %d\n", len(ports))
	}

	for _, ip := range *pips {
		if debug {
			fmt.Fprintln(os.Stderr, ip)
		}

		// Add 1 to wg counter
		wg.Add(1)

		// Send Signal into channel
		sem <- struct{}{}

		// Start go routine
		go connect(ip, pports)
	}

	// blocks until the WaitGroup counter is zero.
	wg.Wait()
	close(sem)
}
