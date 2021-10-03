#python2 >> https://ideone.com/

from Crypto.Cipher import DES
 
# Reading plaintext-ciphertext pairs
pt_ct_list = 'e1d5e1fcaae4aba0b735c8fb2ae8797728b073a34b14c57be236c819e6d5f4bbd94f5748ff9d1e008fcad8d403e23d02811f20f5e3fcb394f28ac4aeb4993fb2ab4f3d8a93beb6bf7158c05975339849'
 
# Weak key list
key = ["0101010101010101", "FEFEFEFEFEFEFEFE", "E0E0E0E0F1F1F1F1", "1F1F1F1F0E0E0E0E"]
 
for i in key:
    key_obj = DES.new(i.decode("hex"), DES.MODE_ECB)
    # Taking one ciphertext from file
    ct = pt_ct_list.decode("hex")
    # Corresponding plaintext from file
    # Potential plaintext
    pot_pt = key_obj.decrypt(ct)
    print(pot_pt)
