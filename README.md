# FP16 ↔ Decimal Converter — Command Line Tool (IEEE 754 Half Precision)

This project provides a Python-based **command-line tool** for converting between:

- **Decimal numbers → IEEE 754 half-precision (16-bit) hexadecimal (FP16)**
- **IEEE 754 FP16 hexadecimal → Decimal numbers**

Floating-point values cannot be directly represented in synthesizable Verilog. Instead, hardware designs use IEEE 754 binary encodings. This tool helps generate FP16 constants and verify values for hardware simulation and testbench development.

---

## IEEE 754 Floating-Point Formats

The IEEE 754 standard defines multiple precision formats:

| Format | Bits |
|--------|------|
| Half Precision (FP16) | 16 |
| Single Precision (FP32) | 32 |
| Double Precision (FP64) | 64 |

This tool supports **only FP16 (half precision)**.

---

## Features

- Interactive command-line interface  
- Converts **decimal → FP16 hexadecimal**  
- Converts **FP16 hexadecimal → decimal**  
- Supports multiple values at once (comma-separated)  
- Displays detailed per-value conversion mapping  
- Suitable for hardware verification workflows  

---

## Requirements

- Python 3.8 or later  
- NumPy  

Install dependency using pip:

```bash
pip install numpy
