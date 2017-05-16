# netscan

netscan is a TCP port scanner intended for normal users to run on Linux systems. The goal of netscan is to find open ports (quickly) for later testing and deep analysis (Nmap, Nessus, etc.).

## To Build

```bash
$ go build netscan.go
```

## To Run (pick one) 

```bash
$ go run netscan.go ips.txt ports.txt
$ netscan ips.txt ports.txt > results.txt
$ netscan /tmp/128.173.0.0 ports.txt | grep Success
```

## Notes

To scan large networks, you'll need to increase the number of open files for the user who runs netscan. 150,000 works well for 10.0.0.0/16 networks (2^16 hosts). Experiment to find a suitable number of open files on your scanner system for your networks. Here's an example taken from my local __/etc/security/limits.conf__:

```bash
user_name      soft    nofile      150000
user_name      hard    nofile      150000
```

The file 'ips.txt' should be a plain text file with one IP address per line. It must contain one or more IP addresses and should look something like this:

```bash
192.168.1.54
192.168.1.98
192.168.1.134
...
```

The file 'ports.txt' should be a plain text file with one TCP port number per line. It must contain one or more port numbers and should look something like this:

```bash
21
22
23
80
443
445
3389
...
```

