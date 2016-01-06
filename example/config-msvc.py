exe = "myprog.exe"
#staticlib = "libmylib.a"

# "gnu" or "msvc" are provided as predefined toolchain
toolchain = "msvc"

# optional
link_pool_depth = 1

# reuired
includes = {
    "gnu" : [ "-I." ]
  , "msvc" : [ "/I." ]
  , "clang" : [ "-I." ]
    }

# reuired
defines = {
    "gnu" : [ "-DEXAMPLE=1" ]
  , "msvc" : [ "/DEXAMPLE=1" ]
  , "clang" : [ "-DEXAMPLE=1" ]
    }

# reuired
cflags = {
    "gnu" : [ "-O2", "-g" ]
  , "msvc" : [ "/O2" ]
  , "clang" : [ "-O2", "-g" ]
    }

# reuired
cxxflags = {
    "gnu" : [ "-O2", "-g" ]
  , "msvc" : [ "/O2" ]
  , "clang" : [ "-O2", "-g", "-fsanitize=address" ]
    }

# reuired
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

    #ninja.rule('clangcxx', description='CXX $out',
    #    command='$clangcxx -MMD -MF $out.d $clangdefines $clangincludes $clangcxxflags -c $in -o $out',
    #    depfile='$out.d', deps='gcc')
    #ninja.rule('clangcc', description='CC $out',
    #    command='$clangcc -MMD -MF $out.d $clangdefines $clangincludes $clangcflags -c $in -o $out',
    #    depfile='$out.d', deps='gcc')
    #ninja.rule('clanglink', description='LINK $out', pool='link_pool',
    #    command='$clangld $clangldflags -o $out $in $libs')
    #ninja.rule('clangar', description='AR $out', pool='link_pool',
    #    command='$clangar rsc $out $in')
    #ninja.rule('clangstamp', description='STAMP $out', command='touch $out')
    #ninja.newline()

    #ninja.variable('clangcxx', 'clang++')
    #ninja.variable('clangcc', 'clang')
    #ninja.variable('clangld', 'clang++')
    #ninja.variable('clangar', 'ar')
    #ninja.newline()


