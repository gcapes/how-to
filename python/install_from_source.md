# Install python from source
- Download the source code
- `./configure --prefix=/home/mbexegc2/software/python/3.13.2-dev --enable-shared`

  This will install shared libraries for development work e.g. pyinstaller
- `make`
- `make install`
- `export LD_LIBRARY_PATH=/home/mbexegc2/software/python/3.13.2-dev/lib:$LD_LIBRARY_PATH`

  This enables python to find the shared libraries at run time.
