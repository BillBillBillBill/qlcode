# coding: utf-8
import struct


def get_file(f):
    meta_data = f.read(5)
    status = struct.unpack('h', meta_data[0] + '\x00')[0]
    file_size = struct.unpack('i', meta_data[1:][::-1])[0]
    print status, file_size
    if status == 2:
        print "no more picture"
        return
    file_data = f.read(file_size)
    output_file = open('out/'+str(file_size), 'wb')
    output_file.write(file_data)
    get_file(f)


if __name__ == '__main__':
    f = open('/home/bill/Desktop/github/qlcoder/766e/rf.data', 'rb')
    get_file(f)
