# Enki RGB Light Bluetooth Command Reference

This document provides a comprehensive reference for the hexadecimal commands used to control the Enki RGB Light via Bluetooth. Each command corresponds to a specific action, such as turning the device on/off, changing colors, or adjusting brightness.

## Commands

### Power Control ⚡

| Action      | Command            |
|-------------|--------------------|
| Turn Off    | `0000100103000000` |
| Turn On     | `0000100103010000` |

### Base Colors

| Color               | Command            |
|---------------------|--------------------|
| Normal Color        | `000012010401720000` |
| Normal Color + White| `000012010400fa0000` |
| White               | `000012010400990000` |

### Custom Colors 💡

| Color            | Command            |
|------------------|--------------------|
| Dark Violet      | `0000130704c1a70000` |
| Pink Violet     | `0000130704c7f50000` |
| Gray Violet     | `0000130704d1800000` |
| Blue Gray       | `00001307048c6e0000` |
| Gray            | `0000130704ab330000` |
| Pollen Yellow   | `000013070415fe0000` |
| Green           | `00001307045efe0000` |
| Mauve           | `0000130704c2e60000` |
| Blue Green      | `000013070467f60000` |
| Raspberry Red   | `0000130704f9f00000` |
| Sky Blue        | `00001307049bfe0000` |

### Brightness Control ☀️

| Brightness Level | Command            |
|------------------|--------------------|
| 12%              | `00001101031e0000` |
| 100%             | `0000110103ff0000` |
| 80%              | `0000110103cd0000` |
| 45%              | `0000110103730000` |

## Usage

To control the Enki RGB Light, send the corresponding hexadecimal command to the Bluetooth characteristic with UUID `0000a101-1115-1000-0001-617573746f6d`. Ensure the device is connected and the characteristic supports write operations.
