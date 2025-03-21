file_path = "extra.bin"

with open(file_path,"wb") as bin_file:
    bin_file.write(b'\x48\x65\x6C\x6C\x6F\x20\x42\x69\x6E\x61\x72\x79')  # "Hello Binary" in hex
print(f"Binary file created at:{file_path}")
