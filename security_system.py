import os
import time
import threading
import queue
import hashlib
import logging
# For network monitoring, scapy is required. If not installed, comment out related lines.
try:
    from scapy.all import sniff, IP, TCP
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# --- Malware Signatures (expand as needed) ---
MALWARE_SIGNATURES = [
    b'\x90\x90\x90\x90',  # NOP sled
    b'\xEB\xFE',           # Infinite loop
]
# Example: Known malicious file hashes (expand as needed)
MALWARE_HASHES = set([
    # 'eicar test file hash',
])

logger = logging.getLogger("SecuritySystem")
logger.setLevel(logging.INFO)

class UnifiedSecuritySystem:
    def __init__(self, root_dir, scan_interval=300, network_interface=None):
        self.root_dir = root_dir
        self.scan_interval = scan_interval  # seconds
        self.network_interface = network_interface
        self.stop_event = threading.Event()
        self.alert_queue = queue.Queue()
        self.threads = []

    def start(self):
        logger.info("Starting Unified Security System...")
        t1 = threading.Thread(target=self.periodic_file_scan, daemon=True)
        self.threads.append(t1)
        t1.start()
        if SCAPY_AVAILABLE and self.network_interface:
            t2 = threading.Thread(target=self.network_monitor, daemon=True)
            self.threads.append(t2)
            t2.start()
        logger.info("Security System is running.")

    def stop(self):
        self.stop_event.set()
        logger.info("Stopping Security System...")

    # --- File Scanning ---
    def scan_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
                # Signature-based scan
                for sig in MALWARE_SIGNATURES:
                    if sig in content:
                        self.alert_queue.put(("malware_signature", file_path))
                        return True
                # Hash-based scan
                file_hash = hashlib.sha256(content).hexdigest()
                if file_hash in MALWARE_HASHES:
                    self.alert_queue.put(("malware_hash", file_path))
                    return True
        except Exception as e:
            logger.warning(f"Error scanning {file_path}: {e}")
        return False

    def scan_all_files(self):
        logger.info(f"Scanning all files in {self.root_dir}")
        for root, _, files in os.walk(self.root_dir):
            for file in files:
                file_path = os.path.join(root, file)
                self.scan_file(file_path)

    def periodic_file_scan(self):
        while not self.stop_event.is_set():
            self.scan_all_files()
            time.sleep(self.scan_interval)

    # --- Network Monitoring ---
    def network_monitor(self):
        if not SCAPY_AVAILABLE:
            logger.warning("Scapy not available, network monitoring disabled.")
            return
        logger.info(f"Starting network monitoring on {self.network_interface}")
        def process_packet(packet):
            # Example: Detect suspicious ports or IPs (expand as needed)
            if packet.haslayer(TCP):
                if packet[TCP].dport == 4444:  # Example suspicious port
                    self.alert_queue.put(("suspicious_port", packet.summary()))
        sniff(iface=self.network_interface, prn=process_packet, store=0, stop_filter=lambda x: self.stop_event.is_set())

    # --- Alert Handler ---
    def alert_handler(self):
        while not self.stop_event.is_set():
            try:
                alert_type, info = self.alert_queue.get(timeout=1)
                logger.warning(f"[ALERT] {alert_type}: {info}")
                # Implement additional response actions here (quarantine, shutdown, etc.)
            except queue.Empty:
                continue

    def run(self):
        self.start()
        alert_thread = threading.Thread(target=self.alert_handler, daemon=True)
        alert_thread.start()
        self.threads.append(alert_thread)
        try:
            while not self.stop_event.is_set():
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
            logger.info("Security System stopped by user.")

if __name__ == "__main__":
    # Example usage: scan all files in current directory every 5 minutes, monitor eth0
    secsys = UnifiedSecuritySystem(root_dir=os.getcwd(), scan_interval=300, network_interface=None)
    secsys.run()
