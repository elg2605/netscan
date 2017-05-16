# netscan

netscan is a TCP port scanner intended for normal users to run on Linux systems. The goal of netscan is to find open ports quickly for later testing and deep analysis (Nmap, Nessus, etc.).

## Scanning a /16 for one port

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

## To Build

```bash
$ go build netscan.go
```

## To Run (pick one) 

```bash
$ go run netscan.go ips.txt ports.txt
$ netscan ips.txt ports.txt > results.txt
$ netscan ips.txt ports.txt | grep Success
$ netscan ips.txt ports.txt | grep Success | awk -F , '{print $3}' > ips.txt
```

## Notes

To scan large networks, you'll need to increase the number of open files for the user who runs netscan. 150,000 works well for 10.0.0.0/16 networks (2^16 hosts). Experiment to find a suitable number of open files on your scanner system for your networks. Here's an example from __/etc/security/limits.conf__:

```bash
user_name      soft    nofile      150000
user_name      hard    nofile      150000
```

The file __ips.txt__ should be a plain text file with one IP address per line. __It must contain one or more IP addresses.__ and should look something like this:

```bash
192.168.1.54
192.168.1.98
192.168.1.134
```

The file __ports.txt__ should be a plain text file with one TCP port number per line. __It must contain one or more port numbers__ and should look something like this:

```bash
21
22
23
80
443
445
3389
```

netscan does not support CIDR notation.

