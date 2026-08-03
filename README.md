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

### Writing Programs

The example below shows how a typical blip program is structured:

```python
import blip
import time

# Runs once
def setup():
  # Show some start text
  blip.clear()
  blip.text("Get ready!", 25, 25)
  blip.show()
  time.sleep(1)

# Runs repeatedly
def loop(dt: float):
  # Erase the last frame
  blip.clear()

  # Add to the current frame
  if blip.button("a").is_pressed:
    blip.text("Hello!", 40, 25)
  else:
    blip.text("Press 'A'", 30, 25)

  # Show the current frame
  blip.show()

# Start running 'setup()' and 'loop()'
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

To package and do a local install in one command, run:

```bash
make dev
```

To install the remote version of this package, run:

```bash
make install-remote
```

> Note that `make install-remote` installs from the current branch's remote content!
