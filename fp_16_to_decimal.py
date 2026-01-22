import struct
import numpy as np


def decimal_to_hex(value):
    """
    Convert a single decimal value to IEEE 754 16-bit hex.
    
    Args:
        value (float): Decimal number to convert
        
    Returns:
        str: Hexadecimal FP16 representation (e.g., '0x3C00')
    """
    fp16_value = np.float16(value)
    fp16_bytes = struct.pack('>e', fp16_value)
    fp16_int = struct.unpack('>H', fp16_bytes)[0]
    return '0x' + format(fp16_int, '04X')


def decimals_to_hex_array(decimal_array):
    """
    Convert an array of decimal values to IEEE 754 16-bit hex array.
    
    Args:
        decimal_array (list): List of decimal numbers
        
    Returns:
        list: List of hexadecimal FP16 values
    """
    return [decimal_to_hex(val) for val in decimal_array]


def hex_to_decimal(hex_value):
    """
    Convert IEEE 754 16-bit hex back to decimal.
    
    Args:
        hex_value (str): Hexadecimal FP16 value (e.g., '0x3C00')
        
    Returns:
        float: Decimal representation
    """
    bits_int = int(hex_value, 16)
    bytes_data = struct.pack('>H', bits_int)
    return struct.unpack('>e', bytes_data)[0]


def convert_decimal_to_fp16(decimal_input):
    """
    Convert decimal value(s) to FP16 hexadecimal.
    
    Args:
        decimal_input (float or list): Single decimal or array of decimals
        
    Returns:
        str or list: Single hex value or list of hex values
    """
    if isinstance(decimal_input, (list, tuple, np.ndarray)):
        return decimals_to_hex_array(decimal_input)
    else:
        return decimal_to_hex(decimal_input)


def convert_fp16_to_decimal(hex_input):
    """
    Convert FP16 hexadecimal back to decimal.
    
    Args:
        hex_input (str or list): Single hex value or list of hex values
        
    Returns:
        float or list: Single decimal or list of decimals
    """
    if isinstance(hex_input, (list, tuple)):
        return [hex_to_decimal(h) for h in hex_input]
    else:
        return hex_to_decimal(hex_input)



if __name__ == "__main__":
    print("=" * 80)
    print("IEEE 754 16-bit Half-Precision Float Converter")
    print("FP16 Hexadecimal to Decimal Converter")
    print("=" * 80)
    
    while True:
        print("\n--- Input FP16 Hexadecimal Array ---")
        print("Enter FP16 hex values separated by commas (e.g., 0x0000, 0x3C00, 0xBE00, 0x4200)")
        print("Or type 'quit' to exit:")
        
        user_input = input("\nEnter FP16 hex array: ").strip()
        
        if user_input.lower() == 'quit':
            print("Exiting...")
            break
        
        try:
            # Parse user input
            hex_strings = user_input.split(',')
            hex_array = [val.strip() for val in hex_strings]
            
            # Convert to decimal
            decimal_array = convert_fp16_to_decimal(hex_array)
            
            # Display results
            print("\n" + "=" * 80)
            print("CONVERSION RESULTS")
            print("=" * 80)
            print(f"\nInput FP16 Hex Array:    {hex_array}")
            print(f"Output Decimal Array:    {decimal_array}")
            
            # Show detailed mapping
            print("\n--- Detailed Conversion ---")
            for i, (hex_val, dec) in enumerate(zip(hex_array, decimal_array)):
                print(f"  [{i}] {hex_val} -> {dec:12.6f}")
            
            print("\n" + "=" * 80)
            
        except ValueError as e:
            print(f"\nError: Invalid input. Please enter hex values in format 0xXXXX separated by commas.")
            print(f"Details: {e}")
        except Exception as e:
            print(f"\nUnexpected error: {e}")
        
        print("\nWould you like to convert another array? (yes/no): ", end="")
        if input().strip().lower() not in ['yes', 'y']:
            print("Exiting...")
            break
