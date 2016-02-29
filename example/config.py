exe = "myprog.exe"
#staticlib = "libmylib.a"

# "gnu", "clang", and "msvc" are provided as predefined toolchain
toolchain = "gnu"
#toolchain = "msvc"

# optional
link_pool_depth = 1

# optional
builddir = {
    "gnu" :  "build"
  , "msvc" :  "build"
  , "clang" :  "build"
    }

# required
includes = {
    "gnu" : [ "-I." ]
  , "msvc" : [ "/I." ]
  , "clang" : [ "-I." ]
    }

# required
defines = {
    "gnu" : [ "-DEXAMPLE=1" ]
  , "msvc" : [ "/DEXAMPLE=1" ]
  , "clang" : [ "-DEXAMPLE=1" ]
    }

# required
cflags = {
    # https://stackoverflow.com/questions/5088460/flags-to-enable-thorough-and-verbose-g-warnings/9862800
    "gnu" : [ "-O2", "-g" ]
  , "msvc" : [ "/O2" ]
  , "clang" : [ "-O2", "-g" ]
    }

# required
# Warn as much as possible: http://qiita.com/MitsutakaTakeda/items/6b9966f890cc9b944d75
cxxflags = {
    "gnu" : [ "-O2", "-g", "-pedantic -Wall -Wextra -Wcast-align -Wcast-qual -Wctor-dtor-privacy -Wdisabled-optimization -Wformat=2 -Winit-self -Wmissing-declarations -Wmissing-include-dirs -Wold-style-cast -Woverloaded-virtual -Wredundant-decls -Wshadow -Wsign-conversion -Wsign-promo -Wstrict-overflow=5 -Wswitch-default -Wundef -Werror -Wno-unused" ]
  , "msvc" : [ "/O2", "/W4" ]
  , "clang" : [ "-O2", "-g", "-Werror -Weverything -Wno-c++98-compat -Wno-c++98-compat-pedantic" ]
    }

# required
ldflags = {
    "gnu" : [ ]
  , "msvc" : [ ]
  , "clang" : [ "-fsanitize=address" ]
    }

# optionsl
cxx_files = [ "main.cc" ]
c_files = [ "add.c" ]

# You can register your own toolchain through register_toolchain function
def register_toolchain(ninja):
    pass

