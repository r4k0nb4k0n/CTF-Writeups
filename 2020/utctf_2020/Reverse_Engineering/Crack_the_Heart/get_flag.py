key = [
	0x71, 0xe5, 0x63, 0x6e, 0x67, 0xac, 0x1f, 0x16,
	0xbb, 0xae, 0x4f, 0x14, 0x56, 0x2d, 0x3f, 0x93,
	0x9b, 0x07, 0x52, 0xc8, 0xa0, 0x37, 0x00, 0xb5,
	0xc2, 0xa0, 0xff, 0xad, 0xa8, 0xd0, 0xb7, 0xcc,
	0x12, 0x24, 0xf9, 0xeb, 0x91, 0xe9, 0x9d, 0x68,
	0xed, 0x49, 0x9d, 0xf9, 0x9b, 0xdf, 0x9f, 0xbf,
	0xaf, 0xa5, 0xd3, 0xc0, 0x2b, 0x73, 0x87, 0x3d,
	0x48, 0x4b, 0xbb, 0x95, 0xab, 0xa6, 0x86, 0xa4,
	0x1a, 0xd6, 0x97, 0x65, 0x5c, 0xef, 0x64, 0x5c,
	0xa5, 0xe1, 0x31, 0x37, 0xe9, 0xbb, 0x43, 0xb6,
	0xa1, 0xa2
 ]

encrypted = [
	0x04, 0x91, 0x05, 0x02, 0x06, 0xcb, 0x64, 0x61,
	0xd3, 0xcf, 0x3b, 0x4b, 0x67, 0x4b, 0x11, 0xbd,
	0xb5, 0x29, 0x3b, 0x97, 0xcd, 0x56, 0x70, 0xc5,
	0xf1, 0xc4, 0xa0, 0xc0, 0xf1, 0x8f, 0xda, 0xff,
	0x7f, 0x14, 0x8b, 0x92, 0xce, 0x87, 0xae, 0x10,
	0x99, 0x16, 0xe9, 0x96, 0xc4, 0xa6, 0xaf, 0xca,
	0xdd, 0xd6, 0xfd, 0xee, 0x05, 0x5d, 0xe6, 0x55,
	0x29, 0x23, 0xda, 0xfd, 0xca, 0x8a, 0xa6, 0xce,
	0x71, 0xbc, 0xfc, 0x4b, 0x72, 0xc1, 0x4a, 0x29,
	0xcb, 0x8d, 0x54, 0x44, 0x9a, 0x9b, 0x78, 0x9f,
	0x9e, 0xdf
]

flag = ''
for k, e in zip(key, encrypted):
	flag += chr(k ^ e)

with open('flag', 'w') as f:
	f.write(flag)