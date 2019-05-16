import struct


def tamper(student_id):
  with open('lenna.bmp','r+b')as f:
    s1 = list(student_id)
    count = 0
    f.seek(54)
    while count < 12:
      if eval(s1[count]) == 0:
        f.read((eval(s1[count])+10)*3-3)
      else:
        if count == 0:
          f.read((eval(s1[count])*3)) 
        else:
          f.read((eval(s1[count])*3-3))
      f.write(b'\x00\x00\x00')
      count += 1

def detect():
  with open('lenna.bmp', 'rb') as f:
    bmp_file_header = f.read(14)

    bm, size, r1, r2, offset = struct.unpack('<2sIHHI', bmp_file_header)

    f.seek(offset)

    count = 12
    offset = 0
    last_offset = 0
    while count > 0:
      color = f.read(3)

      if color == b'\x00\x00\x00':

        if offset - last_offset == 10:
          print(0)
        else:
          print(offset - last_offset)

        last_offset = offset
        count -= 1

      offset += 1


if __name__ == '__main__':
  import sys
  tamper(sys.argv[1])

  detect()
