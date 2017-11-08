# Netscan

Netscan is a fast TCP port scanner for IPv4 and IPv6 networks. Netscan is written in Go and is intended for normal users to run on Linux, Windows or Mac systems. The goal of netscan is to find open server ports quickly for service tracking and later testing and deep analysis using tools such as Nmap and Nessus. Netscan results are intended to be loaded into a relational database.

## Time to scan 1 million hosts for 45 common ports (using 32K semaphore)

```bash
$ time ./netscan 172.txt ports.txt > 172.results.txt

real    44m3.894s
user    24m15.180s
sys     48m20.012s

```

## To get or build netscan

```bash
$ go get github.com/w8rbt/netscan
$ go build netscan.go
```

## To run netscan

```bash
$ netscan ips.txt ports.txt > results.txt
```

## Notes

* To scan large networks for many dozens of ports, consider increasing the number of open files for the user who runs netscan and also increasing the size of the counting semaphore in the netscan code. Experiment to find a suitable number on your scanner systems for your particular networks. Here's an example on Linux systems in the file __/etc/security/limits.conf__:

```bash
user_name      soft    nofile      150000
user_name      hard    nofile      150000
```

* The file __ips.txt__ must be a plain text file with one IP address or hostname per line. It must contain one or more entries. Netscan does not support CIDR notation. See the __gen_ips.py__ script (in this repository) as an example of how to generate a list of IPs based on a CIDR prefix. Here's an example __ips.txt__ file:

```bash
192.168.1.54
2001:468:c80:c111:0:401a:d2f8:de6c
hostname.your.domain
```
* The file __ports.txt__ must be a plain text file with one TCP port number per line. It must contain at least one port number. Typically, __ports.txt__ would look something like this:

```bash
21
22
23
80
443
445
3389
```

## How to scan IPv6 networks efficiently

Add AAAA DNS records for all of your IPv6 servers and allow your netscan scan engines to do zone transfers. This basically limits the scan to what you have in the DNS. 

