def write_1gb_file(name):
  data = "P" * 1024 * 1024 * 1024

  with open(name, "w") as f:
    f.write(data)

i = 0
while True:
  # it will make many panic_ files,
  # in the current directory:
  #   panic_0000000000.txt
  #   panic_0000000001.txt
  #   panic_0000000002.txt
  #   ...
  # each filled with 1073741824 times
  # the letter P, until the disk runs
  # out of space
  write_1gb_file(f"panic_{i:010}.txt")
  i += 1
