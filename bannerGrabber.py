#!/usr/bin/env python3
import socket


def banner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    msg = s.recv(1024).decode()
    print(msg)


def main():
    ip = input("Please specify the IP: ")
    port = input("Please specify the port: ")
    banner(ip, port)


main()
