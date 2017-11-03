# Netscan

Netscan is a TCP port scanner for IPv4 and IPv6 networks. It is intended for normal users to run on Linux, Windows or Mac systems. The goal of netscan is to find open server ports quickly for service tracking and later testing and deep analysis (Nmap, Nessus, etc.). Netscan results are intended to be loaded into a relational database.

## Scanning a /16 for one port in about three seconds

```bash
$ wc -l ports.txt 
    1 ports.txt

$ wc -l ips.txt 
    65536 ips.txt

$ time netscan ips.txt ports.txt > /dev/null
    real    0m2.851s
    user    0m10.816s
    sys 0m3.428s
```

## To get or build

```bash
$ go get github.com/w8rbt/netscan
$ go build netscan.go
```

## To run (pick one) 

```bash
$ go run netscan.go ips.txt ports.txt
$ netscan ips.txt ports.txt > results.txt
$ netscan ips.txt ports.txt | grep Success
$ netscan ips.txt ports.txt | grep Success | awk -F , '{print $3}' > ips.txt
```

## Notes

* To scan large networks for multiple ports, you'll need to increase the number of open files for the user who runs netscan. 150,000 works well when scanning 40 ports on /16 IPv4 networks. Experiment to find a suitable number of open files on your scanner system for your networks. Here's an example from __/etc/security/limits.conf__ that works well for /16 (or smaller) networks:

```bash
user_name      soft    nofile      150000
user_name      hard    nofile      150000
```

* The file __ips.txt__ must be a plain text file with one IP address or hostname per line. It must contain one or more entries. Netscan does not support CIDR notation. See the __gen_ips.py__ script (in this repository) as an example of how to generate a list of IPs based on a CIDR prefix. Here's an example:

```bash
192.168.1.54
192.168.1.98
192.168.1.134
2001:468:c80:c111:0:401a:d2f8:de6b
2001:468:c80:c111:0:401a:d2f8:de6c
hostname.your.domain
```
* The file __ports.txt__ must be a plain text file with one TCP port number per line. It must contain at least one port number. Typically, it should look something like this:

```bash
21
22
23
80
443
445
3389
```
