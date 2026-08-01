# blip

Library for making MicroPython-based games for small devices

## Getting Started

### Installing onto a Board

To install with Arduino Lab for MicroPython:

1. Go to `Add Package -> Advanced Options`
1. Enter the custom URL:
   ```
   github:menehune23/blip
   ```
1. Click `Install`

Alternately, to install with `mpremote`:

1.  Ensure `mpremote` is installed with:
    ```bash
    pip3 install mpremote
    ```
1.  Then run:
    ```bash
    python3 -m mpremote mip install github:menehune23/blip
    ```

### Writing a Program

Every program should have the following structure:

```python
import blip

def setup():
  # Runs once

def loop(dt: float):
  # Runs repeatedly

# Start device
blip.start("dev", setup, loop)
```

## Development

To update the package manifests after adding/removing files or dependencies:

1.  Ensure `"deps"` and `"version"` values are defined in `package.local.json`

1.  Run:
    ```bash
    make package
    ```

To install the local version of this package, run:

```bash
make install
```

To install the remote version of this package, run:

```bash
make install-remote
```
