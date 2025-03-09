import threading
import time

def download_file(file_name, file_size_mb):
    print(f"เริ่มดาวน์โหลดไฟล์: {file_name} (ขนาด {file_size_mb} MB)")
    start_time = time.time()
    
    # คำนวณเวลาดาวน์โหลด (1 MB ใช้เวลา 2 วินาที)
    total_time = file_size_mb * 2
    chunk_time = 1  # อัปเดตความคืบหน้าทุก 1 วินาที
    chunks = int(total_time / chunk_time)  # จำนวนครั้งที่ต้องอัปเดตความคืบหน้า
    
    for i in range(chunks):
        time.sleep(chunk_time)  # หน่วงเวลาตาม chunk_time
        progress = (i + 1) / chunks * 100  
        progress_bar = "-" * int(progress / 5)  # สร้างเส้นขีด (1 ขีด = 5%)
        print(f"\r{file_name}: [{progress_bar:<20}] {progress:.0f}%", end="", flush=True)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nดาวน์โหลดไฟล์ {file_name} เสร็จสิ้น! ใช้เวลา {elapsed_time:.2f} วินาที")

if __name__ == "__main__":
    # ตัวอย่างรายการไฟล์ที่ต้องการดาวน์โหลด
    files_to_download = [
        {"name": "file1.zip", "size": 20},  
        {"name": "file2.zip", "size": 10},  
        {"name": "file3.zip", "size": 5},   
        {"name": "file4.zip", "size": 30},  
    ]

    
    threads = []
    for file in files_to_download:
        thread = threading.Thread(target=download_file, args=(file["name"], file["size"]))
        threads.append(thread)
        thread.start()

    
    for thread in threads:
        thread.join()

    print("The download is complete!")