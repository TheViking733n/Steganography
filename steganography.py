from PIL import Image


def hide(image_file_path, text_file_path, output_file_path):
    content = ""
    try:
        with open(text_file_path, "r", encoding='utf-8') as f:
            content = f.read()
        
    except:
        print("Error occured while reading the text file.")

    binary_data = []
    for ch in content:
        b = bin(ord(ch))[2:]
        b = '0'*(8-len(b)) + b
        for bit in b:
            binary_data.append(int(bit))

    # Adding NULL in the end to represent EOF
    binary_data.extend([0]*32)
    while len(binary_data)%3:
        binary_data.append(0)


    im = Image.open(image_file_path)
    px = im.load()
    pos = 0
    for i in range(im.size[0]): # for every pixel
        for j in range(im.size[1]):
            R, G, B = px[i,j][:3]
            bit1, bit2, bit3 = binary_data[pos:pos+3]
            px[i,j] = R-(R&1)+bit1, G-(G&1)+bit2, B-(B&1)+bit3
            pos += 3
            if pos>=len(binary_data):
                break
        if pos>=len(binary_data):
            break

    im.save(output_file_path)




def unhide(image_file_path, text_file_path):
    im = Image.open(image_file_path)
    px = im.load()

    binary_data = []
    null = [0] * 32

    done = False
    for i in range(im.size[0]): # for every pixel
        for j in range(im.size[1]):
            R, G, B = px[i,j][:3]
            bit1, bit2, bit3 = R&1, G&1, B&1
            binary_data.extend([bit1, bit2, bit3])
            if binary_data[-32:] == null:
                done = True
                break
                
        if done:
            break
    
    decrypted_text = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        ascii_value = 0
        for bit in byte:
            ascii_value <<= 1
            ascii_value |= bit
        if ascii_value:
            decrypted_text.append(chr(ascii_value))
        
    print(*decrypted_text, sep="")

    with open(text_file_path, "w", encoding="utf-8") as f:
        f.write("".join(decrypted_text))