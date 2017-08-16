# fuse-3ds
FUSE Filesystem Python scripts for Nintendo 3DS files

Why Python? Because I can. And I can't be bothered to learn something else. Also these scripts are probably not very good but they work for me.

Requires Python 3.5+, [fusepy](https://github.com/terencehonles/fusepy), and [pycryptodomex](https://github.com/Legrandin/pycryptodome).

## mount_nand.py
Mounts NAND images. Currently only does CTR partitions (no TWL yet). Can read essentials backup by GodMode9, else OTP file/NAND CID must be provided in arguments.

```bash
python3 mount_nand.py [-h] [--otp OTP] [--cid CID] [--dev] [--ro] nand mount_point
```

Current files:
```
mount_point
├── agbsave.bin
├── ctrnand_fat.img
├── ctrnand_full.img
├── firm0.bin
├── firm1.bin
├── nand.bin
├── nand_minsize.bin
└── nand_hdr.bin
```