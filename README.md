# Kuroga

Kuroga is simple and single file meta build system for C/C++ application.
Kuroga generates ninja(https://ninja-build.org) script from portable python script.

## Requirements

* ninja 1.4+
* Python 2.6 or 2.7

## Supported platform

* [x] Linux
* [x] MacOSX
* [ ] Windows(Visual Studio)

## Install

Simply copy kuroga.py to your project directory. No other installation required(except for python itself).

### Setup configuration

Kuroga descibes project configuration in a python file.
See `example/config.py` for example.

Required components are

```
# one of `exe`, `staticlib`
exe       : exe filename
staticlib : static lib filename

toolchain : toolchain name
includes  : List of include directories
defines   : List of defines
c_flags   : CFLAGS
cxx_flags : CXXFLAGS
ld_flags  : LDFLAGS
```

Optional components are

```
cxx_files        : List of C++ files
c_files          : List of C files
link_pool_depth  : Link pool depth(default = 4)
```

### Add your toolchain

define `register_toolchain` function in `input.py`

### More customization

Simply edit `kuroga.py` as you wish ;-)

## TODO

* [ ] Subdirectory
* [ ] Android
* [ ] MSCV(Windows)
* [ ] Support complex build dependencies
* [ ] Support subninja

## License

`kuroga.py` is licensed under MIT license
