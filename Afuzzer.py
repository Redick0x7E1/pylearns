import sys


def bufferOverflow(bufferSize):
    buffer = []
    letter = 'A'
    buffer.append(f"{letter}"*bufferSize)
    print(''.join(buffer))
    return ''.join(buffer)
    
bufferOverflow(4000)